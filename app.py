import json
from flask_paginate import Pagination,get_page_parameter,request
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,static_folder="static",template_folder="templates")
import config
from model.UserModel import User,query,engine
        
    

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
            # "auto_increment_id": res.auto_increment_id,
            "segment_id": res.segment_id,
            "text": res.text,
            "entity": res.entity,
            "entity_kb": res.entity_kb,
            "data":res.data
            # "predicate": res.predicate,
            # "object":res.object
        }
        data_list.append(datas)
    info = {"code": 0, "message": "OK", "total": len(data_list), "data": data_list[(pageNum - 1) * pageSize:pageNum * pageSize]}
    # print(info)
    return info

@app.route('/data/add',methods=["POST"])
def addData():
    data=request.data.decode('utf-8')
    data= json.loads(data)
    # print(data)
    for item in data:
        val='('+item["auto_increment_id"]+','+item["segment_id"]+',"'+item['text']+'","'+item['entity']+'","'+item['entity_kb']+'","'+item['data']+'")'
        insert_sql= "insert into test(auto_increment_id, segment_id, text, entity,entity_kb,data) values{}".format(val)
        engine.execute(insert_sql)
        # user_db = User(item["auto_increment_id"],item["segment_id"],item['text'],item['entity'],item['entity_kb'],item['data'])
        # add(user_db)
    return render_template("index.html")

@app.route('/data/add1',methods=["POST"])
def addData1():
    # text_id=1&text=1&entity=1&entity_kb=1&data=1
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,)
    # db.create_all()