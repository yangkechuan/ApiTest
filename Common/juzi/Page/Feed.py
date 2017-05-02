# -*-coding:UTF-8-*-

from Lib.Article import Article
from Common.conf.configure import ConfList


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

    def topic_recommend(self):
        """专题推荐
        
        专题推荐在banner下的第一个位置，可以不存在
        :return:专题文章 
        """
        topic = self.data['data']['list'][0]
        if topic['type'] == 3:
            return topic
        return None

    def operation(self):
        """运营位

        :return:运营位数据
        """
        for operation in self.data['data']['list']:
            if 'operation' in operation:
                return operation
        return None

    def gif(self):
        """Feed流Gif

        :return:Feed流gif
        """
        for gif in self.data['data']['list']:
            if 'gif' in gif:
                return gif
        return None

    def photo_gallary(self):
        """图集文章
        
        同一页数据中可能存在多个图集，全部返回并验证
        :return: 图集文章
        """
        photos = []
        for photo in self.data['data']['list']:
            if photo['type'] == 8:
                photos.append(photo)
        return photos

    def advertisement(self):
        """广告
        
        Feed流的广告有banner和list两个地方
        :return: 
        """
        ads = []
        for ad in self.data['data']['info']:
            if 'advertise' in ad:
                ads.append(ad)
        for ad in self.data['data']['list']:
            if 'advertise' in ad:
                ads.append(ad)
        return ads

# ######################################################################
#             以下为feed流功能点
# ######################################################################

    @staticmethod
    def request(page=1, ver=3.7):
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

    @staticmethod
    def article_remove(page=5, ver=3.7):
        """不感兴趣功能，可以在feed流删除该文章
        默认删除第五页，第一条数据
        :param page: 页数
        :param ver:版本号
        :return: json
        """

        article_id = Feed.request(page=page)['data']['list'][0]['id']
        request = Article.article_remove(hostname=ConfList['hostname'],
                                         uid=ConfList['uid'],
                                         accesstoken=ConfList['accesstoken'],
                                         ver=ver,
                                         id=article_id)
        return request
