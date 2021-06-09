import pandas as pd
import json
import pickle

initial = {"SeniorCitizen": 0,
           "tenure": 0,
           "MonthlyCharges": 0,
           "TotalCharges": 0,
           "gender_Female": 0,
           "gender_Male": 0,
           "Partner_No": 0,
           "Partner_Yes": 0,
           "Dependents_No": 0,
           "Dependents_Yes": 0,
           "PhoneService_No": 0,
           "PhoneService_Yes": 0,
           "MultipleLines_No": 0,
           "MultipleLines_No phone service": 0,
           "MultipleLines_Yes": 0,
           "InternetService_DSL": 0,
           "InternetService_Fiber optic": 0,
           "InternetService_No": 0,
           "OnlineSecurity_No": 0,
           "OnlineSecurity_No internet service": 0,
           "OnlineSecurity_Yes": 0,
           "OnlineBackup_No": 0,
           "OnlineBackup_No internet service": 0,
           "OnlineBackup_Yes": 0,
           "DeviceProtection_No": 0,
           "DeviceProtection_No internet service": 0,
           "DeviceProtection_Yes": 0,
           "TechSupport_No": 0,
           "TechSupport_No internet service": 0,
           "TechSupport_Yes": 0,
           "StreamingTV_No": 0,
           "StreamingTV_No internet service": 0,
           "StreamingTV_Yes": 0,
           "StreamingMovies_No": 0,
           "StreamingMovies_No internet service": 0,
           "StreamingMovies_Yes": 0,
           "Contract_Month-to-month": 0,
           "Contract_One year": 0,
           "Contract_Two year": 0,
           "PaperlessBilling_No": 0,
           "PaperlessBilling_Yes": 0,
           "PaymentMethod_Bank transfer (automatic)": 0,
           "PaymentMethod_Credit card (automatic)": 0,
           "PaymentMethod_Electronic check": 0,
           "PaymentMethod_Mailed check": 0
           }

# input = ([('seniorCitizen', '0'),
#             ('tenure', '1'),
#             ('monthlycharges', '1'),
#             ('totalCharges', '1'),
#             ('gender', 'Female'),
#             ('partner', 'No'),
#             ('dependents', 'No'),
#             ('phoneService', 'No'),
#             ('multipleLines', 'No'),
#             ('internetService', 'DSL'),
#             ('onlineSecurity', 'No'),
#             ('onlineBackup', 'No'),
#             ('deviceProtection', 'No'),
#             ('techSupport', 'No'),
#             ('streamingTV', 'No'),
#             ('streamingMovies', 'No'),
#             ('contract', 'Month-to-month'),
#             ('paperlessBilling', 'No'),
#             ('paymentMethod', 'Bank Transfer (automatic)')])

output = initial


# Defining serializerJson to convert Json data into DataFrame to feed into model
def serializerJson(input):

    # print(output)

    if input.get("seniorCitizen") == 'Yes':
        output["SeniorCitizen"] = 1
    else:
        output["SeniorCitizen"] = 0

    if input.get("tenure") == "":
        output["tenure"] = 0
    else:
        output["tenure"] = float(input.get("tenure"))

    # output["tenure"] = input.get("tenure")

    if input.get("monthlycharges") == "":
        output["MonthlyCharges"] = 0
    else:
        output["MonthlyCharges"] = float(input.get("monthlycharges"))

    # output["MonthlyCharges"] = input.get("monthlycharges")

    if input.get("totalCharges") == "":
        output["TotalCharges"] = 0
    else:
        output["TotalCharges"] = float(input.get("totalCharges"))

    # output["TotalCharges"] = input.get("totalCharges")

    if input.get("gender") == "Male":
        output["gender_Male"] = 1
    else:
        output["gender_Female"] = 1

    if input.get("partner") == "Yes":
        output["Partner_Yes"] = 1
    else:
        output["Partner_No"] = 1

    if input.get("dependents") == "Yes":
        output["Dependents_Yes"] = 1
    else:
        output["Dependents_No"] = 1

    if input.get("phoneService") == "Yes":
        output["PhoneService_Yes"] = 1
    else:
        output["PhoneService_No"] = 1

    # # multiline
    if input.get("multipleLines") == "Yes":
        output["MultipleLines_Yes"] = 1
    elif input.get("multipleLines") == "No phone service":
        output["MultipleLines_No phone service"] = 1
    else:
        output["MultipleLines_No"] = 1

    # internetService
    if input.get("internetService") == "Yes":
        output["InternetService_DSL"] = 1
    elif input.get("internetService") == "Fiber optic":
        output["InternetService_Fiber optic"] = 1
    else:
        output["InternetService_No"] = 1

    # onlineSecurity
    if input.get("onlineSecurity") == "Yes":
        output["OnlineSecurity_Yes"] = 1
    elif input.get("onlineSecurity") == "No internet service":
        output["OnlineSecurity_No internet service"] = 1
    else:
        output["OnlineSecurity_No"] = 1

    # onlineBackup
    if input.get("onlineBackup") == "Yes":
        output["OnlineBackup_Yes"] = 1
    elif input.get("onlineBackup") == "No internet service":
        output["OnlineBackup_No internet service"] = 1
    else:
        output["OnlineBackup_No"] = 1

    # deviceProtection
    if input.get("deviceProtection") == "Yes":
        output["DeviceProtection_Yes"] = 1
    elif input.get("deviceProtection") == "No internet service":
        output["DeviceProtection_No internet service"] = 1
    else:
        output["DeviceProtection_No"] = 1

    # techSupport
    if input.get("techSupport") == "Yes":
        output["TechSupport_Yes"] = 1
    elif input.get("techSupport") == "No internet service":
        output["TechSupport_No internet service"] = 1
    else:
        output["TechSupport_No"] = 1

    # streamingTV
    if input.get("streamingTV") == "Yes":
        output["StreamingTV_Yes"] = 1
    elif input.get("streamingTV") == "No internet service":
        output["StreamingTV_No internet service"] = 1
    else:
        output["StreamingTV_No"] = 1

    # streamingMovies
    if input.get("streamingMovies") == "Yes":
        output["StreamingMovies_Yes"] = 1
    elif input.get("streamingMovies") == "No internet service":
        output["StreamingMovies_No internet service"] = 1
    else:
        output["StreamingMovies_No"] = 1

    # Contract_Month-
    if input.get("contract") == "Month-to-month":
        output["Contract_Month-to-month"] = 1
    elif input.get("contract") == "One year":
        output["Contract_One year"] = 1
    else:
        output["Contract_Two year"] = 1

    # paperlessBilling
    if input.get("paperlessBilling") == "Yes":
        output["PaperlessBilling_Yes"] = 1
    else:
        output["PaperlessBilling_No"] = 1

    # paymentMethod
    if input.get("paymentMethod") == "Bank Transfer (automatic)":
        output["PaymentMethod_Bank transfer (automatic)"] = 1
    elif input.get("paymentMethod") == "Credit card (automatic)":
        output["PaymentMethod_Credit card (automatic)"] = 1
    elif input.get("paymentMethod") == "Electronic Check":
        output["PaymentMethod_Electronic check"] = 1
    else:
        output["PaymentMethod_Mailed check"] = 1

    model = pickle.load(open('model.pkl', 'rb'))
    print(output)
    resNorm = pd.DataFrame(output, index=[0])
    # resNorm = pd.to_numeric(resNorm, errors='coerce')
    # print(resNorm.dtypes)
    # print(resNorm)
    pred = model.predict(resNorm)
    # print(pred)
    lists = pred.tolist()
    json_pred = json.dumps(lists)
    # json_pred = json.dumps(resNorm)

    return json_pred
