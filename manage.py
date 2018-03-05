# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from ihome import create_app


# 创建flask的应用对象
app = create_app('develop')


if __name__ == '__main__':
    app.run(debug=True)
