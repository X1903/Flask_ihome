# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from ihome import create_app, db
from  flask_script import Manager
from flask_migrate import MigrateCommand, Migrate


# 创建flask的应用对象
app = create_app('develop')


# 数据库迁移
manger = Manager(app)
Migrate(app, db)
manger.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # app.run(debug=True)
    manger.run()


    # 生成数据库
    # python2 manage.py db init

    # 初始化
    # python2 manage.py db migrate -m 'init tables'

    # 升级数据库
    # python2 manage.py db upgrade