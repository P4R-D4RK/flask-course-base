from flask import Flask
from my_app.product.views import product


app = Flask(__name__)

#rest
from my_app.rest_api.product_api import product_view

#importar las vistas
app.register_blueprint(product)

#filter personalizado
@app.template_filter('mydouble')
def mydouble_filter(n:int):
    return n*2
