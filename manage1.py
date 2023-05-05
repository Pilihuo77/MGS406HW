from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql

app = Flask(__name__)

# create the employee table
def create_table():
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="MySQL")
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
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="MySQL")
    c = conn.cursor()
    c.execute('SELECT EmpID, EmpName, EmpGender, EmpPhone, EmpBdate FROM employee')
    employees = c.fetchall()
    conn.close()

    # get the IP address from the request
    ip_address = request.remote_addr

    # redirect to the information page with IP address included
    return redirect(url_for('show_information', ip_address=ip_address))

@app.route('/information/<ip_address>')
def show_information(ip_address):
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="MySQL")
    c = conn.cursor()
    c.execute('SELECT EmpID, EmpName, EmpGender, EmpPhone, EmpBdate FROM employee')
    employees = c.fetchall()
    conn.close()

    return render_template('information.html', employees=employees, ip_address=ip_address)


@app.route('/register', methods=['POST','GET'])
def register_employee():
    # Get employee information from the form
    EmpID = request.form['EmpID']
    EmpName = request.form['EmpName']
    EmpGender = request.form['EmpGender']
    EmpPhone = request.form['EmpPhone']
    EmpBdate = request.form['EmpBdate']

    # Insert employee into the database
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="MySQL")
    c = conn.cursor()
    c.execute('INSERT INTO employee (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES (%s, %s, %s, %s, %s)',
              (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate))
    conn.commit()
    conn.close()

    return 'Employee registered successfully!'


