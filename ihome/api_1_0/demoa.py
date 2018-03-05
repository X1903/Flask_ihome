# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from . import api
from ihome import db

import logging
from flask import current_app

@api.route('/index')
def index():
    # logging.error('')  # 错误级别
    # logging.warn('')  # 警告级别
    # logging.info('')  # 消息提示级别
    # logging.debug('')  # 调试级别

    current_app.logger.error("error info")
    current_app.logger.warn("warn info")
    current_app.logger.info("info info")
    current_app.logger.debug("debug info")
    return "index page"
