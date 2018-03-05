# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from flask import Blueprint

# 创建蓝图对象
api = Blueprint('API_1_0', __name__)


# 导入老土的试图
from . import demoa