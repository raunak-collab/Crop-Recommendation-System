
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# 1. Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# 2. Custom CSS
# -----------------------------

st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .main-title {
        font-size: 38px;
        font-weight: 700;
        color: #166534;
    }

    .subtitle {
        font-size: 16px;
        color: #64748b;
    }

    .result-card {
        background-color: #ecfdf5;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #bbf7d0;
        text-align: center;
    }

    .crop-name {
        font-size: 32px;
        font-weight: bold;
        color: #166534;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 3. Load Model
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "crop_model.pkl"

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
feature_names = saved_data["features"]

# -----------------------------
# 4. Sidebar
# -----------------------------

with st.sidebar:
    st.title("🌱 Crop AI")

    st.write("Crop Recommendation System")

    st.divider()

    st.subheader("About Project")

    st.write(
        "This application uses a Machine Learning "
        "model to recommend suitable crops based "
        "on soil nutrients and weather conditions."
    )

    st.divider()

    st.caption("Built using Python, Scikit-learn & Streamlit")

# -----------------------------
# 5. Main Header
# -----------------------------

st.markdown(
    '<div class="main-title">🌱 Crop Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Find a suitable crop based on soil and weather conditions.</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# 6. Input Form
# -----------------------------

st.subheader("🧪 Enter Soil & Weather Details")

with st.form("crop_prediction_form"):

    st.markdown("**Soil Nutrients**")

    col1, col2, col3 = st.columns(3)

    with col1:
        nitrogen = st.number_input(
            "Nitrogen (N)",
            min_value=0.0,
            value=90.0
        )

    with col2:
        phosphorus = st.number_input(
            "Phosphorus (P)",
            min_value=0.0,
            value=42.0
        )

    with col3:
        potassium = st.number_input(
            "Potassium (K)",
            min_value=0.0,
            value=43.0
        )

    st.markdown("**Weather & Soil Conditions**")

    col4, col5, col6, col7 = st.columns(4)

    with col4:
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-10.0,
            max_value=60.0,
            value=25.0
        )

    with col5:
        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    with col6:
        ph = st.number_input(
            "Soil pH",
            min_value=0.0,
            max_value=14.0,
            value=6.5
        )

    with col7:
        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            value=200.0
        )

    submit = st.form_submit_button(
        "🌾 Recommend Crop",
        use_container_width=True
    )

# -----------------------------
# 7. Prediction Result
# -----------------------------


# -----------------------------
# 7. Input Validation & Prediction
# -----------------------------

if submit:

    # Step 1: Collect inputs
    input_values = {
        "N": nitrogen,
        "P": phosphorus,
        "K": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    # Step 2: Validate inputs
    errors = []

    for feature, value in input_values.items():

        if not isinstance(value, (int, float)):
            errors.append(f"{feature} must be a number.")

        elif not pd.notna(value):
            errors.append(f"{feature} cannot be empty.")

    # Step 3: Check feature ranges
    if not errors:

        if nitrogen < 0:
            errors.append("Nitrogen cannot be negative.")

        if phosphorus < 0:
            errors.append("Phosphorus cannot be negative.")

        if potassium < 0:
            errors.append("Potassium cannot be negative.")

        if temperature < -10 or temperature > 60:
            errors.append("Temperature must be between -10 and 60°C.")

        if humidity < 0 or humidity > 100:
            errors.append("Humidity must be between 0 and 100%.")

        if ph < 0 or ph > 14:
            errors.append("Soil pH must be between 0 and 14.")

        if rainfall < 0:
            errors.append("Rainfall cannot be negative.")

    # Step 4: Display errors or predict
    if errors:

        for error in errors:
            st.error(error)

    else:

        try:

            input_data = pd.DataFrame(
                [input_values]
            )

            input_data = input_data[feature_names]

            prediction = model.predict(input_data)
            recommended_crop = prediction[0]

            probabilities = model.predict_proba(input_data)
            confidence = probabilities.max() * 100

            st.divider()
            st.subheader("🎯 Recommendation Result")

            st.success(
                f"Recommended Crop: {recommended_crop.capitalize()}"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Model Estimated Probability",
                    f"{confidence:.2f}%"
                )

            with col2:
                st.metric(
                    "Number of Crop Classes",
                    len(model.classes_)
                )

            st.caption(
                "This is a dataset-based ML prediction, "
                "not a guarantee of agricultural suitability."
            )

        except ValueError as error:
            st.error(f"Invalid input data: {error}")

        except Exception as error:
            st.error("Something went wrong during prediction.")
            st.exception(error)
