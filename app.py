import streamlit as st
import pandas as pd
import plotly.express as px


# Set page title
st.set_page_config(page_title="Poetry and Science Intersect", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

st.markdown(
    """,
    <style>
        .stApp {
            background-color: pink;
        }
    </style>
    """
    unsafe_allow_html=True
)
# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Tawana Doodles"
    field = "Engineering"
    institution = "University of Science"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")

    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)

        # Interactive Bar Chart
        st.subheader("Energy Levels of Experiments")
        fig = px.bar(physics_data, x="Experiment", y="Energy (MeV)", color="Energy (MeV)", 
                     title="Energy Levels of Different Physics Experiments")
        st.plotly_chart(fig)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)

        # Interactive Scatter Plot
        # Create a bar chart (without 'size')
        fig = px.bar(
            astronomy_data, 
            x="Celestial Object", 
            y="Brightness (Magnitude)", 
            title="Brightness of Celestial Objects",
            color="Celestial Object"  # Optional: Adds color differentiation
            )

        # Display chart in Streamlit
        st.plotly_chart(fig)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)

        # Interactive Line Chart for Temperature Trends
        st.subheader("Temperature Trends Across Cities")
        fig = px.scatter(weather_data, x="Humidity (%)", y="Temperature (°C)", color="City",
                      title="Temperature Changes Over Time")
        st.plotly_chart(fig)

elif menu == "Contact":
    st.header("Contact Information")
    name = "Tawana Doodles"
    email = "tawana.doodles@example.com"
    st.write(f"You can reach {name} at {email}.")
