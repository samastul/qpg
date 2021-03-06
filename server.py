from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('./home.html')


@app.route('/login', methods=['GET'])
def index():
    return render_template('./login.html')


# @app.route('/pdf', methods=['GET'])
# def index():
#     return render_template('./login.html')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
