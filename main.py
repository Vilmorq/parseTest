from flask import Flask, request
from dateutil.parser import parse
# local
from utils import check_form, create_form

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form_data():
    return check_form(request.form)


@app.route('/create_form', methods=['POST'])
def create_form_data():
    return create_form(request.get_json(force=True))


if __name__ == '__main__':
    app.run()
