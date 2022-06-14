from flask import Flask, app,render_template,url_for,request
import pickle
import nltk
import re
from nltk.corpus import stopwords
import string
import pickle
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
stopword=set(stopwords.words('english'))

def cleaning(text):
    text = str(text).lower()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text

loaded_vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
loaded_model = pickle.load(open('final_model.sav', 'rb')) #reads the model

app=Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		feedback = request.form['message']
		#print(feedback)
		data = cleaning('I am stressed')
		data = loaded_vectorizer.transform([data]).toarray()
		output = loaded_model.predict(data)
		if output[0]==1:
			result='Stressed'
			return render_template('result.html',prediction = 0)
		else:
			result = 'Not Stressed'
			return render_template('result.html',prediction = 1)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/report')
def report():
    return render_template('report.html')

    	 	 
if __name__ == '__main__':
	app.run()
