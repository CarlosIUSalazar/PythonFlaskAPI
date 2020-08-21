from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    fruits = ['Apple', 'Mango','Orange']
    return render_template('index.html', fruits=fruits)
    #return redirect(url_for('about'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)




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
