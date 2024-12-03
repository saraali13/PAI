import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Sample dataset (replace with actual data)
data = {
    "email": [
        "Win $1000 now!", 
        "Your bank account needs verification", 
        "Meeting at 10 am", 
        "Congrats, you won a prize", 
        "Let's catch up tomorrow"],
    "label": ["Spam", "Spam", "Ham", "Spam", "Ham"]
}

df = pd.DataFrame(data)

# Preprocessing
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['email'])
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Multinomial Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

