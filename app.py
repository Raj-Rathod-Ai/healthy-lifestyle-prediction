import streamlit as st
import utils

# Page configuration
st.set_page_config(
    page_title="Personal Health Risk Assessment",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling (Light & Dark theme compatible, responsive premium SaaS layout)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .saas-card {
        background: padding-box;
        border-radius: 16px;
        padding: 2.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(128, 128, 128, 0.15);
        margin-bottom: 2rem;
    }
    
    .progress-wrapper {
        margin-bottom: 2rem;
    }
    .progress-text {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #EC4899;
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
    }
    
    .question-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        color: #1E293B;
    }
    .question-desc {
        font-size: 1rem;
        color: #64748B;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 2rem;
        transition: all 0.2s ease-in-out;
    }
    
    @media (prefers-color-scheme: dark) {
        .question-title {
            color: #F8FAFC;
        }
        .question-desc {
            color: #94A3B8;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "step" not in st.session_state:
    st.session_state.step = 1

# Answer storage
if "age" not in st.session_state:
    st.session_state.age = int(utils.DEFAULTS['age'])

if "gender" not in st.session_state:
    st.session_state.gender = "Male"

if "height" not in st.session_state:
    st.session_state.height = 170.0
if "weight" not in st.session_state:
    st.session_state.weight = 70.0
if "bmi_known" not in st.session_state:
    st.session_state.bmi_known = True

if "daily_steps" not in st.session_state:
    st.session_state.daily_steps = int(utils.DEFAULTS['daily_steps'])
if "steps_known" not in st.session_state:
    st.session_state.steps_known = True

if "sleep_hours" not in st.session_state:
    st.session_state.sleep_hours = float(utils.DEFAULTS['sleep_hours'])
if "sleep_known" not in st.session_state:
    st.session_state.sleep_known = True

if "water_intake" not in st.session_state:
    st.session_state.water_intake = float(utils.DEFAULTS['water_intake_l'])
if "water_known" not in st.session_state:
    st.session_state.water_known = True

if "calories" not in st.session_state:
    st.session_state.calories = int(utils.DEFAULTS['calories_consumed'])
if "calories_known" not in st.session_state:
    st.session_state.calories_known = True

if "smoker" not in st.session_state:
    st.session_state.smoker = "No"

if "alcohol" not in st.session_state:
    st.session_state.alcohol = "No"

if "resting_hr" not in st.session_state:
    st.session_state.resting_hr = int(utils.DEFAULTS['resting_hr'])
if "hr_known" not in st.session_state:
    st.session_state.hr_known = True

if "sys_bp" not in st.session_state:
    st.session_state.sys_bp = int(utils.DEFAULTS['systolic_bp'])
if "dia_bp" not in st.session_state:
    st.session_state.dia_bp = int(utils.DEFAULTS['diastolic_bp'])
if "bp_known" not in st.session_state:
    st.session_state.bp_known = True

if "cholesterol" not in st.session_state:
    st.session_state.cholesterol = int(utils.DEFAULTS['cholesterol'])
if "chol_known" not in st.session_state:
    st.session_state.chol_known = True

if "family_history" not in st.session_state:
    st.session_state.family_history = "No"

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

def reset_wizard():
    st.session_state.step = 1
    st.session_state.age = int(utils.DEFAULTS['age'])
    st.session_state.gender = "Male"
    st.session_state.height = 170.0
    st.session_state.weight = 70.0
    st.session_state.bmi_known = True
    st.session_state.daily_steps = int(utils.DEFAULTS['daily_steps'])
    st.session_state.steps_known = True
    st.session_state.sleep_hours = float(utils.DEFAULTS['sleep_hours'])
    st.session_state.sleep_known = True
    st.session_state.water_intake = float(utils.DEFAULTS['water_intake_l'])
    st.session_state.water_known = True
    st.session_state.calories = int(utils.DEFAULTS['calories_consumed'])
    st.session_state.calories_known = True
    st.session_state.smoker = "No"
    st.session_state.alcohol = "No"
    st.session_state.resting_hr = int(utils.DEFAULTS['resting_hr'])
    st.session_state.hr_known = True
    st.session_state.sys_bp = int(utils.DEFAULTS['systolic_bp'])
    st.session_state.dia_bp = int(utils.DEFAULTS['diastolic_bp'])
    st.session_state.bp_known = True
    st.session_state.cholesterol = int(utils.DEFAULTS['cholesterol'])
    st.session_state.chol_known = True
    st.session_state.family_history = "No"

st.title("❤️ Lifestyle Health Risk Assessor")
st.markdown("Assess your personal cardiovascular and health risks based on daily habits and metrics.")

TOTAL_STEPS = 14
progress_percentage = int((st.session_state.step - 1) / TOTAL_STEPS * 100)

# Render Progress Bar
st.markdown(f"""
<div class="progress-wrapper">
    <div class="progress-text">
        <span>Question {min(st.session_state.step, TOTAL_STEPS)} of {TOTAL_STEPS}</span>
        <span>{progress_percentage}% Complete</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.progress(progress_percentage / 100.0)

st.markdown('<div class="saas-card">', unsafe_allow_html=True)

if st.session_state.step == 1:
    st.markdown('<div class="question-title">Step 1: Age</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">How old are you?</div>', unsafe_allow_html=True)
    
    age = st.number_input(
        "Age (years)",
        min_value=int(utils.VALIDATION_LIMITS['age']['min']),
        max_value=int(utils.VALIDATION_LIMITS['age']['max']),
        value=st.session_state.age,
        step=1
    )
    st.session_state.age = age
    
    col1, col2 = st.columns([1, 4])
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 2:
    st.markdown('<div class="question-title">Step 2: Gender</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">What is your gender?</div>', unsafe_allow_html=True)
    
    gender = st.selectbox(
        "Gender",
        options=["Male", "Female"],
        index=0 if st.session_state.gender == "Male" else 1
    )
    st.session_state.gender = gender
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 3:
    st.markdown('<div class="question-title">Step 3: Height & Weight</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">We will use this to automatically determine your body ratio.</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my height and weight", value=st.session_state.bmi_known)
    st.session_state.bmi_known = known
    
    if known:
        height = st.number_input(
            "Height (in cm)",
            min_value=utils.VALIDATION_LIMITS['height']['min'],
            max_value=utils.VALIDATION_LIMITS['height']['max'],
            value=st.session_state.height,
            step=1.0
        )
        weight = st.number_input(
            "Weight (in kg)",
            min_value=utils.VALIDATION_LIMITS['weight']['min'],
            max_value=utils.VALIDATION_LIMITS['weight']['max'],
            value=st.session_state.weight,
            step=0.5
        )
        st.session_state.height = height
        st.session_state.weight = weight
    else:
        st.info("Using standard demographic default average body ratio.")
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 4:
    st.markdown('<div class="question-title">Step 4: Daily Steps</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">On average, how many steps do you walk in a single day?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my average daily steps", value=st.session_state.steps_known)
    st.session_state.steps_known = known
    
    if known:
        steps = st.number_input(
            "Average Daily Steps",
            min_value=utils.VALIDATION_LIMITS['daily_steps']['min'],
            max_value=utils.VALIDATION_LIMITS['daily_steps']['max'],
            value=float(st.session_state.daily_steps),
            step=utils.VALIDATION_LIMITS['daily_steps']['step']
        )
        st.session_state.daily_steps = int(steps)
    else:
        st.info(f"Using default healthy average of **{int(utils.DEFAULTS['daily_steps']):,} steps**")
        st.session_state.daily_steps = int(utils.DEFAULTS['daily_steps'])
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 5:
    st.markdown('<div class="question-title">Step 5: Hours of Sleep</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">How many hours of sleep do you typically get per night?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my average sleep hours", value=st.session_state.sleep_known)
    st.session_state.sleep_known = known
    
    if known:
        sleep = st.number_input(
            "Hours of sleep per night",
            min_value=utils.VALIDATION_LIMITS['sleep_hours']['min'],
            max_value=utils.VALIDATION_LIMITS['sleep_hours']['max'],
            value=st.session_state.sleep_hours,
            step=utils.VALIDATION_LIMITS['sleep_hours']['step']
        )
        st.session_state.sleep_hours = sleep
    else:
        st.info(f"Using standard default sleep threshold: **{utils.DEFAULTS['sleep_hours']:.1f} hours**")
        st.session_state.sleep_hours = utils.DEFAULTS['sleep_hours']
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 6:
    st.markdown('<div class="question-title">Step 6: Daily Water Intake</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">How many liters of water do you drink daily?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my average daily water intake", value=st.session_state.water_known)
    st.session_state.water_known = known
    
    if known:
        water = st.number_input(
            "Liters of water",
            min_value=utils.VALIDATION_LIMITS['water_intake_l']['min'],
            max_value=utils.VALIDATION_LIMITS['water_intake_l']['max'],
            value=st.session_state.water_intake,
            step=utils.VALIDATION_LIMITS['water_intake_l']['step']
        )
        st.session_state.water_intake = water
    else:
        st.info(f"Using default hydration baseline: **{utils.DEFAULTS['water_intake_l']:.1f} Liters**")
        st.session_state.water_intake = utils.DEFAULTS['water_intake_l']
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 7:
    st.markdown('<div class="question-title">Step 7: Daily Calories Consumed</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">What is your typical daily calorie consumption?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my calorie consumption", value=st.session_state.calories_known)
    st.session_state.calories_known = known
    
    if known:
        calories = st.number_input(
            "Calories (kcal)",
            min_value=utils.VALIDATION_LIMITS['calories_consumed']['min'],
            max_value=utils.VALIDATION_LIMITS['calories_consumed']['max'],
            value=float(st.session_state.calories),
            step=utils.VALIDATION_LIMITS['calories_consumed']['step']
        )
        st.session_state.calories = int(calories)
    else:
        st.info(f"Using default guideline baseline: **{int(utils.DEFAULTS['calories_consumed']):,} kcal**")
        st.session_state.calories = int(utils.DEFAULTS['calories_consumed'])
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 8:
    st.markdown('<div class="question-title">Step 8: Smoking Habit</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Do you smoke cigarettes/tobacco?</div>', unsafe_allow_html=True)
    
    smoker = st.selectbox(
        "Do you smoke?",
        options=["No", "Yes"],
        index=0 if st.session_state.smoker == "No" else 1
    )
    st.session_state.smoker = smoker
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 9:
    st.markdown('<div class="question-title">Step 9: Alcohol Habit</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Do you regularly consume alcohol?</div>', unsafe_allow_html=True)
    
    alcohol = st.selectbox(
        "Do you drink alcohol?",
        options=["No", "Yes"],
        index=0 if st.session_state.alcohol == "No" else 1
    )
    st.session_state.alcohol = alcohol
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 10:
    st.markdown('<div class="question-title">Step 10: Resting Heart Rate</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Do you know your typical resting heart rate (in beats per minute)?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my resting heart rate", value=st.session_state.hr_known)
    st.session_state.hr_known = known
    
    if known:
        hr = st.number_input(
            "Resting Heart Rate (bpm)",
            min_value=utils.VALIDATION_LIMITS['resting_hr']['min'],
            max_value=utils.VALIDATION_LIMITS['resting_hr']['max'],
            value=float(st.session_state.resting_hr),
            step=utils.VALIDATION_LIMITS['resting_hr']['step']
        )
        st.session_state.resting_hr = int(hr)
    else:
        st.info(f"Using standard clinical baseline: **{int(utils.DEFAULTS['resting_hr'])} bpm**")
        st.session_state.resting_hr = int(utils.DEFAULTS['resting_hr'])
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 11:
    st.markdown('<div class="question-title">Step 11: Blood Pressure</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Do you know your typical resting blood pressure reading?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my blood pressure numbers", value=st.session_state.bp_known)
    st.session_state.bp_known = known
    
    if known:
        sys = st.number_input(
            "Systolic Blood Pressure (top number, e.g. 120)",
            min_value=utils.VALIDATION_LIMITS['systolic_bp']['min'],
            max_value=utils.VALIDATION_LIMITS['systolic_bp']['max'],
            value=float(st.session_state.sys_bp),
            step=utils.VALIDATION_LIMITS['systolic_bp']['step']
        )
        dia = st.number_input(
            "Diastolic Blood Pressure (bottom number, e.g. 80)",
            min_value=utils.VALIDATION_LIMITS['diastolic_bp']['min'],
            max_value=utils.VALIDATION_LIMITS['diastolic_bp']['max'],
            value=float(st.session_state.dia_bp),
            step=utils.VALIDATION_LIMITS['diastolic_bp']['step']
        )
        st.session_state.sys_bp = int(sys)
        st.session_state.dia_bp = int(dia)
    else:
        st.info(f"Using default baseline stats: **{int(utils.DEFAULTS['systolic_bp'])}/{int(utils.DEFAULTS['diastolic_bp'])} mmHg**")
        st.session_state.sys_bp = int(utils.DEFAULTS['systolic_bp'])
        st.session_state.dia_bp = int(utils.DEFAULTS['diastolic_bp'])
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 12:
    st.markdown('<div class="question-title">Step 12: Cholesterol level</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Do you know your blood cholesterol level (in mg/dL)?</div>', unsafe_allow_html=True)
    
    known = st.checkbox("I know my cholesterol number", value=st.session_state.chol_known)
    st.session_state.chol_known = known
    
    if known:
        chol = st.number_input(
            "Total Cholesterol (mg/dL)",
            min_value=utils.VALIDATION_LIMITS['cholesterol']['min'],
            max_value=utils.VALIDATION_LIMITS['cholesterol']['max'],
            value=float(st.session_state.cholesterol),
            step=utils.VALIDATION_LIMITS['cholesterol']['step']
        )
        st.session_state.cholesterol = int(chol)
    else:
        st.info(f"Using average baseline stats: **{int(utils.DEFAULTS['cholesterol'])} mg/dL**")
        st.session_state.cholesterol = int(utils.DEFAULTS['cholesterol'])
        
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Next Question →", on_click=next_step, type="primary")

elif st.session_state.step == 13:
    st.markdown('<div class="question-title">Step 13: Family History</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Is there a history of chronic illnesses or heart diseases in your close family?</div>', unsafe_allow_html=True)
    
    history = st.selectbox(
        "Family History of Illness",
        options=["No", "Yes"],
        index=0 if st.session_state.family_history == "No" else 1
    )
    st.session_state.family_history = history
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        st.button("Review Summary →", on_click=next_step, type="primary")

elif st.session_state.step == 14:
    st.markdown('<div class="question-title">Review Health Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="question-desc">Verify your lifestyle parameters before submitting for risk assessment.</div>', unsafe_allow_html=True)
    
    # Calculate BMI representation
    bmi_val = utils.calculate_bmi(st.session_state.height, st.session_state.weight) if st.session_state.bmi_known else utils.DEFAULTS['bmi']
    show_bmi = f"{bmi_val:.1f}" if st.session_state.bmi_known else "Unknown (using average baseline)"
    
    show_steps = f"{st.session_state.daily_steps:,} steps" if st.session_state.steps_known else "Unknown (using default)"
    show_sleep = f"{st.session_state.sleep_hours:.1f} hours" if st.session_state.sleep_known else "Unknown (using default)"
    show_water = f"{st.session_state.water_intake:.1f} L" if st.session_state.water_known else "Unknown (using default)"
    show_cal = f"{st.session_state.calories:,} kcal" if st.session_state.calories_known else "Unknown (using default)"
    show_hr = f"{st.session_state.resting_hr} bpm" if st.session_state.hr_known else "Unknown (using default)"
    show_bp = f"{st.session_state.sys_bp}/{st.session_state.dia_bp} mmHg" if st.session_state.bp_known else "Unknown (using default)"
    show_chol = f"{st.session_state.cholesterol} mg/dL" if st.session_state.chol_known else "Unknown (using default)"
    
    st.markdown(f"""
    | Metric | Your Profile Value |
    | :--- | :--- |
    | **Age / Gender** | {st.session_state.age} yrs / {st.session_state.gender} |
    | **Estimated Body Ratio (BMI)** | {show_bmi} |
    | **Daily Activity (Steps)** | {show_steps} |
    | **Sleep Duration** | {show_sleep} |
    | **Hydration (Water)** | {show_water} |
    | **Energy Intake (Calories)** | {show_cal} |
    | **Smoking / Alcohol** | Smoker: {st.session_state.smoker} / Drinks: {st.session_state.alcohol} |
    | **Resting Heart Rate** | {show_hr} |
    | **Blood Pressure** | {show_bp} |
    | **Total Cholesterol** | {show_chol} |
    | **Family History** | {st.session_state.family_history} |
    """, unsafe_allow_html=True)
    
    st.write("")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.button("← Back", on_click=prev_step)
    with col2:
        predict_clicked = st.button("❤️ Evaluate Disease Risk", type="primary")
        
    if predict_clicked:
        try:
            with st.spinner("Generating health risk profile..."):
                risk_class, confidence = utils.predict_disease_risk(
                    st.session_state.age,
                    st.session_state.gender,
                    bmi_val,
                    st.session_state.daily_steps,
                    st.session_state.sleep_hours,
                    st.session_state.water_intake,
                    st.session_state.calories,
                    st.session_state.smoker,
                    st.session_state.alcohol,
                    st.session_state.resting_hr,
                    st.session_state.sys_bp,
                    st.session_state.dia_bp,
                    st.session_state.cholesterol,
                    st.session_state.family_history
                )
            
            # Displays the custom styled assessment box
            st.write("")
            if risk_class == 0:
                st.markdown(f"""
                <div style="background: rgba(16, 185, 129, 0.1); border-left: 5px solid #10B981; padding: 1.5rem; border-radius: 8px; margin-top: 1rem;">
                    <h4 style="color: #10B981; margin: 0 0 0.5rem 0;">Low Disease Risk Profile</h4>
                    <p style="font-size: 2.2rem; font-weight: 700; color: #047857; margin: 0;">Healthy Baseline</p>
                    <div style="margin-top: 0.5rem; font-weight: 600; font-size: 1.05rem; color: #065F46;">
                        Model Confidence: {confidence:.1f}%
                    </div>
                    <p style="font-size: 0.95rem; color: #065F46; margin: 0.5rem 0 0 0; line-height: 1.5;">
                        Your reported lifestyle choices and biological markers align closely with a low cardiovascular/chronic disease risk category. Continue maintaining active, balanced daily habits!
                    </p>
                    <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(245, 158, 11, 0.1); border: 1px dashed #F59E0B; border-radius: 6px; font-size: 0.85rem; color: #B45309; text-align: center;">
                        ⚠️ DISCLAIMER: This is a lifestyle self-assessment prototype. It does not replace professional medical diagnosis.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: rgba(239, 68, 68, 0.1); border-left: 5px solid #EF4444; padding: 1.5rem; border-radius: 8px; margin-top: 1rem;">
                    <h4 style="color: #EF4444; margin: 0 0 0.5rem 0;">Elevated Disease Risk Profile</h4>
                    <p style="font-size: 2.2rem; font-weight: 700; color: #B91C1C; margin: 0;">High Risk Risk</p>
                    <div style="margin-top: 0.5rem; font-weight: 600; font-size: 1.05rem; color: #991B1B;">
                        Model Confidence: {confidence:.1f}%
                    </div>
                    <p style="font-size: 0.95rem; color: #991B1B; margin: 0.5rem 0 0 0; line-height: 1.5;">
                        Your daily patterns or indicators show alignment with statistical chronic health profiles. We recommend scheduling a routine health check-up and consulting a medical professional to review key areas.
                    </p>
                    <div style="margin-top: 1rem; padding: 0.5rem; background: rgba(245, 158, 11, 0.1); border: 1px dashed #F59E0B; border-radius: 6px; font-size: 0.85rem; color: #B45309; text-align: center;">
                        ⚠️ DISCLAIMER: This is a lifestyle self-assessment prototype. It does not replace professional medical diagnosis.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.balloons()
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            
    st.write("")
    st.button("🔄 Restart Assessment", on_click=reset_wizard)

st.markdown('</div>', unsafe_allow_html=True)
