I've made a spam classifier using streamlit python.
Dataset for training: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

Steps performed:
1. Data Cleaning: 
  - Removing un-necessary columns
  - Encoding target variable i.e. form spam/ham to 1 and 0 respectively
  - Removed Duplicates
2. EDA
  - Barplots and figures to know the features
  - made a few columns and made a wordcloud to explore the co-relation
3. Text Processing
  - Lowercase
  - Tokenization
  - Removed special characters
  - Removed Stopwords
  - Removed Punctuation
  - Performed Stemming/Lemmetization
4. Model building and evaluation
  tried countVectorizer and tf-idf for vectorization, but tf-idf performed better, so I picked tf-idf
  tried and tested accuracy and percision scores(in imbalanced data, false positives are important in the case of spam detection)
  models i've tried are:
  - Logistic Regression
  - SVC
  - KNeighbors Classifier
  - Gaussian Naive Bayes
  - Multinomial Naive Bayes
  - Bernoulli Naive Bayes
  - Decision Trees Classifier
  - Random Forest Classifier
  - Ada Boost Classifier
  - Bagging Classifier
  - Extra Trees Classifier
  - Gradient Boosting Classifier
  - XGBoost Classifier

    Among all of these models, MultiNommial Naive Bayes and Random Forest Classifier performed the best with the precision 1.0 and higher accuracy.
5. Improved the model
  tried different techniques to make the model perform better:
  - changed the parameter "max_features = 3000" of tf-idf vectorizer: accuracy and precision got better
  - scaled the data using min-max scaling(to keep data between 0 and 1): precision got worse
  - added the feature of number of characters in training: accuracy got worse
  - did voting classification using MultiNomial Naive Bayes, Random Forest, Extra Trees and XGBoost Classifiers: precision got low
  - did stacking classification using MultiNomial Naive Bayes, Random Forest, Extra Trees and XGBoost Classifiers by keeping MultiNomial Naive Bayes as final estimator: accuracy got low

  so, As a result I just kept with the MultiNomial Naive Bayes with tf-idf vectorizer having "max_features = 3000"
6. Pickled the vectorizer and model and made app.py having UI of streamlit

Video I followed: https://www.youtube.com/watch?v=YncZ0WwxyzU&ab_channel=CampusX
Note: Will try to improve its accuracy in future with different dataset and will deploy it too ;)
