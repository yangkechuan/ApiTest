# -*-coding:UTF-8-*-

from Ver.ts_v1.ts_v1_conf import ts_v1conf
from Common.explore.Page.Feed import Feed


class Test_feed_v1(object):

    ver = ts_v1conf['ver']

    def test_banner(self):
        request = Feed.request(ver=self.ver)
        banner = Feed(request).banner()
        assert len(banner) >= 1
        for msg in banner:
            assert type(msg['id']) is int
            assert msg['urlroute'] != ''
            assert msg['title'] != ''
            assert msg['pic'] != ''
            assert msg['cat']['name'] != ''
            assert msg['cat']['pic'] != ''

