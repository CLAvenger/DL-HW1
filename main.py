from flask import Flask,render_template,request
from utils import *
app = Flask(__name__,static_url_path='', static_folder='templates')
ele=element()

def convert_K2C(value): 
    # Convert Kelvin  to Celsius temperature 
    return "{:.5g}".format(float(value)-273.15)

def convert_K2F(value):
    # Convert  Kelvin to Fahrenheit temperature
    return "{:.5g}".format((float(value)-273.15)*9/5+32)
app.jinja_env.filters['convert_K2C']=convert_K2C
app.jinja_env.filters['convert_K2F']=convert_K2F

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        ele.get_data(symbol)
        if not ele.prop:
            return render_template('index.html',error="没有这个元素")
        return render_template('index.html',prop=ele.prop,compounds=ele.compounds)
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run()