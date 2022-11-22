import json
from flask_paginate import Pagination,get_page_parameter,request
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,static_folder="static",template_folder="templates")
import config
from model.UserModel import User,query
        
    

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/list')
def ShowData():
    pageNum = int(request.args.get("pageNum"))
    pageSize = int(request.args.get("pageSize"))
    data_list = []
    all = query()
    for res in all:
        datas = {
            "auto_increment_id": res.auto_increment_id,
            "segment_id": res.segment_id,
            "text": res.text,
            "entity": res.entity,
            "entity_kb": res.entity_kb,
            "data": res.data
        }
        data_list.append(datas)
    info = {"code": 0, "message": "OK", "total": len(data_list), "data": data_list[(pageNum - 1) * pageSize:pageNum * pageSize]}
    print(info)
    return info


if __name__ == '__main__':
    app.run(debug=True,)
    # db.create_all()