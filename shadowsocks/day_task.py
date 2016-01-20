#!/usr/bin/python
# -*- coding: UTF-8 -*-
from db import MySQL
import cymysql,time,datetime,calendar
def get_service(uid,types):
    conn = MySQL.db()
    today = time.strftime("%Y-%m-%d")
    cur = conn.cursor(cursor=cymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM t_user_service  where state=1 and uid=%s and service_type in %s and end_date>=%s order by end_date ASC limit 1",[uid,types,today])
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data
def run():
    conn = MySQL.db()
    cur = conn.cursor(cursor=cymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM user where switch=1 and enable=1")
    today = datetime.datetime.now()
    days = calendar.monthrange(today.year, today.month)[1]
    print days
    for user in cur.fetchall():
        service = get_service(user['uid'],[1,2])
        if user['service_type'] in [1,2] :
            if service :
                start_day = service['start_date'].day
                end_day = service['end_date'].day
                print end_day
        if user['service_type'] in [0,3] :
            print service and service['end_date'].day
    cur.close()
    conn.close()
if __name__ == '__main__':
    run()