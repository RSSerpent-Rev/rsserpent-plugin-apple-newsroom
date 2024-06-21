import arrow
from feedgen.feed import FeedGenerator
from rsserpent_rev.utils import HTTPClient, cached
from rsserpent_rev.models import Feed  # noqa: F401

path = "/apple-newsroom"


@cached
async def provider() -> Feed:
    """Define a basic example data provider function."""
    async with HTTPClient() as client:
        resp = await client.get("https://www.apple.com.cn/newsroom/archive.json")
        r = resp.json()
        fg = FeedGenerator()
        fg.title("Apple Newsroom")
        fg.link(href="https://www.apple.com.cn/newsroom/")
        fg.description("Apple Newsroom")
        fg.id("https://www.apple.com.cn/newsroom/")
        for item in r["results"][0]["result"]:
            fe = fg.add_entry(order="append")
            fe.id(item["link"])
            fe.title(item["title"])
            fe.link(href="https://www.apple.com.cn/newsroom/" + item["link"])
            fe.description(item["description"])
            fe.pubDate(arrow.get(item["date"], "YYYY 年 M 月 D 日").datetime)
            fe.category(term=item["category"]["text"])
    return fg
