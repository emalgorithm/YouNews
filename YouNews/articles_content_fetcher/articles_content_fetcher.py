import requests

from YouNews.database.article_metadata import Article
from YouNews.kafka_client.consumer import Consumer
from YouNews.kafka_client.producer import Producer


class ArticlesContentFetcher(Consumer, Producer):
    def __init__(self):
        super().__init__(Article)
        self.api_key = "1a31ef2d2fb3040e57806136973e3379"

    def on_received_message(self, msg):
        url = "https://document-parser-api.lateral.io/"

        querystring = {"url": "{{}}".format(msg.url)}

        headers = {
            'subscription-key': self.api_key,
            'content-type': "application/json"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.body)

        msg.content = response.body


