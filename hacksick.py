from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from ip_form import IPForm
from command_agent import CommandAgent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacksick' #サンプルだよ！ちゃんと変えなさいね！
csrf = CSRFProtect(app)

@app.route("/", methods=["GET","POST"])
def index():
    form = IPForm()
    output = ""
    error = ""
    if form.validate_on_submit():
        ip_address = form.ip_address.data
        output, error = CommandAgent.run_command("nmap -sV", ip_address)
    return render_template('index.html', form=form, output=output, error=error)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8949, debug=True)