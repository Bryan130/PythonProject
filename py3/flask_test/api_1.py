#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan.Lan
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@time: 2017/11/28 15:18
"""
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    "1":{
        "title":"game",
        "content":"play game"
    },
    "2":{
        "title":"run",
        "content":"run now"
    }
}

def abort_if_post_doesnot_exist(todo_id):
    try:
        todo_id = str(todo_id)
        TODOS[todo_id]
    except IndexError:
        abort(404, message="TODO doesn't exist")


parser = reqparse.RequestParser()
parser.add_argument("post", type=int)


class Todo(Resource):
    def get(self, todo_id):
        abort_if_post_doesnot_exist(todo_id)
        return TODOS[todo_id]

    def delete(self):
        pass

    def put(self):
        pass


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        json_data = request.get_json(force=True)
        todo_id = int(TODOS)
        return "bryan"


api.add_resource(Todo, '/todo/<todo_id>')
api.add_resource(TodoList, '/todos')


if __name__ == '__main__':
    app.run(debug=True)
