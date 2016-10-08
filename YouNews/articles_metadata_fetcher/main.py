import sys
from YouNews.articles_metadata_fetcher.articles_metadata_fetcher import ArticlesMetadataFetcher


def main(args=None):
    """The main routine.
    :param args:
    """
    if args is None:
        args = sys.argv[1:]

    amf = ArticlesMetadataFetcher()
    amf.run()

if __name__ == "__main__":
    main()