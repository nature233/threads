# -*- coding=utf-8 -*-

import pymysql

class Mysql_Helper(object):
    """docstring for mysql"""

    def __init__(self,dbconfig):
        self.host =dbconfig['host']
        self.port =dbconfig['port']
        self.user =dbconfig['user']
        self.passwd =dbconfig['passwd']
        self.dbname =dbconfig['dbname']
        self.charset =dbconfig['charset']
        self._conn=None
        self._conn=self.get_con()
        self._currsor=self._conn.cursor()

    def get_con(self):
        try:
            conn = pymysql.connect(host=self.host,
                                         port=self.port,
                                         user=self.user,
                                         passwd=self.passwd,
                                         db=self.dbname,
                                         charset=self.charset)
            print('connnection successful')
            return conn
        except pymysql.Error:
            print('connection error',pymysql.Error)


    def select_all(self, sql):

       _list1=[]
       try:
            self._currsor.execute(sql)
            results = self._currsor.fetchall()
            for row in results:
                _list1.append(row)
            self._conn.commit()
            return _list1
       except pymysql.Error:

                    self._conn.rollback()
                    print("select error",pymysql.Error)


    def select(self, table, column='*', condition=''):

        condition = ' where ' + condition if condition else None
        if condition:
            sql = "select distinct %s from %s %s" % (column, table, condition)
        else:
            sql = "select distinct %s from %s" % (column, table)

        return self.select_all(sql)

    def insert(self, table, tdict):
        # try:
            column = ''
            value = ''
            for key in tdict:
                column += ',' + key
                value += "','" + tdict[key]
            column = column[1:]
            value = value[2:] + "'"
            sql = "insert into %s(%s) values(%s)" % (table, column, value)
            self._currsor.execute(sql)
            self._conn.commit()
            print('insert successful')
            return self._currsor.lastrowid  # 返回最后的id
        # except pymysql.Error:
        #     print('insert error:',pymysql.Error)
        #     self._conn.rollback()


    def update(self, table, tdict, condition=''):
        try:
            if not condition:
                print ("must have id")
                exit()
            else:
                condition = 'where ' + condition
            value = ''
            for key in tdict:
                value += ",%s='%s'" % (key, tdict[key])
            value = value[1:]
            sql = "update %s set %s %s" % (table, value, condition)
            self._currsor.execute(sql)
            self._conn.commit()
            return self._currsor.rowcount  # 返回受影响行数
        except pymysql.Error:
               print('pymysql error:', pymysql.Error)
               self._conn.rollback()

    def delete(self, table, condition=''):
        try:

            condition = 'where ' + condition if condition else None
            sql = "delete from %s %s" % (table, condition)
            # print sql
            self._currsor.execute(sql)
            self._conn.commit()
            return self._currsor.rowcount  # 返回受影响行数
        except pymysql.Error:
            print('pymysql error:', pymysql.Error)
    def close(self):
        try:
            self._currsor.close()
            self._conn.close()
        except:
            pass


if __name__ == '__main__':
    list2=[]

    dbconfig={'host':'127.0.0.1',
              'port':3306,
              'user':'root',
              'passwd':'123456',
              'dbname':'frameworkdb',
              'charset':'utf8'
              }
    db = Mysql_Helper(dbconfig)
    # lis2=db.select_all('select device_name from device_cabinet where testfile_name=%s()')
    a=input()
    sql='select * from cabinet limit 0,'+a
    list3=db.select_all(sql)

    print(list3)

    db.close()
