from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'securekey'

# Dummy user data
users = {
    'john': {'password': '1234', 'security_q': 'blue', 'level3': 'pending'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user in users and users[user]['password'] == pwd:
            session['user'] = user
            return redirect('/level2')
        return "Invalid Login"
    return render_template('login.html')

@app.route('/level2', methods=['GET', 'POST'])
def level2():
    if 'user' not in session: return redirect('/')
    if request.method == 'POST':
        ans = request.form['security_q']
        if ans == users[session['user']]['security_q']:
            return redirect('/level3')
        return "Wrong answer"
    return render_template('level2.html')

@app.route('/level3', methods=['GET', 'POST'])
def level3():
    if 'user' not in session: return redirect('/')
    if request.method == 'POST':
        if request.form['approval'] == 'yes':
            return redirect('/success')
        return "Admin Denied"
    return render_template('level3.html')

@app.route('/success')
def success():
    if 'user' not in session: return redirect('/')
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
