from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

X = [
    [1, 35], [2, 40], [3, 45], [4, 50],
    [5, 20], [6, 25], [7, 30], [8, 55]
]

y = [0, 0, 0, 0, 1, 1, 1, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Actual:", y_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))



#if not working : try this
# Naïve Bayes Classifier - Simple Version

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# # --- 1) Data Preparation ---
# data = {'Hours_Studied':[1,2,3,4,5,6,7,8],
#         'Exam_Result':['Fail','Fail','Fail','Pass','Pass','Pass','Pass','Pass']}
# df = pd.DataFrame(data)
# X = df[['Hours_Studied']]
# y = df['Exam_Result']
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

# # --- 2) Training Naïve Bayes Model ---
# model = GaussianNB()
# model.fit(X_train, y_train)

# # --- 3) Testing & Evaluation ---
# y_pred = model.predict(X_test)
# print("Predictions:", y_pred)
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))