from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from itertools import chain
import yaml


app = Flask(__name__)
Bootstrap(app)

#Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    #cur.execute("INSERT INTO user VALUES(%s)",['Mike'])
    #mysql.connection.commit()   #saves the changes into db
    result_value = cur.execute("SELECT * FROM user")  #Returns the number of columbs of user and saves it into varialbe "result_value"
    if result_value > 0:
        #users = cur.fetchall()
        users = list(chain.from_iterable(cur.fetchall()))
        return users[0]
    return render_template('index.html')

    #fruits = ['Apple', 'Mango','Orange']
    #return render_template('index.html', fruits=fruits)
    #return redirect(url_for('about'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True)



#From index.html
# <!DOCTYPE html>
# <html>
#   <head>
#     <title>My Project</title>
#   </head>
#   <body>
#     <ul>
#       {% for fruit in fruits %}
#         <li>{{fruit}}</li>
#       {% endfor %}
#     </ul>
#     {% if 'Mango' in fruits %}
#       <p>Mango exists in the list</p>
#     {% else %}
#       <p>Mango Desn't exist in the list</p>
#     {% endif %}
#   </body>
# </html>
