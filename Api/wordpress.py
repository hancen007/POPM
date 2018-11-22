
from Api.Req import Req
from urllib.parse import urljoin


class Wordpress(Req):
    """Testing different HTTP verbs"""

    def __init__(self):
        super(Wordpress,self).__init__()
        self.url = urljoin(self.host, '/wp-json/wp/v2/posts')

    def KeyWord(self):
        re = self.get(self.url)
        return re


if __name__ == "__main__":

    E = Wordpress()
    E.KeyWord()