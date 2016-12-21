# -*-coding:UTF-8-*-

import os
import sendMail


class checkError:

    ErrorMsg = 'FAILURES'

    def checkLogFile(self):

        tag = False
        if os.path.exists('apiTest.log'):
            tag = True
        return tag

    def checkIsError(self):
        with open('apiTest.log') as f:
            if self.ErrorMsg in f.read():
                sendMail.sendmail()

if __name__ == '__main__':
    E = checkError()
    if E.checkLogFile():
        E.checkIsError()
