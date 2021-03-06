# -*-coding:UTF-8
import pymysql


class Db(object):
    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    db = 'laravel5'

    ErrorMsg = 'FAILURES'

    def __init__(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        self.conn.encoding = 'utf8'
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def check_status(self):
        with open('apiTest.log') as f:
            if self.ErrorMsg in f.read():
                return 0
            else:
                return 1

    def write_sql(self, content, status):
        sql = """
            INSERT INTO `api_log`(content, status, created_at, updated_at) VALUES (%s, %s, now(), now())
        """
        self.cur.execute(sql, (content, status))
        self.conn.commit()

if __name__ == '__main__':
    db = Db()
    content = ''
    with open('apiTest.log') as f:
        for line in f.readlines():
            line + "\n"
            content += line

    status = db.check_status()
    db.write_sql(content=content, status=status)
