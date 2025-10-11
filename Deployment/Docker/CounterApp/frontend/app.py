import streamlit as st
import requests

# Set the title of the Streamlit app
st.title('Page View Counter')

# Define the backend API endpoint
# The hostname 'backend' is used here because that will be the service name in docker-compose
BACKEND_URL = 'http://backend:8000/'

try:
    # Make a request to the backend to get the current count
    response = requests.get(BACKEND_URL)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    count = data.get('count', 'N/A')

    # Display the count
    st.write("This page has been viewed:")
    st.header(count)

    st.info("Reload the page to increase the count!", icon="ℹ️")

except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to the backend: {e}")
    st.warning("Please make sure the backend service is running.")
