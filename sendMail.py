#!/usr/bin/env python
# -*-coding:UTF-8


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common.conf.status import STATUS

_usr = "yangkechuan@happyjuzi.com"
_pwd = "xiaochuan.126"
_to = "yangkechuan@happyjuzi.com"
_cc = "ceshi@happyjuzi.com"
msg = MIMEMultipart()
msg["Subject"] = STATUS + "环境api自动化测试报警"
msg["From"] = _usr
msg["To"] = _to
msg['Cc'] = _cc
msg["Accept-Language"] = "zh-CN"
msg["Accept-Charset"] = "ISO-8859-1,utf-8"

'正文'

with open('report.html') as f:
    content = f.read()
part = MIMEText(content, 'html')
msg.attach(part)

'附件'
# part = MIMEApplication(open('apiTest.log','rb').read())
# part.add_header('Content-Disposition','attachment',filename = 'apiTest.log')
# msg.attach(part)


def sendmail():
    """
        端口默认25
    :return: void
    """
    s = smtplib.SMTP("smtp.exmail.qq.com", timeout=30)
    s.login(_usr, _pwd)
    s.sendmail(_usr, _to, msg.as_string())
    s.close()
