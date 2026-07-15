import os
import pickle
import pandas as pd
import numpy as np

# Column statistics derived from the dataset
DEFAULTS = {
    'age': 48.0,
    'gender': 0,          # Male (0), Female (1)
    'bmi': 29.0,
    'daily_steps': 10468.0,
    'sleep_hours': 6.5,
    'water_intake_l': 2.8,
    'calories_consumed': 2603.0,
    'smoker': 0,
    'alcohol': 0,
    'resting_hr': 74.0,
    'systolic_bp': 135.0,
    'diastolic_bp': 89.0,
    'cholesterol': 224.0,
    'family_history': 0
}

VALIDATION_LIMITS = {
    'age': {'min': 1.0, 'max': 120.0, 'step': 1.0},
    'height': {'min': 100.0, 'max': 250.0, 'step': 1.0},
    'weight': {'min': 30.0, 'max': 250.0, 'step': 1.0},
    'daily_steps': {'min': 0.0, 'max': 50000.0, 'step': 500.0},
    'sleep_hours': {'min': 0.0, 'max': 24.0, 'step': 0.5},
    'water_intake_l': {'min': 0.0, 'max': 10.0, 'step': 0.1},
    'calories_consumed': {'min': 500.0, 'max': 10000.0, 'step': 50.0},
    'resting_hr': {'min': 40.0, 'max': 200.0, 'step': 1.0},
    'systolic_bp': {'min': 70.0, 'max': 250.0, 'step': 1.0},
    'diastolic_bp': {'min': 40.0, 'max': 150.0, 'step': 1.0},
    'cholesterol': {'min': 100.0, 'max': 500.0, 'step': 5.0}
}

# Training mappings:
# gender: Male -> 0, Female -> 1
GENDER_MAPPING = {'Male': 0, 'Female': 1}
SMOKER_MAPPING = {'No': 0, 'Yes': 1}
ALCOHOL_MAPPING = {'No': 0, 'Yes': 1}
HISTORY_MAPPING = {'No': 0, 'Yes': 1}

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'decision_tree_model.pkl')

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

def calculate_bmi(height_cm, weight_kg):
    if height_cm is None or weight_kg is None or height_cm <= 0:
        return DEFAULTS['bmi']
    height_m = height_cm / 100.0
    return round(weight_kg / (height_m ** 2), 2)

def predict_disease_risk(age, gender, bmi, daily_steps, sleep_hours, water_intake_l, 
                         calories_consumed, smoker, alcohol, resting_hr, 
                         systolic_bp, diastolic_bp, cholesterol, family_history):
    """
    Predict disease risk and confidence.
    Categorical values are encoded, and None inputs fallback to defaults.
    """
    model = load_model()
    
    # Encodings
    enc_gender = GENDER_MAPPING.get(gender, DEFAULTS['gender'])
    enc_smoker = SMOKER_MAPPING.get(smoker, DEFAULTS['smoker'])
    enc_alcohol = ALCOHOL_MAPPING.get(alcohol, DEFAULTS['alcohol'])
    enc_history = HISTORY_MAPPING.get(family_history, DEFAULTS['family_history'])
    
    # Numeric Fallbacks
    val_age = age if age is not None else DEFAULTS['age']
    val_bmi = bmi if bmi is not None else DEFAULTS['bmi']
    val_steps = daily_steps if daily_steps is not None else DEFAULTS['daily_steps']
    val_sleep = sleep_hours if sleep_hours is not None else DEFAULTS['sleep_hours']
    val_water = water_intake_l if water_intake_l is not None else DEFAULTS['water_intake_l']
    val_calories = calories_consumed if calories_consumed is not None else DEFAULTS['calories_consumed']
    val_hr = resting_hr if resting_hr is not None else DEFAULTS['resting_hr']
    val_sys = systolic_bp if systolic_bp is not None else DEFAULTS['systolic_bp']
    val_dia = diastolic_bp if diastolic_bp is not None else DEFAULTS['diastolic_bp']
    val_chol = cholesterol if cholesterol is not None else DEFAULTS['cholesterol']
    
    # Construct feature matrix matching model columns exactly:
    # ['age', 'gender', 'bmi', 'daily_steps', 'sleep_hours', 'water_intake_l',
    #  'calories_consumed', 'smoker', 'alcohol', 'resting_hr', 'systolic_bp',
    #  'diastolic_bp', 'cholesterol', 'family_history']
    features_df = pd.DataFrame([{
        'age': float(val_age),
        'gender': enc_gender,
        'bmi': float(val_bmi),
        'daily_steps': float(val_steps),
        'sleep_hours': float(val_sleep),
        'water_intake_l': float(val_water),
        'calories_consumed': float(val_calories),
        'smoker': enc_smoker,
        'alcohol': enc_alcohol,
        'resting_hr': float(val_hr),
        'systolic_bp': float(val_sys),
        'diastolic_bp': float(val_dia),
        'cholesterol': float(val_chol),
        'family_history': enc_history
    }])
    
    pred_class = model.predict(features_df)[0]
    probabilities = model.predict_proba(features_df)[0]
    
    class_idx = list(model.classes_).index(pred_class)
    confidence = float(probabilities[class_idx]) * 100.0
    
    return int(pred_class), confidence
