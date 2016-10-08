from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


class ArticleMetadata(object):
    __tablename__ = 'articles'

    author = Column(String)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    published_at = Column(Date)

    def __init__(self, article_metadata, content=""):
        self.article_metadata = article_metadata
        self.content = content
