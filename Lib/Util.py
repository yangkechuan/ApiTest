# -*-coding:UTF-8-*-

import hashlib


class Util(object):

    @staticmethod
    def md5_gen(uid):
        """
        :param uid: user id
        :return: token
        """
        return hashlib.md5((str(uid) + "oY*JpRsF@kj0qig7").encode("utf-8")).hexdigest()

    @staticmethod
    def comment_md5_gen(uid, aid, content, replyid=''):
        """
        :param uid:user id
        :param aid: article id
        :param content: barrage content
        :param replyid: reply barrage id ,default empty
        :return:
        """
        return hashlib.md5(
            (str(uid) + str(aid) + str(content) + str(replyid) + "oY*JpRsF@kj0qig7").encode("utf-8")).hexdigest()
