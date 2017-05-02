# -*-coding:UTF-8-*-

import requests
from Common.conf.configure import ConfList


class Comment(object):

    @staticmethod
    def comment_create(hostname, uid, accesstoken, aid, content, replyid, ver, pf='android'):
        """
        comment/create  POST
        :param uid: user id
        :param accesstoken: user token
        :param aid: article id
        :param content:  barrage content
        :param replyid: reply barrage id
        :param ver: version
        :param pf: android or ios
        :return: request
        """
        data = {
            'uid': uid,
            'accesstoken': accesstoken,
            'aid': aid,
            'content': content,
            'replyid': replyid,
            'ver': ver,
            'pf': pf
        }
        try:
            request = requests.post(url=hostname + '/comment/create', data=data)
            return request.json()
        except requests.RequestException as e:
            pass
