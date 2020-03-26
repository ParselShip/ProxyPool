# -*- coding: UTF-8 -*-
import pymysql
import random
from setting import *


class ProxyDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host=HOST,
            port=3306,
            user=USER,
            passwd=PASSWORD,
            db=DB
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def addProxy(self, proxy):
        """向数据库添加成功proxy"""
        self.connection.ping()
        try:
            sql = 'insert into proxypool(`proxy`) value ("{proxy}")'.format(proxy=proxy)
            self.cursor.execute(sql)
            self.connection.commit()
        except pymysql.err.IntegrityError:
            print(f'~~~ 该代理ip已存在 ~~~')

    def testDBProxy(self):
        """查询所有proxy并交由测试模块测试 进行相应的加减分"""
        self.connection.ping()
        sql = 'select proxy from proxypool;'
        self.cursor.execute(sql)
        allProxy = [proxy[0] for proxy in self.cursor.fetchall()]
        return allProxy

    def AlterScore(self, proxy):
        """如果不能使用就删除该ip"""
        self.connection.ping()
        sql = 'delete from proxypool where proxy = \'%s\';' % proxy
        self.cursor.execute(sql)
        self.connection.commit()

    def returnProxy(self):
        """查询所有proxy并交由测试模块测试 进行相应的加减分"""
        self.connection.ping()
        count = random.randint(1, len(self.testDBProxy()) + 1)
        sql = 'select proxy,score from proxypool where id=%s;' % count
        self.cursor.execute(sql)
        proxy = self.cursor.fetchone()
        return proxy

    def getOneProxy(self):
        """随机获取一个代理返回到api"""
        wholeProxy = self.testDBProxy()
        Ip = random.choice(wholeProxy)
        return Ip


if __name__ == '__main__':
    a = ProxyDB()
    print(len(a.testDBProxy()))
