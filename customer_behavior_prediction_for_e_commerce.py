# -*- coding: utf-8 -*-
"""Customer Behavior Prediction for E-Commerce

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SUQ3XCrx8yYmtCxp8BVv4PuJZCY_kfhz
"""

import pandas as pd
import numpy as np

# Create a synthetic dataset
np.random.seed(0)

data = {
    'customer_id': np.arange(1, 101),  # 100 customers
    'age': np.random.randint(18, 70, size=100),  # Random ages between 18 and 70
    'gender': np.random.choice(['Male', 'Female'], size=100),  # Random genders
    'annual_income': np.random.randint(30000, 120000, size=100),  # Income between $30k and $120k
    'purchase_history': np.random.randint(1, 20, size=100),  # Number of purchases made
    'last_purchase_days': np.random.randint(1, 365, size=100),  # Days since last purchase
}

df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('ecommerce_data.csv', index=False)

print(df.head())

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('/content/ecommerce_data.csv')

# Preprocessing
# Convert categorical variable to numerical
data['gender'] = data['gender'].map({'Male': 1, 'Female': 0})

# Define features and target variable
X = data[['age', 'gender', 'annual_income', 'purchase_history', 'last_purchase_days']]
y = (data['purchase_history'] > 10).astype(int)  # Target: whether the customer will purchase more than 10 items

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Create a confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Purchased', 'Purchased'], yticklabels=['Not Purchased', 'Purchased'])
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Get feature importances from the model
importances = model.feature_importances_
features = X.columns

# Create a DataFrame for visualization
feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Plotting feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importance')
plt.show()

# Create a pair plot
sns.pairplot(data, hue='purchase_history', palette='Set1')
plt.title('Pair Plot of Features')
plt.show()

from sklearn.metrics import roc_curve, roc_auc_score

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
roc_auc = roc_auc_score(y_test, y_pred)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label='ROC Curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.show()

# Plotting distribution of annual income
plt.figure(figsize=(10, 6))
sns.histplot(data['annual_income'], bins=20, kde=True)
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.show()