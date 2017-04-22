# -*-coding:UTF-8-*-


from Common.Page.Feed import Feed
from Ver.v3_7.v3_7conf import v3_7conf


class Test_feed_v3_7(object):

    ver = v3_7conf['ver']

    def test_banner(self):
        request = Feed.request(ver=self.ver)
        banner = Feed(request).banner()
        assert len(banner) >= 1
        for msg in banner:
            assert type(msg['id']) is int
            assert msg['readnum'] >= 0
            assert msg['replynum'] >= 0
            assert msg['urlroute'] != ''
            assert msg['title'] != ''
            assert msg['pic'] != ''

    def test_topic_recommend(self):
        request = Feed.request(ver=self.ver)
        topic = Feed(request).topic_recommend()
        if topic is not None:
            assert isinstance(topic['id'], int)
            assert topic['urlroute'] != ''
            assert topic['title'] != ''
            assert topic['pic'] != ''
            assert topic['artnum'] == len(topic['article'])
            for article in topic['article']:
                assert isinstance(article['id'], int)
                assert article['title'] != ''
                assert article['pic'] != ''
                assert article['urlroute'] != ''

    def test_operation(self):
        request = Feed.request(ver=self.ver)
        operation = Feed(request).operation()
        if operation is not None:
            assert operation['type'] == 9
            assert operation['flag'] == 4
            assert operation['operation']['op'] != ''

    def test_gif(self):
        """
            gif在第二页才出现
        :return:
        """
        request = Feed.request(page=2, ver=self.ver)
        gif = Feed(request).gif()
        if gif is not None:
            assert type(gif['id']) is int
            assert gif['title'] != ''
            assert gif['shareurl'] != ''
            assert gif['type'] == 1
            assert gif['gif'][0]['mp4'] != ''
            assert gif['gif'][0]['pic'] != ''
            assert gif['gif'][0]['url'] != ''
            assert gif['gif'][0]['thumb'] != ''
            assert gif['gif'][0]['thumb_jpg'] != ''
            assert gif['readnum'] >= 0
            assert gif['replynum'] >= 0
            assert gif['display'] == 0

    def test_photo(self):
        request = Feed.request(ver=self.ver)
        photos = Feed(request).photo_gallary()
        if len(photos) >= 1:
            for photo in photos:
                assert photo['type'] == 8
                assert photo['readnum'] >= 0
                assert photo['replynum'] >= 0
                assert photo['urlroute'] != ''
                assert photo['title'] != ''
                assert photo['pic'] != ''
                assert photo['cat']['name'] != ''
                assert photo['cat']['icon'] != ''
                assert len(photo['contents']) >= 1
                for img in photo['contents']:
                    assert img['img'] != ''

    def test_ad(self):
        request = Feed.request(ver=self.ver)
        ads = Feed(request).advertisement()
        if len(ads) >= 1:
            for ad in ads:
                assert ad['advertise'] is True
                assert isinstance(ad['id'], int)
                assert ad['title'] != ''
                assert isinstance(ad['urlroute'], str)
                assert ad['pic'] != ''

    def test_article_remove(self):
        result = Feed.article_remove(page=5, ver=self.ver)
        assert result['code'] == 1
        assert result['msg'] == '操作成功'
