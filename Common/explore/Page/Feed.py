# -*-coding:UTF-8-*-

from Common.conf.ts_configure import ConfList
from Lib.Article import Article


class Feed(object):

    def __init__(self, data):
        """初始化数据

        :param data:Feed流数据 
        """
        self.data = data

    def banner(self):
        """banner位

        :return: banner位数据
        """
        return self.data['data']['info']

    @staticmethod
    def request(page=1, ver=1):
        """
        feed流请求数据，默认为第一页，3.7版本，返回json格式
        :param page: 页数
        :param ver: 版本号
        :return: json
        """
        request = Article.article_list_home(hostname=ConfList['hostname'],
                                            uid=ConfList['uid'],
                                            accesstoken=ConfList['accesstoken'],
                                            page=page,
                                            channel=ConfList['channel'],
                                            ver=ver)
        return request
