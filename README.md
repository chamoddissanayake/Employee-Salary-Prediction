
# Employee Salary Prediction




This salary prediction application, built with Flask, utilizes a linear regression model to estimate salaries based on years of experience. Users can submit their years of experience via a JSON request to the `/predict-salary` endpoint. The app processes the input and returns a predicted salary, allowing individuals to gauge potential earnings in their field. With a simple and intuitive interface, it serves as a helpful tool for job seekers and professionals alike.
## Run Locally

Install Python 3.10.0


  https://www.python.org/downloads/release/python-3100/


Clone the project

```bash
  git clone https://github.com/chamoddissanayake/Employee-Salary-Prediction.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```
## Tech Stack

**Programming Language:** Python

**Web Framework:** Flask

**Data Handling:**

* Pandas: For data manipulation and analysis
* NumPy: For numerical operations

**Machine Learning:**

* Scikit-learn: For building and training the linear regression model

**Data Format:** JSON
## Usage/Examples

Test the following endpoint using Postman.

POST Method

```bash
http://127.0.0.1:5010/predict-salary
```

Request
```javascript
{
    "yearsExperience":3
}
```
Response
```javascript
{
    "predictedSalary": 54814.92846446466,
    "yearsExperience": 3
}
```
