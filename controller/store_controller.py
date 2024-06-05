from app import app
# from model import *
from model.store_model import StoreModel
from flask import request,jsonify

store = [{"name": "My Store"}]


store_obj=StoreModel()

@app.get("/store")
def get_full_store():
    result = store_obj.get_full_store_details();
    return jsonify(result) if isinstance(result,dict) else result

@app.route("/store/create",methods=['POST'])
def create_store():
    result = store_obj.create_new_store(request.form);
    return jsonify(result) if isinstance(result,dict) else result

@app.put('/store/update/<id>')
def update_the_store(id):
    result = store_obj.update_store(request.form,id);
    return jsonify(result) if isinstance(result,dict) else result

@app.delete('/store/delete/<id>')
def delete_the_store(id):
    result = store_obj.delete_store(id);
    return jsonify(result) if isinstance(result,dict) else result

