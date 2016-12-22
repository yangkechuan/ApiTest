# -*-coding:UTF-8-*-

import requests
from Common.conf.configure import ConfList


class User(object):

    """
    判断用户是否是使用手机号注册过
    """
    @staticmethod
    def is_register(uid, accesstoken, mobile, ver, pf='android'):
        """
        user/is_register GET
        :param uid: 用户ID
        :param accesstoken: token
        :param mobile: 手机号
        :param ver: 版本号
        :param pf: 设备
        :return: json
        """
        params = {
            'uid': uid,
            'accesstoken': accesstoken,
            'mobile': mobile,
            'ver': ver,
            'pf': pf
        }
        try:
            request = requests.get(ConfList['hostname'] + '/user/is_register', params=params)
            return request.json()
        except Exception as e:
            raise e

    @staticmethod
    def login(uid, accesstoken, access_token, clientid, mobile, password, ver):
        """
        user/login POST
        :param uid: 用户ID
        :param accesstoken: token
        :param access_token: 登陆时的token
        :param clientid: 设备ID
        :param mobile: 手机号
        :param password: 密码
        :param ver: 版本号
        :return: json
        """
        data = {
            'uid': uid,
            'accesstoken': accesstoken,
            'access_token': access_token,
            'clientid': clientid,
            'mobile': mobile,
            'pass': password,
            'ver': ver
        }
        try:
            request = requests.post(ConfList['hostname'] + '/user/login', data=data)
            return request.json()
        except Exception as e:
            raise e
