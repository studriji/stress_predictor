from flask import Flask, app,render_template,url_for,request
import pickle

app=Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	return render_template('result.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/report')
def report():
    return render_template('report.html')

    	 	 
if __name__ == '__main__':
	app.run(debug=True)