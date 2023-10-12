from flask import Flask,render_template,request
app = Flask(__name__,static_url_path='', static_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    symbol=''
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        print(symbol)
    return render_template('index.html',symbol=symbol)

if __name__ == '__main__':
    app.debug=True
    app.run()