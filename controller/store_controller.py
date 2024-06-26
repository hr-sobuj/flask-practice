from app import app
# from model import *
from model.store_model import StoreModel
from flask import request,jsonify,make_response


store = [{"name": "My Store"}]


store_obj=StoreModel()

@app.get("/store")
def get_full_store_controller():
    result = store_obj.get_full_store_details();
    return make_response({'data':jsonify(result) if isinstance(result,dict) else result},200)

@app.route("/store/create",methods=['POST'])
def create_store_controller():
    result = store_obj.create_new_store(request.form);
    return jsonify(result) if isinstance(result,dict) else result

@app.put('/store/update/<id>')
def update_the_store_controller(id):
    result = store_obj.update_store(request.form,id);
    return jsonify(result) if isinstance(result,dict) else result

@app.delete('/store/delete/<id>')
def delete_the_store_controller(id):
    result = store_obj.delete_store(id);
    return jsonify(result) if isinstance(result,dict) else result

@app.patch('/store/patch/<id>')
def patch_the_store_controller(id):
    return store_obj.patch_score(request.form, id)

@app.get('/store/pages/<page_no>')
def store_pagination_controller(page_no):
    return store_obj.pagination_model(page_no);

