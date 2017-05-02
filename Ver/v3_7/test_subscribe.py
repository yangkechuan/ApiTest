# -*-coding:UTF-8-*-

from Ver.v3_7.v3_7conf import v3_7conf
from Common.Page.Subscribe import Subscribe


class Test_subscribe_v3_7(object):

    ver = v3_7conf['ver']

    def test_star_no_login(self):
        """未登录下的明星状态
        
        :return: 
        """
        request = Subscribe.request(islogin=0, ver=self.ver)
        stars = Subscribe(request).star()
        if stars is not None:
            for star in stars:
                assert star['id'] != ''
                assert star['name'] != ''
                assert star['portrait'] != ''
                assert star['praise'] >= 0
                assert star['praised_num'] >= 0
                assert star['issub'] is False

    def test_label_no_login(self):
        """未登录下的订阅
        
        :return: 
        """
        request = Subscribe.request(islogin=0, ver=self.ver)
        labels = Subscribe(request).label()
        if labels is not None:
            for label in labels:
                assert label['name'] != ''
                assert isinstance(label['id'], int)
                assert label['pic'] != ''
                assert label['urlroute'] != ''
                assert label['issub'] is False

    def test_is_star_sub(self):
        """登录后需要有isstarsub这个字段
        
        :return: 
        """
        request = Subscribe.request(islogin=1, ver=self.ver)
        is_star_sub = Subscribe(request).is_star_sub()
        assert isinstance(is_star_sub, bool)
