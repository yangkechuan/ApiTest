# -*-coding:UTF-8-*-
from Lib.User import User
from Common.conf.configure import ConfList


class Person(object):

    def __init__(self, data):
        self.data = data

    """
    用户登录信息
    """
    @staticmethod
    def login(ver=3.7):
        request = User.login(uid=ConfList['uid'],
                             accesstoken=ConfList['accesstoken'],
                             access_token=ConfList['access_token'],
                             clientid=ConfList['clientid'],
                             mobile=ConfList['mobile'],
                             password=ConfList['pass'],
                             ver=ver)
        return request


