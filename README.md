 Loan Management Portal with AI-Based Eligibility Predictor



📌 Project Overview



The Loan Management Portal with AI-Based Eligibility Predictor is a web-based application developed using Python and Django.



The system helps users enter applicant details and predicts whether the applicant is eligible for a loan using a Machine Learning model.



The application combines a Django web interface, Machine Learning prediction, and MySQL database to provide an integrated loan eligibility management system.



\---



🎯 Objectives



\- To develop a web-based loan management system.

\- To collect applicant information through an easy-to-use interface.

\- To predict loan eligibility using Machine Learning.

\- To store loan application and prediction details in a database.

\- To provide a simple dashboard for viewing loan-related information.

\- To demonstrate the practical use of Machine Learning in financial decision support.



\---



 🚀 Features



 1. Loan Application



Users can enter important applicant information such as:



\- Gender

\- Marital Status

\- Number of Dependents

\- Education

\- Self Employment Status

\- Applicant Income

\- Coapplicant Income

\- Loan Amount

\- Loan Term

\- Credit History

\- Property Area



2. AI-Based Loan Eligibility Prediction



After submitting the applicant information, the trained Machine Learning model processes the input and predicts the loan eligibility status.



The result is displayed to the user as:



\- Loan Approved

\- Loan Not Approved



 3. Database Management



The application stores loan prediction records in a MySQL database.



The stored information can be viewed and managed through the database system.



 4. Dashboard



The application provides a dashboard for viewing loan-related information and prediction records.



\---



 🤖 Machine Learning



The application uses a Machine Learning classification model to predict loan eligibility.



The model was trained using applicant-related features such as income, education, credit history, loan amount, loan term, and property area.



Categorical features are converted into numerical values using encoders before they are provided to the Machine Learning model.



The trained model is stored using the Joblib library and loaded by the Django application during prediction.



 Prediction Process





User enters applicant details

&#x20;           ↓

Django receives the form data

&#x20;           ↓

Input data is cleaned and formatted

&#x20;           ↓

Categorical values are encoded

&#x20;           ↓

Data is passed to the trained ML model

&#x20;           ↓

Model predicts loan eligibility

&#x20;           ↓

Prediction result is displayed

&#x20;           ↓

Application details are stored in MySQL

Project Overview:

Applicant
    ↓
Enter Loan Details
    ↓
Django Web Application
    ↓
Input Data Preprocessing
    ↓
Categorical Encoding
    ↓
Machine Learning Model
    ↓
Loan Eligibility Prediction
    ↓
Approved / Not Approved
    ↓
Store Application in MySQL
    ↓
View Records in Dashboard

