# -*- coding: UTF-8 -*-
import requests
from q01proxySpider import main
from q03saveDB import ProxyDB
import concurrent.futures


class TestProxy:
    def __init__(self):
        self.addSuccessProxy = ProxyDB()

    def testIp(self, proxy):
        proxies = {
            'http': 'http://' + proxy
        }
        try:
            result = requests.get('http://www.baidu.com', proxies=proxies, timeout=5)
        except requests.exceptions.ConnectTimeout:
            print('+++> 代理不能使用 <+++' + f'---| {proxy} |---')
        except requests.exceptions.ProxyError:
            print('+++> 代理不能使用 <+++' + f'---| {proxy} |---')
        except requests.exceptions.ReadTimeout:
            print('+++> 代理不能使用 <+++' + f'---| {proxy} |---')
        else:
            if result.reason == 'OK':
                print('===> 代理可以使用 <===' + f'***| {proxy} |***', result.reason)
                self.addSuccessProxy.addProxy(proxy)
                print(f'^^^  {proxy}保存到数据库  ^^^')

            else:
                print('+++> 代理不能使用 <+++' + f'---| {proxy} |---')

    def textAlready(self):
        allProxy = self.addSuccessProxy.testDBProxy()
        print(f'$$$ 数据库现有ip数量{len(allProxy)}个 $$$')
        for proxy in allProxy:
            proxies = {
                'http': 'http://' + proxy
            }
            try:
                result = requests.get('http://www.baidu.com', proxies=proxies, timeout=3)
            except requests.exceptions.ConnectTimeout:
                self.addSuccessProxy.AlterScore(proxy)
                print(f'^^^  {proxy} 此代理不可用 (减分操作) ^^^')
            except requests.exceptions.ProxyError:
                self.addSuccessProxy.AlterScore(proxy)
                print(f'^^^  {proxy} 此代理不可用 (减分操作) ^^^')
            except requests.exceptions.ReadTimeout:
                self.addSuccessProxy.AlterScore(proxy)
                print(f'^^^  {proxy} 此代理不可用 (减分操作) ^^^')
            except requests.exceptions.ChunkedEncodingError:
                self.addSuccessProxy.AlterScore(proxy)
                print(f'^^^  {proxy} 此代理不可用 (减分操作) ^^^')
            except requests.exceptions.ConnectionError:
                self.addSuccessProxy.AlterScore(proxy)
                print(f'^^^  {proxy} 此代理不可用 (减分操作) ^^^')
            except Exception as e:
                print(e)
            else:
                if result.reason == 'OK':
                    print(f'^^^  {proxy} 此代理还可用  ^^^', result.reason)
                else:
                    self.addSuccessProxy.AlterScore(proxy)
                    print(f'^^^  {proxy} 此代理不可用 (删除操作) ^^^')


if __name__ == '__main__':
    test = TestProxy()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exp:
    #     for proxy in main():
    #         exp.submit(test.testIp, proxy)
    test.textAlready()
