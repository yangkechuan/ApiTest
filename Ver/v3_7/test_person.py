# -*-coding:UTF-8-*-
from Ver.v3_7.v3_7conf import v3_7conf
from Common.Page.Person import Person


class Test_person_v3_7(object):

    ver = v3_7conf['ver']

    def test_login(self):

        request = Person.login(ver=self.ver)
        assert request['code'] == 1
        assert request['msg'] == '操作成功'
        assert request['data']['id'] != ''
        assert request['data']['avatar'] != ''
        assert request['data']['name'] != ''
        assert type(request['data']['is_init_sub']) is bool
