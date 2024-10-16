from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create a Flask app
app = Flask(__name__)

# Load and prepare the data
def load_and_train_model():
    # Assuming 'Salary.csv' is available in the current directory
    data = pd.read_csv('Salary.csv')

    # Prepare the data
    X = data[['YearsExperience']]  # Features
    y = data['Salary']  # Target variable

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

# Train the model once on startup
model = load_and_train_model()

@app.route('/predict-salary', methods=['POST'])
def predict_salary():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract 'years of experience' from the data
        years_experience = data.get('yearsExperience')

        if years_experience is None:
            return jsonify({"error": "yearsExperience field is required"}), 400

        # Prepare the input for the model
        experience_array = np.array([[years_experience]])

        # Predict the salary based on years of experience
        predicted_salary = model.predict(experience_array)

        # Return the predicted salary as JSON
        return jsonify({
            "yearsExperience": years_experience,
            "predictedSalary": predicted_salary[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5010)
