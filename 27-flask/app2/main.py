# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') 
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = 'My Flask App'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = 'My Flask App'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Post'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        return redirect(url_for('detail'))
   
if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)