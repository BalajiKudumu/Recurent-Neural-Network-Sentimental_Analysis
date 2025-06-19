import numpy as np
import pandas as pd
import tensorflow
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import sequence
# from tensorflow.keras.datasets import imdb

## Load the IMDB word index.
word_index=tensorflow.keras.datasets.imdb.get_word_index()
reverse_word_index={value: key for key, value  in word_index.items()}


# Load the pre-trained model with ReLU activation
model=tensorflow.keras.models.load_model('simple_rnn_model.h5')


# Step 2: Helper function
## Function to decode the reviews
def decoded_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3, '?') for i in encoded_review])

# Function to preprocess user input
def preproces_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word, 2)+3 for word in words]
    padding_review=tensorflow.keras.preprocessing.sequence.pad_sequences([encoded_review], maxlen=500)
    return padding_review


# ## Step 3 Prediction Function
# def predict_sentiment(review):
#     preprocessed_input=preproces_text(review)
#     prediction=model.predict(preprocessed_input)
#     sentiment='Positive' if prediction[0][0]>0.5 else 'Negative'
#     return sentiment, prediction[0][0]


## Streamlit App
import streamlit as st

st.title('IMDB Movie Review Sentimental Analysis')
st.write('Enter a Movie review to classify it as positive or negative.')


# User Input
user_input=st.text_area('Movie Review')

if st.button('Classify'):
    preprocessed_input=preproces_text(user_input)


    ## Make Prediction
    prediction=model.predict(preprocessed_input)
    sentiment='Positive' if prediction[0][0]>0.5 else 'Negative'

    ## Display the results
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please write a Movie review')
