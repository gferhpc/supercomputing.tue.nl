# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from datetime import datetime

from material.plugins.blog.structure import PostConfig
from material.plugins.blog.structure.options import UniqueListOfItems
from mkdocs.config.base import Config
from mkdocs.config.config_options import ListOfItems, Optional, Type, Choice, SubConfig, URL


class CustomPostConfig(PostConfig):
    type = Optional(Choice(["news", "maintenance", "event"]))

class NewsConfig(CustomPostConfig):
    pass # no additional properties

class MaintenanceConfig(CustomPostConfig):
    start = Type(datetime)
    end = Type(datetime)

class ScheduleItem(Config):
    title = Type(str)
    start = Type(datetime)
    end = Type(datetime)
    icon = Optional(Type(str))
    location = Optional(Type(str))
    speakers = UniqueListOfItems(Type(str), default = [])

class Schedule(ScheduleItem):
    schedule = ListOfItems(SubConfig(ScheduleItem), default = [])

class RegistrationOption(Config):
    title = Type(str)
    url = URL()
    qr = Type(bool, default = False)

class Registration(Config):
    enabled = Type(bool, default = False)
    description = Optional(Type(str))
    options: list[RegistrationOption] = ListOfItems(SubConfig(RegistrationOption), default = [])

class EventConfig(CustomPostConfig):
    start = Type(datetime)
    end = Type(datetime)
    location = Optional(Type(str))
    price = Optional(Type(float))
    speakers = UniqueListOfItems(Type(str), default = [])
    sponsors = UniqueListOfItems(Type(str), default = [])
    registration = SubConfig(Registration)
    schedule = ListOfItems(SubConfig(Schedule), default = [])
    image = Optional(Type(str))
    scheme = Optional(Type(str))
