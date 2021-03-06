# -*-coding:UTF-8-*-

import requests
from Common.conf.configure import ConfList


class Common(object):

    @staticmethod
    def common_setting(hostname, uid, accesstoken, ver, pf='android'):
        """
        common/setting GET
        :param uid:user id
        :param accesstoken: user token
        :param ver: version
        :param pf: android or ios
        :return: request
        """
        params = {
            'uid': uid,
            'accesstoken': accesstoken,
            'pf': pf,
            'ver': ver
        }
        try:
            request = requests.get(url=hostname + '/common/setting', params=params)
            return request.json()
        except Exception as e:
            pass

    @staticmethod
    def common_menu(hostname, uid, accesstoken, ver, pf='android'):
        """
        common/menu GET
        :param uid: user id
        :param accesstoken: user token
        :param ver: version
        :param pf: android or ios
        :return: request
        """
        params = {
            'uid': uid,
            'accesstoken': accesstoken,
            'pf': pf,
            'ver': ver
        }
        try:
            request = requests.get(url=hostname + '/common/menu', params=params)
            return request.json()
        except Exception as e:
            pass
