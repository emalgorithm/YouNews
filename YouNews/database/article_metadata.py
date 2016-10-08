from sqlalchemy import Column, Integer, String


class ArticleMetadata(object):
    __tablename__ = 'articlesMetadata'

    author = Column(String)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    published_at = Column(String)

    def __init__(self, author, title, description, url, published_at):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.published_at = published_at
