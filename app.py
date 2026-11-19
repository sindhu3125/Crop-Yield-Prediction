
# import streamlit as st
# import pandas as pd
# import pickle
# from pathlib import Path

# # Page configuration
# st.set_page_config(
#     page_title="Crop Yield Prediction",
#     page_icon="🌾",
#     layout="wide"
# )

# # File paths
# folder = Path(__file__).parent
# model_path = folder / "dtree_model.pkl"
# data_path = folder / "crop_yield.csv"

# # Load model and preprocessing objects
# try:
#     with open(model_path, "rb") as file:
#         saved_objects = pickle.load(file)

#     model = saved_objects["model"]
#     encoder = saved_objects["encoder"]
#     scaler = saved_objects["scaler"]

# except Exception as e:
#     st.error(f"Error loading model: {e}")
#     st.stop()

# # Load dataset for dashboard
# try:
#     data = pd.read_csv(data_path)
# except Exception as e:
#     data = None


# # Sidebar navigation
# st.sidebar.title("🌾 Crop Yield Prediction")

# page = st.sidebar.radio(
#     "Navigation",
#     ["Prediction", "Dashboard"]
# )


# # =====================================
# # PREDICTION PAGE
# # =====================================

# if page == "Prediction":

#     st.title("🌾 Crop Yield Prediction")
#     st.write(
#         "Predict expected crop yield based on agricultural factors."
#     )

#     st.divider()

#     with st.form("prediction_form"):

#         st.header("Enter Crop Details")

#         crop = st.selectbox(
#             "Select Crop",
#             encoder.categories_[2]
#         )

#         state = st.selectbox(
#             "Select State",
#             encoder.categories_[0]
#         )

#         season = st.selectbox(
#             "Select Season",
#             encoder.categories_[1]
#         )

#         production = st.number_input(
#             "Production",
#             min_value=0.0,
#             value=1000.0
#         )

#         area = st.number_input(
#             "Area",
#             min_value=0.0,
#             value=1000.0
#         )

#         rainfall = st.number_input(
#             "Annual Rainfall",
#             min_value=0.0,
#             value=1000.0
#         )

#         fertilizer = st.number_input(
#             "Fertilizer",
#             min_value=0.0,
#             value=1000.0
#         )

#         submit = st.form_submit_button("Predict Yield")

#     if submit:

#         input_data = pd.DataFrame([{
#             "Crop": crop,
#             "Production": production,
#             "State": state,
#             "Area": area,
#             "Annual_Rainfall": rainfall,
#             "Fertilizer": fertilizer,
#             "Season": season
#         }])

#         try:

#             # Encode categorical features
#             cat_cols = ["State", "Season", "Crop"]

#             input_data[cat_cols] = encoder.transform(
#                 input_data[cat_cols]
#             )

#             # Scale numerical features
#             numeric_cols = [
#                 "Production",
#                 "Area",
#                 "Annual_Rainfall",
#                 "Fertilizer"
#             ]

#             input_data[numeric_cols] = scaler.transform(
#                 input_data[numeric_cols]
#             )

#             # Select features in training order
#             selected_features = [
#                 "Crop",
#                 "Production",
#                 "State",
#                 "Area",
#                 "Annual_Rainfall",
#                 "Fertilizer",
#                 "Season"
#             ]

#             input_data = input_data[selected_features]

#             # Predict
#             prediction = model.predict(input_data)

#             st.divider()
#             st.success("Prediction Completed!")

#             st.metric(
#                 "Predicted Crop Yield (Tonnes per Hectare)",
#                 f"{prediction[0]:,.2f}"
#             )

#         except Exception as e:
#             st.error(f"Prediction Error: {e}")


# # =====================================
# # DASHBOARD PAGE
# # =====================================

# elif page == "Dashboard":

#     st.title("📊 Crop Yield Dashboard")
#     st.write(
#         "Explore agricultural data through different visualizations."
#     )

#     st.divider()

#     if data is None:
#         st.error(
#             "Dashboard dataset not found. "
#             "Please keep crop_yield.csv in the same folder as app.py."
#         )

#     else:

#         required_cols = [
#             "Crop", "Crop_Year", "Yield",
#             "Annual_Rainfall", "Production"
#         ]

#         missing_cols = [
#             col for col in required_cols if col not in data.columns
#         ]

#         if missing_cols:
#             st.error(f"Missing dataset columns: {missing_cols}")

#         else:

#             # Clean chart data
#             chart_data = data.copy()

#             for col in [
#                 "Crop_Year", "Yield",
#                 "Annual_Rainfall", "Production"
#             ]:
#                 chart_data[col] = pd.to_numeric(
#                     chart_data[col], errors="coerce"
#                 )

#             chart_data = chart_data.dropna(
#                 subset=required_cols
#             )

#             # Dataset overview
#             st.header("Dataset Overview")

#             col1, col2, col3 = st.columns(3)

#             col1.metric("Total Records", f"{len(chart_data):,}")
#             col2.metric(
#                 "Number of Crops",
#                 chart_data["Crop"].nunique()
#             )
#             col3.metric(
#                 "Average Yield",
#                 f"{chart_data['Yield'].mean():.2f} t/ha"
#             )

#             st.divider()

#             # Chart 1: Average yield by crop
#             st.subheader("1. Average Yield by Crop")

#             crop_yield = (
#                 chart_data.groupby("Crop")["Yield"]
#                 .mean()
#                 .sort_values(ascending=False)
#                 .head(10)
#             )

#             st.bar_chart(crop_yield)

#             st.divider()

#             # Chart 2: Yearly yield trend
#             st.subheader("2. Crop Yield Trend Over Years")

#             yearly_yield = (
#                 chart_data.groupby("Crop_Year")["Yield"]
#                 .mean()
#                 .sort_index()
#             )

#             st.line_chart(yearly_yield)

#             st.divider()

#             # Chart 3: Rainfall vs Yield
#             st.subheader("3. Annual Rainfall vs Crop Yield")

#             rainfall_yield = chart_data[
#                 ["Annual_Rainfall", "Yield"]
#             ]

#             st.scatter_chart(
#                 rainfall_yield,
#                 x="Annual_Rainfall",
#                 y="Yield"
#             )

#             st.divider()

#             # Chart 4: Production by crop
#             st.subheader("4. Production by Crop")

#             crop_production = (
#                 chart_data.groupby("Crop")["Production"]
#                 .sum()
#                 .sort_values(ascending=False)
#                 .head(10)
#             )

#             st.area_chart(crop_production)

#             st.divider()

#             st.caption(
#                 "Dashboard visualizations are based on the "
#                 "historical crop yield dataset."
#             )



import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# =====================================
# COLOR THEME
# =====================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F1F8E9;
    }

    [data-testid="stSidebar"] {
        background-color: #C8E6C9;
    }

    h1, h2, h3 {
        color: #1B5E20;
    }

    div.stButton > button {
        background-color: #2E7D32;
        color: white;
        border-radius: 8px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #F9A825;
        color: black;
    }

    div[data-testid="stMetric"] {
        background-color: #DCEDC8;
        padding: 15px;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# File paths
folder = Path(__file__).parent
model_path = folder / "dtree2_model.pkl"
data_path = folder / "crop_yield.csv"

# Load model and preprocessing objects
try:
    with open(model_path, "rb") as file:
        saved_objects = pickle.load(file)

    model = saved_objects["model"]
    encoder = saved_objects["encoder"]
    scaler = saved_objects["scaler"]

except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Load dataset for dashboard
try:
    data = pd.read_csv(data_path)
except Exception as e:
    data = None


# Sidebar navigation
st.sidebar.title("🌾 Crop Yield Prediction")

page = st.sidebar.radio(
    "Navigation",
    ["Prediction", "Dashboard"]
)


# =====================================
# PREDICTION PAGE
# =====================================

if page == "Prediction":

    st.title("🌾 Crop Yield Prediction")
    st.write(
        "Predict expected crop yield based on agricultural factors."
    )

    st.divider()

    with st.form("prediction_form"):

        st.header("Enter Crop Details")

        crop = st.selectbox(
            "Select Crop",
            encoder.categories_[2]
        )

        state = st.selectbox(
            "Select State",
            encoder.categories_[0]
        )

        season = st.selectbox(
            "Select Season",
            encoder.categories_[1]
        )

        production = st.number_input(
            "Production",
            min_value=0.0,
            value=1000.0
        )

        area = st.number_input(
            "Area",
            min_value=0.0,
            value=1000.0
        )

        rainfall = st.number_input(
            "Annual Rainfall",
            min_value=0.0,
            value=1000.0
        )

        fertilizer = st.number_input(
            "Fertilizer",
            min_value=0.0,
            value=1000.0
        )

        submit = st.form_submit_button("Predict Yield")

    if submit:

        input_data = pd.DataFrame([{
            "Crop": crop,
            "Production": production,
            "State": state,
            "Area": area,
            "Annual_Rainfall": rainfall,
            "Fertilizer": fertilizer,
            "Season": season
        }])

        try:

            # Encode categorical features
            cat_cols = ["State", "Season", "Crop"]

            input_data[cat_cols] = encoder.transform(
                input_data[cat_cols]
            )

            # Scale numerical features
            numeric_cols = [
                "Production",
                "Area",
                "Annual_Rainfall",
                "Fertilizer"
            ]

            input_data[numeric_cols] = scaler.transform(
                input_data[numeric_cols]
            )

            # Select features in training order
            selected_features = [
                "Crop",
                "Production",
                "State",
                "Area",
                "Annual_Rainfall",
                "Fertilizer",
                "Season"
            ]

            input_data = input_data[selected_features]

            # Predict
            prediction = model.predict(input_data)

            st.divider()
            st.success("Prediction Completed!")

            st.metric(
                "Predicted Crop Yield (Tonnes per Hectare)",
                f"{prediction[0]:,.2f}"
            )

        except Exception as e:
            st.error(f"Prediction Error: {e}")


# =====================================
# DASHBOARD PAGE
# =====================================

elif page == "Dashboard":

    st.title("📊 Crop Yield Dashboard")
    st.write(
        "Explore agricultural data through different visualizations."
    )

    st.divider()

    if data is None:
        st.error(
            "Dashboard dataset not found. "
            "Please keep crop_yield.csv in the same folder as app.py."
        )

    else:

        required_cols = [
            "Crop", "Crop_Year", "Yield",
            "Annual_Rainfall", "Production"
        ]

        missing_cols = [
            col for col in required_cols if col not in data.columns
        ]

        if missing_cols:
            st.error(f"Missing dataset columns: {missing_cols}")

        else:

            # Clean chart data
            chart_data = data.copy()

            for col in [
                "Crop_Year", "Yield",
                "Annual_Rainfall", "Production"
            ]:
                chart_data[col] = pd.to_numeric(
                    chart_data[col], errors="coerce"
                )

            chart_data = chart_data.dropna(
                subset=required_cols
            )

            # Dataset overview
            st.header("Dataset Overview")

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Records", f"{len(chart_data):,}")
            col2.metric(
                "Number of Crops",
                chart_data["Crop"].nunique()
            )
            col3.metric(
                "Average Yield",
                f"{chart_data['Yield'].mean():.2f} t/ha"
            )

            st.divider()

            # Chart 1: Average yield by crop
            st.subheader("1. Average Yield by Crop")

            crop_yield = (
                chart_data.groupby("Crop")["Yield"]
                .mean()
                .sort_values(ascending=False)
                .head(10)
            )

            st.bar_chart(crop_yield)

            st.divider()

            # Chart 2: Yearly yield trend
            st.subheader("2. Crop Yield Trend Over Years")

            yearly_yield = (
                chart_data.groupby("Crop_Year")["Yield"]
                .mean()
                .sort_index()
            )

            st.line_chart(yearly_yield)

            st.divider()

            # Chart 3: Rainfall vs Yield
            st.subheader("3. Annual Rainfall vs Crop Yield")

            rainfall_yield = chart_data[
                ["Annual_Rainfall", "Yield"]
            ]

            st.scatter_chart(
                rainfall_yield,
                x="Annual_Rainfall",
                y="Yield"
            )

            st.divider()

            # Chart 4: Production by crop
            st.subheader("4. Production by Crop")

            crop_production = (
                chart_data.groupby("Crop")["Production"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )

            st.area_chart(crop_production)

            st.divider()

            st.caption(
                "Dashboard visualizations are based on the "
                "historical crop yield dataset."
            )
