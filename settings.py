# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 11:25
# File    : settings.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqllite://:memory:'


class ProductionConfig(BaseConfig):
    DATABASE_URI = 'mysql://user@production/foo'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = 'mysql://user@development/foo'


class TestingConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = 'mysql://user@test/foo'
