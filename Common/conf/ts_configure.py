# -*-coding:UTF-8-*-


"""

    配置列表
    测试环境和线上环境

"""

from Common.conf.status import STATUS


if STATUS == 'test':

    ConfList = {
        'accetttoken': '64b32c9e41de2e59ef02f1bafd447208',
        'hostname': 'http://testapi.app.happyjuzi.com/explore',
        'uid': '4016430349851247',
        'pf': 'android',
        'content': 'juzi',
        'channel': 'juzi',
    }

if STATUS == 'prod':

    ConfList = {
        'clientid': '96b24bf126a71d2af56b0023d105cf08f675510d2656cbed25187c7610cbc1d3',
        'access_token': '238bdf2dcb06be52875afd77df7106a1',
        'accesstoken': '03479980758f45657d2aec3883ea2d94',
        'hostname': 'http://api.app.happyjuzi.com/explore',
        'mobile': 18611425451,
        'uid': '4055433308488339',
        'pf': 'android',
        'content': 'juzi',
        'channel': 'juzi',
        'pass': 123456,

    }
