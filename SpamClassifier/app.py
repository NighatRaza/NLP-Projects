import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y
    # y.clear()
    y = []
    for i in text:
        if i not  in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y
    y = []
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
    # return y

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title("Spam Classifier")

input_text = st.text_area("Enter the message")

if st.button("Predict"):
    # 1. preprocess
    transformed_text = transform_text(input_text)

    # 2. vectorize
    vector_input = tfidf.transform([transformed_text])

    # 3. predict
    result = model.predict(vector_input)[0]

    # 4. display
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")

