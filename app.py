import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="HealthCare App",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))


stroke_prediction_model = pickle.load(open(f'{working_dir}/saved_models/stroke_model.sav','rb' ))
thyroid_prediction_model = pickle.load(open(f'{working_dir}/saved_models/thyroid_model.sav','rb' ))
# sidebar for navigation'
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Stroke Prediction', 
                            'Thyroid Detection'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Stroke Prediction Page
if selected == 'Stroke Prediction':

    # page title
    st.title('Stroke Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        hypertension = st.text_input('Does the person have hypertension? 0: No, 1: Yes')

    with col3:
        heart_disease = st.text_input('Does the person have heart disease? 0: No, 1: Yes')

    with col1:
        avg_glucose_level = st.text_input('Average glucose')

    with col2:
        bmi = st.text_input('BMI')

    with col3:
        gender_Male = st.text_input('Male or Female? 0: Female, 1: Male')

    with col1:
        ever_married_Yes = st.text_input('Married or Unmarried ? 0: Unmarried, 1:Married')

    with col2:
        work_type_Never_worked = st.text_input('If the person has never worked enter 1 otherwise enter 0')
    
    with col3:
        work_type_Private = st.text_input('If the person works in private organization enter 1 otherwise enter 0')
    
    with col1:
       work_type_Self_employed = st.text_input('If the person is self-employed enter 1 otherwise enter 0')
    
    with col2:
       work_type_children = st.text_input('If the person is a child enter 1 otherwise enter 0')

    with col3:
        Residence_type_Urban = st.text_input('If the person stays in urban area enter 1 otherwise enter 0')
    
    with col1:
        smoking_status_formerly_smoked = st.text_input('If the person formerly used to smoke enter 1 otherwise enter 0')
    
    with col2:
        smoking_status_never_smoked = st.text_input('If the person has never smoked enter 1 otherwise enter 0')
    
    with col3:
        smoking_status_smokes = st.text_input('If the person smokes enter 1 otherwise enter 0')
    
    

    


    # code for Prediction
    stroke_diagnosis = ''

    # creating a button for Prediction

    if st.button('Stroke Prediction Result'):

        user_input = [age, hypertension, heart_disease, avg_glucose_level, bmi,
        gender_Male, ever_married_Yes, work_type_Never_worked,
       work_type_Private, work_type_Self_employed, work_type_children,
       Residence_type_Urban, smoking_status_formerly_smoked,
       smoking_status_never_smoked, smoking_status_smokes]

        user_input = [float(x) for x in user_input]

        stroke_prediction = stroke_prediction_model.predict([user_input])

        if stroke_prediction[0] == 1:
            stroke_diagnosis = 'The person has a chance of getting stroke'
        else:
            stroke_diagnosis = 'The person is free from the risk of getting stroke'

    st.success(stroke_diagnosis)

# Thyroid Prediction Page
if selected == 'Thyroid Detection':

    # page title
    st.title('Thyroid Detection')

    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex 0: Female, 1: Male')

    with col3:
        thyroid_surgery = st.text_input('Has the person undergone thyroid surgery? 0: No, 1: Yes')

    with col4:
        TSH = st.text_input('TSH')

    with col1:
        T3 = st.text_input('T3')

    with col2:
        TT4 = st.text_input('TT4')

    with col3:
        T4U = st.text_input('T4U')

    with col4:
        FTI = st.text_input('FTI')
    
    
 # code for Prediction
    thyroid_diagnosis = ''

    # creating a button for Prediction

    if st.button('Thyroid Detection Result'):

        user_input = [age, sex, thyroid_surgery, TSH, T3,
        TT4, T4U, FTI]

        user_input = [float(x) for x in user_input]

        thyroid_detection = thyroid_prediction_model.predict([user_input])

        if  thyroid_detection[0] == 1:
            thyroid_diagnosis = 'The person has thyroid'
        else:
            thyroid_diagnosis = 'The person does not have thyroid'

    st.success(thyroid_diagnosis)

