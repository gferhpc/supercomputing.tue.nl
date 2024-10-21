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

import os
from datetime import datetime
from material.plugins.blog.author import Author
from material.plugins.blog.plugin import BlogPlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority
from mkdocs.structure.files import File
from .structure import Excerpt, Post, View


class EventPlugin(BlogPlugin):
    @event_priority(-50)
    def on_page_markdown(self, markdown, *, page, config, files):
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

            if page.is_homepage:
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

        # Extract and assign authors to post, if enabled
        if self.config.authors:
            for name in page.config.authors:
                if name not in self.authors:
                    raise PluginError(f"Couldn't find speaker '{name}'")

                # Append to list of authors
                page.authors.append(self.authors[name])

        if page.config.schedule:
            for schedule in page.config.schedule:
                if "authors" in schedule:
                    schedule["authors"] = self._populate_authors(schedule["authors"])

                    if "schedule" in schedule:
                        for sub_schedule in schedule["schedule"]:
                            if "authors" in sub_schedule:
                                sub_schedule["authors"] = self._populate_authors(sub_schedule["authors"])

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

    def _populate_authors(self, authors: list):
        resolved_authors: list[Author] = []

        for name in authors:
            if name not in self.authors:
                raise PluginError(f"Couldn't find author '{name}'")

            # Append to list of authors
            resolved_authors.append(self.authors[name])

        return resolved_authors

    # Register template filters for plugin
    def on_env(self, env, *, config, files):
        super().on_env(env, config=config, files=files)

        # Filter for formatting dates related to posts
        def date_filter(date: datetime, format: str = None):
            return self._format_date_for_post(date, config, format)

        # Register custom template filters
        env.filters["date"] = date_filter

    # Resolve post - the caller must make sure that the given file points to an
    # actual post (and not a page), or behavior might be unpredictable
    def _resolve_post(self, file: File, config: MkDocsConfig):
        post = Post(file, config)

        # @TODO fix in jinja2 template...
        post.config.past = post.config.date.end < datetime.now() if post.config.date.end else post.config.date.created < datetime.now()

        if not post.config.date.start:
            post.config.date.start = post.config.date.created
        if not post.config.date.end:
            post.config.date.end = post.config.date.created

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
