from flask import Flask,render_template,request
from utils import *
app = Flask(__name__,static_url_path='', static_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        prop,compounds=get_data(symbol)
        if not prop:
            return render_template('index.html',error="没有这个元素")
        return render_template('index.html',prop=prop,compounds=compounds)
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run()