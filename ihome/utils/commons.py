# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import functools
from werkzeug.routing import BaseConverter
from flask import jsonify, session, g
from ihome.utils.response_code import RET

# 定义正则转换器
class ReConverter(BaseConverter):
    ''' '''

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex


def login_required(f):
    """要求用户登录的验证装饰器"""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # 从session数据中获取user_id
        user_id = session.get("user_id")
        if user_id is None:
            # 如果session中不存在user_id，表示用户未登录
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")
        else:
            # 表示用户已登录，将可能用到的user_id用户编号保存到g中，供视图函数使用
            g.user_id = user_id
            return f(*args, **kwargs)
    return wrapper