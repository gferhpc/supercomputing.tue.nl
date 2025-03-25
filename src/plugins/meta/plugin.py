from mkdocs.config import Config
from mkdocs.config.config_options import SubConfig, OptionallyRequired, Optional, Type
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin, log
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from plugins.meta.hero import HeroConfig


class MetaPluginConfig(Config):
    hero = OptionallyRequired(SubConfig(HeroConfig))
    knowledgebase = Type(bool, default=False)

class MetaPlugin(BasePlugin):
    def on_page_markdown(self, markdown: str, /, *, page: Page, config: MkDocsConfig, files: Files):
        self.config = MetaPluginConfig(page.file.abs_src_path)
        self.config.load_dict({
            key: page.meta[key] for key in (set(page.meta.keys()) & set(self.config.keys()))
        })

        errors, warnings = self.config.validate()
        for _, w in warnings:
            log.warning(w)
        for k, e in errors:
            raise PluginError(
                f"Error reading metadata '{k}' of post '{page.title}' in '{page.file}':\n"
                f"{e}"
            )
