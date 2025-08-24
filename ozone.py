import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

# import plotly.graph_objects as go
import numpy as np


# Page 1: Upload Dataset
def page_upload_dataset():
    st.title("Ozone Layer Depletion Analysis and Prediction")
    st.header("Upload Your CSV Dataset")
    uploaded_file = st.file_uploader("Choose a file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the uploaded data:")
        st.write(df.head())
        # Normalize the data
        # df = normalize_data(df)
        # Save the DataFrame for later access
        st.session_state.df = df


# Page 2: Perform Analysis and Prediction
def page_analysis_and_prediction():
    st.title("Ozone Layer Analysis and Prediction")
    st.header("Analysis and Prediction")
    if "df" not in st.session_state:
        st.error("Please upload a dataset on the first page.")
        return
    df = st.session_state.df
    df = df.rename(columns={"date": "ds", "0-700du": "y"})
    df.replace({"?": np.nan}, inplace=True)
    df = df.fillna(method="ffill").copy()
    # Perform analysis and prediction
    model = Prophet()
    model.fit(df)
    future_dates = model.make_future_dataframe(periods=3650)
    prediction = model.predict(future_dates)
    # Plot forecast
    fig = plot_plotly(model, prediction)
    st.plotly_chart(fig, use_container_width=True)

    # Plot trend, yearly, and weekly seasonality
    st.markdown("Trend, yearly and weekly seasonality of the time series data")
    components_fig = plot_components_plotly(model, prediction)
    st.plotly_chart(components_fig, use_container_width=True)


# Page 3: Future Data Points
def page_future_data_points():
    st.title("Future Data Points")
    st.header("Select a Date")
    if "df" not in st.session_state:
        st.error("Please upload a dataset on the first page.")
        return
    df = st.session_state.df
    df = df.rename(columns={"date": "ds", "0-700du": "y"})
    df.replace({"?": np.nan}, inplace=True)
    df = df.fillna(method="ffill").copy()
    min_date = pd.to_datetime(df["ds"]).min().date()
    max_date = pd.to_datetime(df["ds"]).max().date() + pd.Timedelta(
        days=3652
    )  # Extend max date by 10 years
    selected_date = st.sidebar.date_input(
        "Select a Date", min_value=min_date, max_value=max_date, value=min_date
    )
    if st.sidebar.button("Get Future Data Point"):
        if selected_date is not None:
            future_date = pd.to_datetime(selected_date)
            future_value = get_future_value(df, future_date)
            if future_value is None:
                st.error("No data available for the selected date.")
            else:
                st.success(
                    f"### The ozone level on {future_date.strftime('%Y-%m-%d')} is **{future_value:.2f} Dobson Units.**"
                )


def get_future_value(df, future_date):
    model = Prophet()
    model.fit(df)
    future_dates = model.make_future_dataframe(periods=3652)
    prediction = model.predict(future_dates)
    future_value = prediction.loc[prediction["ds"] == future_date, "yhat"].values
    # Normalize future predicted value between 0 and 700
    min_val = min(prediction["yhat"])
    max_val = max(prediction["yhat"])
    normalized_min = 0
    normalized_max = 700
    scaled_future_value = ((future_value - min_val) / (max_val - min_val)) * (
        normalized_max - normalized_min
    ) + normalized_min
    return scaled_future_value[0] if len(future_value) > 0 else None


# Multi-page app setup
PAGES = {
    "Upload Dataset": page_upload_dataset,
    "Analysis and Prediction": page_analysis_and_prediction,
    "Future Data Points": page_future_data_points,
}


def main():
    st.set_page_config(
        page_title="Ozone Layer Depletion Analysis and Prediction",
        page_icon=":earth_americas:",
        layout="wide",
        initial_sidebar_state="auto",
    )

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()


if __name__ == "__main__":
    main()
