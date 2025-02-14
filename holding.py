# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Load the dataset
container_data = pd.read_csv('ContainerData.csv')

# One-hot encode the categorical feature 'Hue'
container_data = pd.get_dummies(container_data, columns=['Hue'])

# Separate features and target
X = container_data.drop('Priority', axis=1)
y = container_data['Priority']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

# Save the trained model for integration
dump(model, 'container_priority_model.joblib')

# Function to predict container priority
def predict_priority(container_features):
    container_df = pd.DataFrame([container_features], columns=X.columns)
    container_df = container_df.reindex(columns=X.columns, fill_value=0)
    return model.predict(container_df)[0]

# Integrate ML model into A* heuristic
def heuristic(state, goal_bays, ml_model):
    misplaced = 0
    for i, bay in enumerate(state.bays):
        for container in bay:
            if container not in goal_bays[i]:
                container_features = [height, width, hue, moves, hours]  # Placeholder for actual features
                priority = predict_priority(container_features)
                misplaced += 2 if priority == 1 else 1
    return misplaced

# (A* search algorithm code goes here, using the new heuristic function)
