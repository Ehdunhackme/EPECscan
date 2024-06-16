import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Define actual and predicted labels
actual_labels = ['Rod'] * 100 + ['Microcolony'] * 100 + ['Background'] * 100
predicted_labels = (['Rod'] * 100 + ['Microcolony'] * 0 + ['Background'] * 0 +
                    ['Rod'] * 1 + ['Microcolony'] * 97 + ['Background'] * 2 +
                    ['Rod'] * 1 + ['Microcolony'] * 0 + ['Background'] * 99)

# Generate confusion matrix
conf_matrix = confusion_matrix(actual_labels, predicted_labels, labels=['Rod', 'Microcolony', 'Background'])

# Normalize confusion matrix
conf_matrix_normalized = conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis]

# Create DataFrames for better visualization
conf_matrix_df = pd.DataFrame(conf_matrix, index=['Actual: Rod', 'Actual: Microcolony', 'Actual: Background'],
                              columns=['Predicted: Rod', 'Predicted: Microcolony', 'Predicted: Background'])
conf_matrix_normalized_df = pd.DataFrame(conf_matrix_normalized, index=['Actual: Rod', 'Actual: Microcolony', 'Actual: Background'],
                                         columns=['Predicted: Rod', 'Predicted: Microcolony', 'Predicted: Background'])

# Calculate accuracy, precision, recall, and F1 score
accuracy = accuracy_score(actual_labels, predicted_labels)
precision = precision_score(actual_labels, predicted_labels, average=None, labels=['Rod', 'Microcolony', 'Background'])
recall = recall_score(actual_labels, predicted_labels, average=None, labels=['Rod', 'Microcolony', 'Background'])
f1 = f1_score(actual_labels, predicted_labels, average=None, labels=['Rod', 'Microcolony', 'Background'])

# Print results
print("Confusion Matrix:\n", conf_matrix_df)
print("\nNormalized Confusion Matrix:\n", conf_matrix_normalized_df)
print("\nAccuracy: {:.2%}".format(accuracy))
print("\nPrecision (Rod, Microcolony, Background):", precision)
print("Recall (Rod, Microcolony, Background):", recall)
print("F1 Score (Rod, Microcolony, Background):", f1)

# Plot normalized confusion matrix using seaborn heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix_normalized_df, annot=True, fmt='.2f', cmap='Blues', cbar=True)
plt.title('Normalized Confusion Matrix')
plt.ylabel('Actual Class')
plt.xlabel('Predicted Class')
plt.show()
