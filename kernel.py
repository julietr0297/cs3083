from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/loginpage', methods = ['POST', 'GET'])
def loginpage():
    if request.method == 'POST':
        user = request.form['nm']
        if user == None:
            return redirect(url_for('loginpage'))
        else:    
            return redirect(url_for('welcome', id_name = user))
            
    

@app.route('/welcome/<id_name>')
def welcome(id_name):
    return 'Welcome {}'.format(id_name)
    
if __name__ == '__main__':
    app.run()
