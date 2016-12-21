# -*-coding:UTF-8-*-


import requests
from Common.conf.configure import ConfList


class Article(object):

    @staticmethod
    def article_list_home(uid, accesstoken, page, channel, ver, pf='android'):
        """
        article/list/home GET
        :param uid: user id
        :param accesstoken: token
        :param ver: version
        :param channel: not required
        :param page: not required
        :param pf: android or ios
        :return: request
        """

        params = {
            'pf': pf,
            'uid': uid,
            'ver': ver,
            'page': page,
            'channel': channel,
            'accesstoken': accesstoken
        }
        try:
            request = requests.get(ConfList['hostname'] + '/article/list/home', params=params)
            return request.json()
        except Exception as e:
            raise e

    @staticmethod
    def article_list_subscribe(uid, accesstoken, ver, islogin=0, page=1, channel='', pf='android'):
        """
        article/list/subscribe GET
        :param uid: user id
        :param accesstoken: token
        :param islogin: 1 or 0
        :param ver: version
        :param page: default 1
        :param channel: not required
        :param pf: android or ios
        :return: request
        """

        params = {
            'uid': uid,
            'accesstoken': accesstoken,
            'islogin': islogin,
            'ver': ver,
            'page': page,
            'channel': channel,
            'pf': pf
        }
        try:
            request = requests.get(ConfList['hostname'] + '/article/list/subscribe', params=params)
            return request.json()
        except Exception as e:
            raise e

    @staticmethod
    def article_remove(uid, accesstoken, id, ver, pf='android'):
        """
        article/remove POST
        :param uid: 用户ID
        :param accesstoken: token
        :param id: 文章ID
        :param ver: 版本
        :param pf: 设备
        :return:
        """
        data = {
            'uid': uid,
            'accesstoken': accesstoken,
            'id': id,
            'ver': ver,
            'pf': pf
        }
        try:
            request = requests.post(ConfList['hostname'] + '/article/remove', data=data)
            return request.json()
        except Exception as e:
            raise e

