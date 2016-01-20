#!/usr/bin/python
# -*- coding: UTF-8 -*-
from db import MySQL
import cymysql
def service(uid,type):
    conn = MySQL.db()
    cur = conn.cursor(cursor=cymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM t_user_service  where state=1 and uid=%s and service_type=%s",[uid,type])
    data = cur.fetchone()
    cur.close()
    conn.close()
    pass
def run():
    conn = MySQL.db()
    cur = conn.cursor(cursor=cymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM user where switch=1 and enable=1")
    for user in cur.fetchall():
        service(user['uid'],user['service_type'])
        pass
    cur.close()
    conn.close()
if __name__ == '__main__':
    run()