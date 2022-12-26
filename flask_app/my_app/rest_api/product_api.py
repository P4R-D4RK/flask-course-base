from flask.views import MethodView
from flask import request
from my_app.product.model.products import PRODUCTS
from my_app.rest_api.helper.request import sendResJson
from my_app import app
import json

class ProductApi(MethodView):
    def get(self, id=None):

        if id:
            product = PRODUCTS.get(id)
            res = productToJson(id,product)

        else:
            res = []
            for p in PRODUCTS:
                res.append(productToJson(p,PRODUCTS[p]))
        
        return sendResJson(res,None,200)
    
    
    def post(self):

        if not request.form:
            return sendResJson(None,'Sin parámetros',403)
        
        #validaciones nombre
        if not 'name' in request.form:
            return sendResJson(None,'Sin parámetro nombre',403)

        if len(request.form['name']) < 3:
            return sendResJson(None,'Nombre no válido',403)
        
        #validaciones precio
        if not 'price' in request.form:
            return sendResJson(None,'Sin parámetro precio',403)
        
        try:
            float(request.form['price'])
        except ValueError:
            return sendResJson(None,'Precio no válido',403)
        
        #validaciones categoria
        if not 'category' in request.form:
            return sendResJson(None,'Sin parámetro categoría',403)
        
        if len(request.form['category']) < 3:
            return sendResJson(None,'Categoría no válida',403)

        i = list(PRODUCTS.keys())[-1] + 1
        PRODUCTS[i] = {
            'name': request.form['name'], 
            'category': request.form['category'], 
            'price': request.form['price'], 
            }
 
        return sendResJson(productToJson(i,PRODUCTS[i]),None,200)
    
    def put(self,id):
        product = PRODUCTS.get(id)
        if not product:
            return sendResJson(None,'Producto no existe',403)
        
        if not request.form:
            return sendResJson(None,'Sin parámetros',403)
        
        #validaciones nombre
        if not 'name' in request.form:
            return sendResJson(None,'Sin parámetro nombre',403)

        if len(request.form['name']) < 3:
            return sendResJson(None,'Nombre no válido',403)
        
        #validaciones precio
        if not 'price' in request.form:
            return sendResJson(None,'Sin parámetro precio',403)
        
        try:
            float(request.form['price'])
        except ValueError:
            return sendResJson(None,'Precio no válido',403)
        
        #validaciones categoria
        if not 'category' in request.form:
            return sendResJson(None,'Sin parámetro categoría',403)
        
        if len(request.form['category']) < 3:
            return sendResJson(None,'Categoría no válida',403)

        PRODUCTS[id] = {
            'name': request.form['name'], 
            'category': request.form['category'], 
            'price': request.form['price'], 
            }
 
        return sendResJson(productToJson(id,PRODUCTS[id]),None,200)
    
    def delete(self,id):
        product = PRODUCTS.get(id)
        if not product:
            return sendResJson(None,'Producto no existe',403)

        del PRODUCTS[id]
        return sendResJson('Producto eliminado!',None,200)

def productToJson(id_prod,product):
    return {
        'id': id_prod,
        'name': product['name'],
        'category': product['category'],
        'price': product['price']
    }

product_view = ProductApi.as_view('product_view')
app.add_url_rule('/api/products/',view_func=product_view,methods=['GET','POST'])
app.add_url_rule('/api/products/<int:id>',view_func=product_view,methods=['GET','DELETE','PUT'])