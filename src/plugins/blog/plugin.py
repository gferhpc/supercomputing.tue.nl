# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import annotations

import json
import os
import posixpath
from datetime import datetime
from material.plugins.blog.plugin import BlogPlugin
from material.plugins.social.plugin import _digest
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority, BasePlugin
from mkdocs.structure.files import File
from qrcode.image.styles.moduledrawers.svg import SvgCircleDrawer
from qrcode.image.svg import SvgImage
from qrcode.main import QRCode

from .config import CustomBlogConfig
from .structure import Excerpt, Post, View
from .structure.config import Registration


class CustomBlogPlugin(BlogPlugin[CustomBlogConfig]):
    manifest: dict[str, str] = {}

    config: CustomBlogConfig

    def on_config(self, config):
        if not self.config.enabled:
            return
        super().on_config(config)

        # Resolve cache directory (once) - this is necessary, so the cache is
        # always relative to the configuration file, and thus project, and not
        # relative to the current working directory, or it would not work with
        # the projects plugin.
        path = os.path.abspath(self.config.cache_dir)
        if path != self.config.cache_dir:
            self.config.cache_dir = os.path.join(
                os.path.dirname(config.config_file_path),
                os.path.normpath(self.config.cache_dir)
            )

            # Ensure cache directory exists
            os.makedirs(self.config.cache_dir, exist_ok = True)

        # Initialize manifest
        self.manifest_file = os.path.join(
            self.config.cache_dir, "manifest.json"
        )

        # Load manifest if it exists and the cache should be used
        if os.path.isfile(self.manifest_file) and self.config.cache:
            try:
                with open(self.manifest_file) as f:
                    self.manifest = json.load(f)
            except:
                pass

    @event_priority(-50)
    def on_page_markdown(self, markdown, *, page: Post, config, files):
        if not self.config.enabled:
            return

        # Skip if page is not a post managed by this instance - this plugin has
        # support for multiple instances, which is why this check is necessary
        if page not in self.blog.posts:

            view = self._resolve_original(page)
            if view in self._resolve_views(self.blog):
                for post in self.blog.posts:
                    if post.excerpt:
                        post.excerpt.render(page, self.config.post_excerpt_separator)

            if page.is_homepage or page.is_top_level:
                page.blog = self.blog

            if not self.config.pagination:
                return

            # We set the contents of the view to its title if pagination should
            # not keep the content of the original view on paginated views
            if not self.config.pagination_keep_content:
                view = self._resolve_original(page)
                if view in self._resolve_views(self.blog):

                    # If the current view is paginated, use the rendered title
                    # of the original view in case the speaker set the title in
                    # the page's contents, or it would be overridden with the
                    # one set in mkdocs.yml, leading to inconsistent headings
                    assert isinstance(view, View)
                    if view != page:
                        name = view._title_from_render or view.title
                        return f"# {name}"

            # Nothing more to be done for views
            return


        page.blog = self.blog

        # Extract and assign authors to post, if enabled
        if self.config.authors:
            for name in page.config.authors:
                if name not in self.authors:
                    raise PluginError(f"Couldn't find author '{name}'")

                # Append to list of authors
                page.authors.append(self.authors[name])

        if self.config.speakers and page.is_event():
            for key, name in enumerate(page.config.speakers):
                if name not in self.authors:
                    raise PluginError(f"Couldn't find speaker '{name}'")
                page.config.speakers[key] = self.authors[name]

            for schedule in page.config.schedule:
                for key, name in enumerate(schedule.speakers):
                    if name not in self.authors:
                        raise PluginError(f"Couldn't find speaker '{name}'")
                    schedule.speakers[key] = self.authors[name]
                for child_schedule in schedule.schedule:
                    for key, name in enumerate(child_schedule.speakers):
                        if name not in self.authors:
                            raise PluginError(f"Couldn't find speaker '{name}'")
                        child_schedule.speakers[key] = self.authors[name]

        if self.config.sponsors and page.is_event():
            for key, name in enumerate(page.config.sponsors):
                if name not in self.authors:
                    raise PluginError(f"Couldn't find sponsor '{name}'")
                page.config.sponsors[key] = self.authors[name]

        # Extract settings for excerpts
        separator = self.config.post_excerpt_separator
        max_authors = self.config.post_excerpt_max_authors
        max_categories = self.config.post_excerpt_max_categories

        # Ensure presence of separator and throw, if its absent and required -
        # we append the separator to the end of the contents of the post, if it
        # is not already present, so we can remove footnotes or other content
        # from the excerpt without affecting the content of the excerpt
        if separator not in page.markdown:
            if self.config.post_excerpt == "required":
                docs = os.path.relpath(config.docs_dir)
                path = os.path.relpath(page.file.abs_src_path, docs)
                raise PluginError(
                    f"Couldn't find '{separator}' in post '{path}' in '{docs}'"
                )

        # Create excerpt for post and inherit authors and categories - excerpts
        # can contain a subset of the authors and categories of the post
        page.excerpt = Excerpt(page, config, files)
        page.excerpt.authors = page.authors[:max_authors]
        page.excerpt.categories = page.categories[:max_categories]

    def _generate_qr(self, post: Post, config: MkDocsConfig):
        registration: Registration = post.config.registration

        if not registration.enabled:
            return

        for option in registration.options:
            if not option.qr:
                continue

            # Compute digest of all fingerprints - we use this value to check if
            # the exact same card was already generated and cached
            hash = _digest(option.url)

            file = self._path_to_qr_file(f"{hash}.svg", config)

            qr = QRCode()
            qr.add_data(option.url)

            img = qr.make_image(image_factory = SvgImage, module_drawer = SvgCircleDrawer())
            os.makedirs(os.path.dirname(file.abs_src_path), exist_ok = True)
            img.save(file.abs_src_path)

            # Update manifest by associating file with hash
            self.manifest[file.url] = hash
            option.qr_url = file.url
            file.copy_file()

    def _path_to_qr_file(self, path: str, config: MkDocsConfig):
        assert path.endswith(".svg")
        return File(
            posixpath.join(self.config.qr_dir, path),
            self.config.cache_dir,
            config.site_dir,
            False
        )

    # Register template filters for plugin
    def on_env(self, env, *, config, files):
        super().on_env(env, config=config, files=files)

        # Filter for formatting dates related to posts
        def date_filter(date: datetime, format: str = None):
            return self._format_date_for_post(date, config, format)

        # Register custom template filters
        env.filters["date"] = date_filter
        env.globals['now'] = datetime.now

    # Save manifest after build
    def on_post_build(self, *, config):
        if not self.config.enabled:
            return

        # Save manifest if cache should be used
        if self.config.cache:
            with open(self.manifest_file, "w") as f:
                f.write(json.dumps(self.manifest, indent = 2, sort_keys = True))

    # Resolve post - the caller must make sure that the given file points to an
    # actual post (and not a page), or behavior might be unpredictable
    def _resolve_post(self, file: File, config: MkDocsConfig):
        post = Post(file, config)

        if post.is_event():
            self._generate_qr(post, config)

        # Compute path and create a temporary file for path resolution
        path = self._format_path_for_post(post, config)
        temp = self._path_to_file(path, config, temp=False)

        # Replace destination file system path and URL
        file.dest_uri = temp.dest_uri
        file.abs_dest_path = temp.abs_dest_path
        file.url = temp.url

        # Replace canonical URL and return post
        post._set_canonical_url(config.site_url)
        return post

    # Format date for post
    def _format_date_for_post(self, date: datetime, config: MkDocsConfig, format: str = None):
        if not format:
            format = self.config.post_date_format
        return self._format_date(date, format, config)
