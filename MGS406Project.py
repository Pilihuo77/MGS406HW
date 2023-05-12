from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


# create the reservations table
def create_table():
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="Restaurant")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reservations
                 (id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(50) NOT NULL,
                  email VARCHAR(50) NOT NULL,
                  phone VARCHAR(20) NOT NULL,
                  party_size INT NOT NULL,
                  reservation_date DATE NOT NULL,
                  reservation_time TIME NOT NULL);''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/information')
def information():
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="Restaurant")
    c = conn.cursor()
    c.execute('SELECT id, name, email, phone, party_size, reservation_date, reservation_time FROM reservations')
    reservations = c.fetchall()
    conn.close()

    # for item in reservations:
    #     print(item)
    # get the IP address from the request
    # ip_address = request.remote_addr

    # redirect to the information page with IP address included
    return render_template('information.html', reservations = reservations)



@app.route('/reservation', methods=['POST','GET'])
def reserve_table():
    # Get reservation information from the form
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    party_size = request.form['party_size']
    reservation_date = request.form['reservation_date']
    reservation_time = request.form['reservation_time']

    # Insert reservation into the database
    conn = sql.connect(host="localhost", user="root", password="lx1218", database="Restaurant")
    c = conn.cursor()
    c.execute('INSERT INTO reservations (name, email, phone, party_size, reservation_date, reservation_time) VALUES (%s, %s, %s, %s, %s, %s)',
              (name, email, phone, party_size, reservation_date, reservation_time))
    conn.commit()
    conn.close()

    return f'Thank you for reserving a table at Ying Restaurant!\n\nWe are pleased to confirm that your table has been successfully reserved for {reservation_date} at {reservation_time}. We look forward to welcoming you to our restaurant.'

    



if __name__ == "__main__":
    app.run(debug='True')
