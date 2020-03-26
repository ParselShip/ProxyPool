# -*- coding: UTF-8 -*-
import time
import requests
import parsel
import faker
import concurrent.futures


class GetProxies:
    def __init__(self):
        self.fake = faker.Faker()
        self.selector = parsel.Selector
        self.AllProxy = []

    def quick_proxy(self):
        """快代理获取"""
        print('~~~ 开始爬取快代理 ~~~')
        headers = {
            'Host': 'www.kuaidaili.com',
            'Referer': 'https://www.kuaidaili.com/free/inha/2/',
            'User-Agent': self.fake.user_agent()
        }
        for page in range(1, 16):
            resp = requests.get(f'https://www.kuaidaili.com/free/inha/{page}/', headers=headers)
            # resp = requests.get('https://www.kuaidaili.com/free/inha/2/', headers=headers)
            quickSel = self.selector(resp.text)
            quickProxy_ip = quickSel.xpath('//td[@data-title="IP"]/text()').getall()
            quickProxy_port = quickSel.xpath('//td[@data-title="PORT"]/text()').getall()
            quickProxy = dict(zip(quickProxy_ip, quickProxy_port))
            quickProxy = [f'{key}:{values}' for key, values in quickProxy.items()]
            self.AllProxy.extend(quickProxy)
            time.sleep(1)

    def EN_proxy(self):
        """89代理获取"""
        print('~~~ 开始爬取89代理 ~~~')
        headers = {
            'Host': 'www.89ip.cn',
            'User-Agent': self.fake.user_agent()
        }
        for page in range(1, 16):
            resp = requests.get(f'http://www.89ip.cn/index_{page}.html', headers=headers)
            EnSel = self.selector(resp.text)
            EnProxy_ip = EnSel.xpath('//td[1]/text()').getall()
            EnProxy_port = EnSel.xpath('////td[2]/text()').getall()
            EnProxy = dict(zip(EnProxy_ip, EnProxy_port))
            EnProxy = [f'{key.strip()}:{values.strip()}' for key, values in EnProxy.items()]
            self.AllProxy.extend(EnProxy)
            time.sleep(1)

    def XC_proxy(self):
        """西刺代理获取"""
        print('~~~ 开始爬取西刺代理 ~~~')
        headers = {
            'Host': 'www.xicidaili.com',
            'Referer': 'https: // www.xicidaili.com / nn /',
            'User-Agent': self.fake.user_agent()
        }
        for page in range(1, 11):
            resp = requests.get(f'https://www.xicidaili.com/nn/{page}', headers=headers)
            XcSel = self.selector(resp.text)
            XcProxy_ip = XcSel.xpath('//tr/td[2]/text()').getall()
            XcProxy_port = XcSel.xpath('//tr/td[3]/text()').getall()
            XcProxy = dict(zip(XcProxy_ip, XcProxy_port))
            XcProxy = [f'{key.strip()}:{values.strip()}' for key, values in XcProxy.items()]
            self.AllProxy.extend(XcProxy)
            time.sleep(1)

    def TO_proxy(self):
        """三一代理"""
        print('~~~ 开始爬取三一代理 ~~~')
        headers = {
            'Host': '31f.cn',
            'User-Agent': self.fake.user_agent()
        }
        resp = requests.get('http://31f.cn/', headers=headers)
        ToSel = self.selector(resp.text)
        ToProxy_ip = ToSel.xpath('//tr/td[2]/text()').getall()
        ToProxy_port = ToSel.xpath('//tr/td[3]/text()').getall()
        ToProxy = dict(zip(ToProxy_ip, ToProxy_port))
        ToProxy = [f'{key.strip()}:{values.strip()}' for key, values in ToProxy.items()]
        self.AllProxy.extend(ToProxy)
        time.sleep(1)


def main():
    """利用多线程爬取代理"""
    one = GetProxies()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ext:
        ext.submit(one.quick_proxy)
        ext.submit(one.EN_proxy)
        ext.submit(one.XC_proxy)
        ext.submit(one.TO_proxy)
    return one.AllProxy
