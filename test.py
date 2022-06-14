import nltk
import re
from nltk.corpus import stopwords
import string
import pickle
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()

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

loaded_model = pickle.load(open('final_model.sav', 'rb')) #reads the model
data = cleaning(input("Enter a Text: "))
data = cv.transform([data]).toarray()
output = loaded_model.predict(data)
if output[0]==1:
  result='Stressed'
else:
  result = 'Not Stressed'
print(result)