from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from ip_form import IPForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacksick' #サンプルだよ！ちゃんと変えなさいね！
csrf = CSRFProtect(app)

@app.route("/", methods=["GET","POST"])
def index():
    form = IPForm()
    if form.validate_on_submit():
        ip_address = form.ip_address.data
        # TODO 処理書く
    return render_template('index.html', form=form)