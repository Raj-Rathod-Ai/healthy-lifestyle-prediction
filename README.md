# Lifestyle Health Risk Assessor - Streamlit App

This is a premium, conversational Streamlit application designed for assessing cardiovascular and general chronic disease risks based on lifestyle attributes.

## Features & Questionnaire Flow
The application guides the user through a detailed 14-step conversational questionnaire:
1. **Age**: Patient's age in years.
2. **Gender**: Male or Female.
3. **Height & Weight**: Inputs are automatically used to compute BMI (without exposing formulas or jargon). Can be bypassed.
4. **Daily Steps**: Odometer or step tracker counts.
5. **Sleep Duration**: Hours of sleep per night.
6. **Water Intake**: Daily hydration in Liters.
7. **Calories Consumed**: Daily nutritional energy intake.
8. **Smoking Habit**: Yes/No smoking status.
9. **Alcohol Habit**: Yes/No alcohol consumption status.
10. **Resting Heart Rate**: Resting pulse in beats per minute (bpm).
11. **Blood Pressure**: Systolic & Diastolic mmHg readings (top/bottom numbers). Can be bypassed.
12. **Cholesterol level**: Serum cholesterol level in mg/dL.
13. **Family History**: Family genetic baseline of cardiovascular or chronic illnesses.
14. **Prediction**: Summarizes input parameters and calculates Low vs Elevated Risk alongside a model confidence probability score.

## How to Run Locally

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Deploying to Streamlit Community Cloud

1. Push this directory to your GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and connect your repository.
3. Set the main file path to `app.py`.

## Keep-Alive Configuration (No-Sleep Workflow)
Streamlit Community Cloud automatically puts applications to sleep after 7 days of inactivity. 

To keep this application awake continuously:
1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
3. Name the secret **`APP_URL`**.
4. Set the value to the deployed URL of your Streamlit app (e.g., `https://your-app-name.streamlit.app`).
5. The daily GitHub Action in `.github/workflows/keep_alive.yml` will automatically ping this URL to ensure it never goes to sleep.
