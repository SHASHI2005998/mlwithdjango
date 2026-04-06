import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("C:/Users/SHASHIKUMAR T/Downloads/spam.csv")
df.columns = ["label", "message"]

# Clean
df = df.dropna()
df["label"] = df["label"].str.strip().str.lower()
df = df[df["label"].isin(["ham", "spam"])]
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["message"])
y = df["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model (improved)
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)

# 🔥 PREDICTION
y_pred = model.predict(X_test)

# 🔥 ACCURACY
accuracy = accuracy_score(y_test, y_pred)
print("✅ Accuracy:", accuracy)

# 🔥 CONFUSION MATRIX
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 🔥 CLASSIFICATION REPORT
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
test1 = ["Congratulations! You won a free lottery"]
test2 = ["Meeting scheduled at 10 AM"]

print(model.predict(vectorizer.transform(test1)))  # expect 1
print(model.predict(vectorizer.transform(test2)))  # expect 0
# Save model
pickle.dump(model, open("ml_model/spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("ml_model/vectorizer.pkl", "wb"))

print("\n✅ Model saved successfully")