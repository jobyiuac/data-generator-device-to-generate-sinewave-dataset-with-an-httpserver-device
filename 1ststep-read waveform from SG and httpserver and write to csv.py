import numpy as np
import matplotlib.pyplot as plt
import http.client

# Define the IP address and path for HTTP communication
host = "192.168.1.102"
path = "/rpc/pot1/read"

# Function to read voltage from ADC
def read_current_voltage():
    # Establish a connection to the specified host and path
    connection = http.client.HTTPConnection(host)
    connection.request("GET", path)
    
    # Get the response from the server
    response = connection.getresponse()
    
    # Read the response, convert it to a float, and format it to three decimal places
    x1 = response.read().decode()
    x = float(x1)
    x = float("{:.3f}".format(x))
    
    # Close the connection and return the voltage value
    connection.close()
    return x

# Initialize an empty list to store test signal values
Xtest = []

# Loop to generate test signal values by reading voltage from the ADC
for r in range(0, 110, 1):
    voltage = (read_current_voltage() - 0.5)
    Xtest.append(voltage)  # Modified earlier function to get values in the range -1 to +1

# Plot the generated test signal
plt.plot(Xtest)


# Write the test signal values to a CSV file
writebuffer = Xtest
with open("sinewave.csv", "w") as file:
    for value in writebuffer:
        file.write(str((value + 1) / 2.0) + "\n")  # Scale values to the range 0 to 1
plt.show()
