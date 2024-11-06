import socket

# Function to convert temperature
def convert_temperature(value, scale):
    if scale == 'C':
        # Celsius to Fahrenheit and Kelvin
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return f"{fahrenheit:.2f} F, {kelvin:.2f} K"
    elif scale == 'F':
        # Fahrenheit to Celsius and Kelvin
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return f"{celsius:.2f} C, {kelvin:.2f} K"
    elif scale == 'K':
        # Kelvin to Celsius and Fahrenheit
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return f"{celsius:.2f} C, {fahrenheit:.2f} F"
    else:
        return "Invalid scale"

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8099))
    server_socket.listen(5)
    print("Server is listening on port 8090...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        temp, scale = data.split()

        # Convert the temperature to float
        temp = float(temp)
        
        # Convert the temperature based on the scale provided
        converted_temp = convert_temperature(temp, scale)

        # Send the converted temperature back to the client
        client_socket.send(f"Converted temperature: {converted_temp}".encode('utf-8'))

        # Close the client connection
        client_socket.close()

# Run the server
if __name__ == "__main__":
    start_server()
