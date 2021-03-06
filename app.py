
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route('/check', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        number = request.form['number']
        data = {'name':name,"surname":surname,'number':number}
        return render_template('home.html', context=data)
    return render_template("index.html")   
        
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)