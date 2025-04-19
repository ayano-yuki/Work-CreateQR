from flask import Flask, render_template, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'qr_history' not in session:
        session['qr_history'] = []

    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            qr_url = f"http://api.qrserver.com/v1/create-qr-code/?data={data}&size=200x200"
            new_entry = {'url': qr_url, 'text': data}
            session['qr_history'] = [new_entry] + session['qr_history']
            session.modified = True
        return redirect(url_for('index'))

    return render_template('index.html', history=session.get('qr_history', []))

@app.route('/clear', methods=['POST'])
def clear_session():
    session.clear()
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=True)
