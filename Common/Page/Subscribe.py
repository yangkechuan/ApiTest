# -*-coding:UTF-8-*-

from Lib.Article import Article
from Common.conf.configure import ConfList


class Subscribe(object):

    def __init__(self, data):
        self.data = data

    def star(self):
        """订阅明星列表
        
        :return: star list
        """
        if 'star' in self.data['data']:
            return self.data['data']['star']
        return None

    def label(self):
        """订阅内容
        
        :return: label list
        """
        if 'label' in self.data['data']:
            return self.data['data']['label']
        return None

    def list(self):
        """文章列表
        未登陆时为猜你喜欢，登陆后显示订阅的内容
        :return: list
        """
        return self.data['data']['list']

    def is_star_sub(self):
        """登录后需要有的字段
        
        :return: bool
        """
        return self.data['data']['isstarsub']

    @staticmethod
    def request(page=1, ver=3.7, islogin=0):
        request = Article.article_list_subscribe(uid=ConfList['uid'],
                                                 accesstoken=ConfList['accesstoken'],
                                                 ver=ver,
                                                 islogin=islogin,
                                                 page=page,
                                                 pf=ConfList['pf'])
        return request
