import younews.third_api_helpers.news_api as news_api
from YouNews.database.article_metadata import ArticleMetadata
from younews.kafka_client.producer import Producer


class ArticlesMetadataFetcher(Producer):

    def __init__(self):
        self.db = db.Session()

    def run(self):
        articles = news_api.get_latest_articles('bbc-news')
        new_articles = self.filter_new_articles(articles)
        new_articles = self.create_article_models(new_articles)


        self.send(ArticleMetadata, new_articles)

    def filter_new_articles(self, articles):
        return filter(lambda article: db.article_exists(article['title'],
                                                        article['publishedAt']), articles)

    def create_article_models(self, articles):
        return map(lambda article: ArticleMetadata(article['title'],
                                                   article['date']))




