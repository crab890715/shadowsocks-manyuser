#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Config,cymysql
class MySQL:
    instance = None
    @staticmethod    
    def get_instance(host=Config.MYSQL_HOST, port=Config.MYSQL_PORT, user=Config.MYSQL_USER,
                                   passwd=Config.MYSQL_PASS, db=Config.MYSQL_DB, charset='utf8'):
        if MySQL.instance is None:
            MySQL.instance = cymysql.connect(host=host, port=port, user=user,passwd=passwd, db=db, charset=charset)
        return MySQL.instance
    
if __name__ == '__main__':
    MySQL.get_instance()
    MySQL.get_instance().close()