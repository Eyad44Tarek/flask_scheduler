from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/')
def home():
    return render_template('schedule.html', appointments=appointments)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        client_name = request.form['client_name']
        pet_name = request.form['pet_name']
        date = request.form['date']
        reason = request.form['reason']
        appointments.append({'client_name': client_name, 'pet_name': pet_name, 'date': date, 'reason': reason})
        return redirect(url_for('home'))
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=True)

