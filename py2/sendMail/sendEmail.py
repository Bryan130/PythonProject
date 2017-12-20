#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan.Lan
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@time: 2017/12/12 18:38
"""

import string
import smtplib
from email.mime.text import MIMEText


mailinfo = {
    "msg_from" : "244896035@qq.com",
    # "msg_to" : "alex.cao@vengasz.com,bryan.lan@vengasz.com",
    "msg_to" : "bryan.lan@vengasz.com",
    "hostname" : "stmp.qq.com",
    "username" : "244896035@qq.com",
    "password" : "azdygxlxfgeibhch",
    "mailsubject" : "Python发送邮件debug",
    "mailtext" : "正文内容",
    "mailencoding" : "utf-8"
}


def main(mailinfo):

    msg = MIMEText(mailinfo["mailtext"], "plain", mailinfo["mailencoding"])
    msg["Subject"] = mailinfo["mailsubject"]
    msg["From"] = mailinfo["msg_from"]
    msg["To"] = mailinfo["msg_to"]
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # s.set_debuglevel(1)
        s.login(mailinfo["msg_from"], mailinfo["password"])
        s.sendmail(mailinfo["msg_from"], mailinfo["msg_to"].split(","), msg.as_string())
        print("Send Success!")
    finally:
        s.quit()


if __name__ == "__main__":
    main(mailinfo)
