from material.plugins.blog.config import BlogConfig
from mkdocs.config.config_options import Type

class CustomBlogConfig(BlogConfig):
    cache = Type(bool, default = True)
    cache_dir = Type(str, default = ".cache/plugin/blog")

    qr_dir = Type(str, default = "assets/images/qr")

    speakers = Type(bool, default = True)
    sponsors = Type(bool, default = True)