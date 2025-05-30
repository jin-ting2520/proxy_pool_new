# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     configHandler
   Description :
   Author :        JHao
   date：          2020/6/22
-------------------------------------------------
   Change Activity:
                   2020/6/22:
-------------------------------------------------
"""
__author__ = 'JHao'

import os, inspect
import setting
from util.singleton import Singleton
from util.lazyProperty import LazyProperty
from util.six import withMetaclass


class ConfigHandler(withMetaclass(Singleton)):

    def __init__(self):
        pass

    @LazyProperty
    def serverHost(self):
        return os.environ.get("HOST", setting.HOST)

    @LazyProperty
    def serverPort(self):
        return os.environ.get("PORT", setting.PORT)

    @LazyProperty
    def dbConn(self):
        return os.getenv("DB_CONN", setting.DB_CONN)

    @LazyProperty
    def tableName(self):
        return os.getenv("TABLE_NAME", setting.TABLE_NAME)

    @LazyProperty
    def fetchers(self):
        from fetcher.proxyFetcher import ProxyFetcher
        return [
            method for method in dir(ProxyFetcher)
            if callable(getattr(ProxyFetcher, method))
               and not method.startswith("__")
        ]


    @LazyProperty
    def httpUrl(self):
        return os.getenv("HTTP_URL", setting.HTTP_URL)

    @LazyProperty
    def httpsUrl(self):
        return os.getenv("HTTPS_URL", setting.HTTPS_URL)

    @LazyProperty
    def verifyTimeout(self):
        return int(os.getenv("VERIFY_TIMEOUT", setting.VERIFY_TIMEOUT))

    # @LazyProperty
    # def proxyCheckCount(self):
    #     return int(os.getenv("PROXY_CHECK_COUNT", setting.PROXY_CHECK_COUNT))

    @LazyProperty
    def maxFailCount(self):
        return int(os.getenv("MAX_FAIL_COUNT", setting.MAX_FAIL_COUNT))

    # @LazyProperty
    # def maxFailRate(self):
    #     return int(os.getenv("MAX_FAIL_RATE", setting.MAX_FAIL_RATE))

    @LazyProperty
    def poolSizeMin(self):
        return int(os.getenv("POOL_SIZE_MIN", setting.POOL_SIZE_MIN))

    @LazyProperty
    def proxyRegion(self):
        return bool(os.getenv("PROXY_REGION", setting.PROXY_REGION))

    @LazyProperty
    def timezone(self):
        return os.getenv("TIMEZONE", setting.TIMEZONE)

    @LazyProperty
    def useProxy(self):
        return os.getenv("USE_PROXY", setting.USE_PROXY)

    @LazyProperty
    def proxies(self):
        return os.getenv("PROXIES", setting.PROXIES)

    @LazyProperty
    def inputLogFile(self):
        return os.getenv("INPUT_LOG_FILE", setting.INPUT_LOG_FILE)

    @LazyProperty
    def logFileSaveDate(self):
        return os.getenv("LOG_FILE_SAVE_DATE", setting.LOG_FILE_SAVE_DATE)

    @LazyProperty
    def fetchInterval(self):
        return os.getenv("FETCH_INTERVAL", setting.FETCH_INTERVAL)

    @LazyProperty
    def workersNumber(self):
        return os.getenv("WORKERS_NUMBER", setting.WORKERS_NUMBER)

if __name__ == '__main__':
    config = ConfigHandler()
    print(config.fetchers)