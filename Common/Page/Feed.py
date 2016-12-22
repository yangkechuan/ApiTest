# -*-coding:UTF-8-*-

from Lib.Article import Article
from Common.conf.configure import ConfList


class Feed(object):

    def __init__(self, data):
        self.data = data

    def banner(self):
        return self.data['data']['info']

    def operation(self):
        for operation in self.data['data']['list']:
            if 'operation' in operation:
                return operation
        return None

    def gif(self):
        for gif in self.data['data']['list']:
            if 'gif' in gif:
                return gif
        return None


# ######################################################################
#             以下为feed流功能点
# ######################################################################

    """
    feed流请求数据，默认为第一页，3.7版本，返回json格式
    """
    @staticmethod
    def request(page=1, ver=3.7):
        request = Article.article_list_home(uid=ConfList['uid'],
                                            accesstoken=ConfList['accesstoken'],
                                            page=page,
                                            channel=ConfList['channel'],
                                            ver=ver)
        return request

    """
    不感兴趣功能，可以在feed流删除该文章,默认删除第五页，第一条数据
    """
    @staticmethod
    def article_remove(page=5, ver=3.7):

        article_id = Feed.request(page=page)['data']['list'][0]['id']
        request = Article.article_remove(uid=ConfList['uid'],
                                         accesstoken=ConfList['accesstoken'],
                                         ver=ver,
                                         id=article_id)
        return request
