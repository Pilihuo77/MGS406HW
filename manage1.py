from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# create the employee table
def create_table():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employee
                 (EmpID INT PRIMARY KEY NOT NULL,
                  EmpName TEXT NOT NULL,
                  EmpGender TEXT,
                  EmpPhone TEXT,
                  EmpBdate TEXT);''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/information')
def information():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('SELECT EmpID, EmpName, EmpGender, EmpPhone, EmpBdate FROM employee')
    employees = c.fetchall()
    conn.close()
    return render_template('information.html', employees=employees)


@app.route('/register', methods=['POST','GET'])
def register_employee():
    # Get employee information from the form
    EmpID = request.form['EmpID']
    EmpName = request.form['EmpName']
    EmpGender = request.form['EmpGender']
    EmpPhone = request.form['EmpPhone']
    EmpBdate = request.form['EmpBdate']

    # Insert employee into the database
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('INSERT INTO employee (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES (?, ?, ?, ?, ?)',
              (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate))
    conn.commit()
    conn.close()

    return 'Employee registered successfully!'

if __name__ == '__main__':
    app.run(debug=True)
