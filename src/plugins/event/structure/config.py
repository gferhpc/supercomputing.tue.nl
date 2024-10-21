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

from material.plugins.blog.structure import PostConfig
from mkdocs.config.config_options import ListOfItems, Optional, Type, Choice


class PostConfig(PostConfig):
    type = Optional(Choice(["news", "maintenance", "event"]))
    speakers = ListOfItems(Type(str), default = []) # = authors
    sponsors = ListOfItems(Type(dict), default = [])
    location = Optional(Type(str))
    location_url = Optional(Type(str))
    price = Optional(Type(float))
    past = Optional(Type(bool))
    image = Optional(Type(str))
    scheme = Optional(Type(str))
    title = Optional(Type(str))
    description = Optional(Type(str))
    actions = ListOfItems(Type(dict), default = [])
    schedule = ListOfItems(Type(dict), default = [])
