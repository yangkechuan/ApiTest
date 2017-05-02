# -*-coding:UTF-8-*-
from Lib.User import User
from Common.conf.configure import ConfList


class Person(object):

    def __init__(self, data):
        self.data = data

    @staticmethod
    def login(ver=3.7):
        """用户登录信息
        :param ver: 版本号
        :return: json
        """
        request = User.login(hostname=ConfList['hostname'],
                             uid=ConfList['uid'],
                             accesstoken=ConfList['accesstoken'],
                             access_token=ConfList['access_token'],
                             clientid=ConfList['clientid'],
                             mobile=ConfList['mobile'],
                             password=ConfList['pass'],
                             ver=ver)
        return request


