from flask import Flask, render_template, request, redirect, url_for, jsonify, session

app = Flask(__name__)
app.secret_key = 'secret'

# Simulated database
users = {'test@kennct.io': 'Qwerty@1234'}
patients = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['user'] = username
        return redirect(url_for('home'))
    else:
        return "Invalid credentials. Try again."

@app.route('/home')
def home():
    if 'user' not in session:
         return redirect(url_for('index'))
    return render_template('home.html')

# @app.route('/patients', methods=['GET', 'POST'])
# def add_patient():
#     if request.method == 'POST':
#         name = request.form['name']
#         test_name = request.form['test_name']
#         cost = request.form['cost']
#         patients.append({'name': name, 'test_name': test_name, 'cost': cost})
#         return redirect(url_for('home'))
    
#     return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_new_patient():
    return "Add Patient Page"

@app.route('/patients', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        test_name = request.form['test_name']
        cost = int(request.form['cost'])  # Convert cost to integer
        patients.append({'name': name, 'test_name': test_name, 'cost': cost})
        return redirect(url_for('home'))

    return render_template('patients.html', patients=patients)

@app.route('/cost_calculator', methods=['GET'])
def cost_calculator():
    total_cost = sum(int(p['cost']) for p in patients)
    return jsonify({'total_cost': total_cost})

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Flask app is running...")
    app.run(debug=True,port=8080)