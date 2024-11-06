# client.py
import socket
import streamlit as st

# Function to send temperature data to the server
def send_temperature(value, scale):
    try:
        # Establish connection with the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 8099))
        
        # Send temperature data
        client_socket.send(f"{value} {scale}".encode('utf-8'))

        # Receive the converted temperature from the server
        response = client_socket.recv(1024).decode('utf-8')
        client_socket.close()
        return response
    except ConnectionRefusedError:
        return "Server is not running. Please start the server and try again."

# Streamlit UI
st.title("Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin")

# Input fields for temperature and scale
temperature = st.number_input("Enter the temperature value:", format="%.2f")
scale = st.selectbox("Select the scale of the input temperature:", ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"])

# Map scale selection to short form
scale_dict = {
    "Celsius (C)": "C",
    "Fahrenheit (F)": "F",
    "Kelvin (K)": "K"
}
selected_scale = scale_dict[scale]

# Convert button
if st.button("Convert Temperature"):
    result = send_temperature(temperature, selected_scale)
    st.success(result)
