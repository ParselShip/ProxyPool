# -*- coding: UTF-8 -*-
from q01proxySpider import main
from q03saveDB import ProxyDB
from q02ipTest import TestProxy
import concurrent.futures


class Scheduler:
    def __init__(self):
        self.getNewProxy = main()
        self.db = ProxyDB()
        self.testProxy = TestProxy()

    def testAlready(self):
        print('正在测试已经存在的ip')
        while True:
            self.testProxy.textAlready()
            if len(sch.db.testDBProxy()) < 25:
                print('-*- 代理数量小于25 获取可用ip -*-')
                break

    def testNewProxy(self):
        newProxy = self.getNewProxy
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ext:
            for new in newProxy:
                ext.submit(self.testProxy.testIp, new)


if __name__ == '__main__':
    sch = Scheduler()
    while True:
        sch.testAlready()
        sch.testNewProxy()
