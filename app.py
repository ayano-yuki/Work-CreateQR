from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_url = None
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            qr_url = f"http://api.qrserver.com/v1/create-qr-code/?data={data}&size=200x200"
    return render_template('index.html', qr_url=qr_url)

if __name__ == '__main__':
    app.run(debug=True)