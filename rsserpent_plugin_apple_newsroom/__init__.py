from rsserpent_rev.models import Persona, Plugin

from . import route

plugin = Plugin(
    name="rsserpent-plugin-apple-newsroom",
    author=Persona(
        name="RSSerpent-Rev",
        link="https://github.com/RSSerpent-Rev",
        email="beijiu572@gmail.com",
    ),
    prefix="/apple-newsroom",
    repository="https://github.com/RSSerpent-Rev/rsserpent-plugin-apple-newsroom",
    routers={route.path: route.provider},
)
