# Fake News Detection
The goal is to develop a Machine Learning model that can detect fake news with accuracy. 
The model will be integrated into the Chrome plug-in and will provide users with a real-time indication of the veracity of the news they are reading.

## Dataset
Two [dataset](https://proai-datasets.s3.eu-west-3.amazonaws.com/fake_news.zip) are given:
1. Real news 
2. Fake news

## Questions to analyze:
1. Are fake news more frequent in a particular category?
2. Are there topics that are more prone to fake news?
3. Do fake news headlines exhibit recurring patterns?

## ML Model
- The model will be developed using Natural Language Processing (NLP) and Machine Learning techniques.
- It will be trained with true and fake news datasets to recognize text patterns associated with untrue news. Relevant features, such as headlines, keywords and categories of news will be analyzed.
- Performance metrics (e.g., accuracy, precision, recall) will be used to evaluate the effectiveness of the model.
- Optimization techniques will be applied to improve the ability of fake news recognition.
- Once training is complete, the model will be exported to pickle format for implementation.
- The Machine Learning Engineer and Web Developer team will integrate the model into the Chrome plug-in.

## Technology
Python
