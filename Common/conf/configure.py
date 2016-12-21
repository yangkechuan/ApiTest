# -*-coding:UTF-8-*-


"""

    配置列表
    测试环境和线上环境

"""

from Common.conf.status import STATUS


if STATUS == 'test':

    ConfList = {
        'accetttoken': '64b32c9e41de2e59ef02f1bafd447208',
        'hostname': 'http://testapi.app.happyjuzi.com',
        'uid': '4016430349851247',
        'pf': 'android',
        'content': 'juzi',
        'channel': 'juzi',
    }

if STATUS == 'prod':

    ConfList = {
        'accesstoken': 'd9c29080f4d6681a35d0ebd93a9242f0',
        'hostname': 'http://api.app.happyjuzi.com',
        'uid': '3884832497361059',
        'pf': 'android',
        'content': 'juzi',
        'channel': 'juzi',
    }
