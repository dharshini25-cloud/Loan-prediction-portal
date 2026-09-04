import joblib
import os
import pandas as pd
from django.shortcuts import render
from .models import LoanPrediction


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)



model = joblib.load(
    os.path.join(BASE_DIR, "loan_model.pkl")
)



def clean_amount(value):
    """
    Converts values such as:

    ₹1,00,000
    1,00,000
    ₹ 1,00,000
    100000
    1 00 000

    into:

    100000.0
    """

    if value is None:
        raise ValueError("Amount is empty")

    value = str(value).strip()

    # Remove Indian Rupee symbol
    value = value.replace("₹", "")

    # Remove commas
    value = value.replace(",", "")

    # Remove spaces
    value = value.replace(" ", "")

    # Check after cleaning
    if value == "":
        raise ValueError("Amount is empty")

    # Convert to float
    return float(value)



def home(request):

    result = ""

    if request.method == "POST":

        try:

            

            gender = request.POST.get("gender")
            married = request.POST.get("married")
            dependents = request.POST.get("dependents")
            education = request.POST.get("education")
            self_employed = request.POST.get("self_employed")

            applicant_income = request.POST.get("applicant_income")
            coapplicant_income = request.POST.get("coapplicant_income")
            loan_amount = request.POST.get("loan_amount")
            loan_term = request.POST.get("loan_term")
            credit_history = request.POST.get("credit_history")
            property_area = request.POST.get("property_area")


            if not all([
                gender,
                married,
                dependents,
                education,
                self_employed,
                applicant_income,
                coapplicant_income,
                loan_amount,
                loan_term,
                credit_history,
                property_area
            ]):

                result = "Please fill all fields ❌"

                return render(
                    request,
                    "home.html",
                    {"result": result}
                )


            applicant_income_value = clean_amount(
                applicant_income
            )

            coapplicant_income_value = clean_amount(
                coapplicant_income
            )

            loan_amount_value = clean_amount(
                loan_amount
            )


            if dependents == "3+":

                dependents = 3

            else:

                dependents = int(dependents)


            loan_term_value = float(loan_term)

            credit_history_value = float(credit_history)


            input_data = pd.DataFrame([{

                "Gender": gender,

                "Married": married,

                "Dependents": dependents,

                "Education": education,

                "Self_Employed": self_employed,

                "ApplicantIncome": applicant_income_value,

                "CoapplicantIncome": coapplicant_income_value,

                "LoanAmount": loan_amount_value,

                "Loan_Amount_Term": loan_term_value,

                "Credit_History": credit_history_value,

                "Property_Area": property_area

            }])

            input_data = input_data[
                [
                    "Gender",
                    "Married",
                    "Dependents",
                    "Education",
                    "Self_Employed",
                    "ApplicantIncome",
                    "CoapplicantIncome",
                    "LoanAmount",
                    "Loan_Amount_Term",
                    "Credit_History",
                    "Property_Area"
                ]
            ]

            print("\n====================================")
            print("MODEL INPUT:")
            print(input_data)

            print("\nDATA TYPES:")
            print(input_data.dtypes)

            print("\nMODEL TYPE:")
            print(type(model))

            print("====================================")


            prediction = model.predict(input_data)


            print("\nMODEL PREDICTION:")
            print(prediction)

            print("====================================\n")


            if prediction[0] == "Y":

                result = "Loan Approved ✅"

            elif prediction[0] == "N":

                result = "Loan Rejected ❌"

            else:

                result = f"Unknown Prediction: {prediction[0]}"


            LoanPrediction.objects.create(

                gender=gender,

                married=married,

                dependents=dependents,

                education=education,

                self_employed=self_employed,

                applicant_income=applicant_income_value,

                coapplicant_income=coapplicant_income_value,

                loan_amount=loan_amount_value,

                loan_term=loan_term_value,

                credit_history=credit_history_value,

                property_area=property_area,

                result=result
            )


        except ValueError as e:

            print("\n🔥 VALUE ERROR:")
            print(e)

            result = f"Invalid amount/value ❌: {e}"


        except Exception as e:

            print("\n🔥 REAL MODEL ERROR:")
            print(e)

            result = f"Error in prediction ❌: {e}"


    return render(
        request,
        "home.html",
        {"result": result}
    )


def dashboard(request):

    data = LoanPrediction.objects.all()

    print("TOTAL DATA:", data)

    return render(
        request,
        "dashboard.html",
        {"data": data}
    )