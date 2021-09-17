#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/17 14:13
# @Author : ma.fei
# @File : user.py.py
# @Software: PyCharm

import json
import tornado.web
from web.db import T_User
from web.utils import DateEncoder
from playhouse.shortcuts import model_to_dict

class user(tornado.web.RequestHandler):
    # 按姓名查询用户信息t_user表 name列
     def get(self):
         xm = self.get_argument("xm")
         rs = T_User.select().where(T_User.name.contains(xm))
         res = []
         for r in rs:
             res.append(model_to_dict(r))
         self.write(json.dumps(res ,cls=DateEncoder))

     def post(self):
        pass

     def put(self):
        pass

     def delete(self):
        pass