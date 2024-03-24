import feedparser
import pyshorteners

class NewsFetcher:
    @staticmethod
    def fetch_top_news(topic, num_headlines=3):
        url = f"https://rss.nytimes.com/services/xml/rss/nyt/{topic}.xml"
        feed = feedparser.parse(url)
        if not feed.get('entries'):
            return []
        top_headlines = [(entry.title.strip(), entry.link) for entry in feed.entries[:num_headlines]]
        return top_headlines

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

def queryNews(topic):
    top_news = NewsFetcher.fetch_top_news(topic.lower(), num_headlines=1)
    if top_news:
        for idx, (headline, link) in enumerate(top_news, start=1):
            short_link = shorten_url(link)
            return f"{idx}. {headline} ({short_link})"
    else:
        return f"No {topic} news available."
