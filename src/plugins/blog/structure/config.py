from datetime import datetime
from email.policy import default

from material.plugins.blog.structure import PostConfig
from mkdocs.config.base import Config
from mkdocs.config.config_options import ListOfItems, Optional, Type, Choice, SubConfig, URL, OptionallyRequired


class CustomPostConfig(PostConfig):
    type = Optional(Choice(["news", "maintenance", "event"]))

class NewsSourceConfig(Config):
    title = Type(str)
    url = URL()

class NewsConfig(CustomPostConfig):
    source = OptionallyRequired(SubConfig(NewsSourceConfig))

class AnnouncementBanner(Config):
    enabled = Type(bool, default = False)
    message = Optional(Type(str))

class MaintenanceConfig(CustomPostConfig):
    start = Type(datetime)
    end = Type(datetime)
    banner = SubConfig(AnnouncementBanner)

class ScheduleItem(Config):
    title = Type(str)
    description = OptionallyRequired(Type(str))
    start = Type(datetime)
    end = Type(datetime)
    icon = Optional(Type(str))
    location = Optional(Type(str))
    speakers = ListOfItems(Type(str), default = [])
    disabled = Optional(Type(str|bool))

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
    speakers = ListOfItems(Type(str), default = [])
    sponsors = ListOfItems(Type(str), default = [])
    registration = SubConfig(Registration)
    schedule = ListOfItems(SubConfig(Schedule), default = [])
    image = Optional(Type(str))
    scheme = Optional(Type(str))
    banner = SubConfig(AnnouncementBanner)
