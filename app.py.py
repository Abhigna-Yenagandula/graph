import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Timestamp': ['15-10-2023 08:00', '15-10-2023 08:01', '15-10-2023 08:02', '15-10-2023 08:03', '15-10-2023 08:04', '15-10-2023 08:05'],
    'Engine_RPM': [1500, 1600, 1550, 1580, 1520, 1510],
    'Vehicle_Speed': [60, 61, 62, 63, 64, 65],
    'Engine_Temperature': [95, 96, 97, 98, 99, 100],
    'Fuel_Level' : [75,76,77,78,79,80],
    'Oil_Pressure' : [40,41,42,43,44,45],
    'Coolant_Level': [80,81,82,83,84,85],
    'Brake_Pedal_Position': [30,31,32,33,34,35],
    'Steering_Angle':[15,16,17,18,19,20],
    'Acceleration_Pedal_Position': [50,51,52,53,54,55],
    'Transmission_Oil_Temperature':[70,71,72,73,74,75],
    'Fuel_Consumption_Rate' : [10,11,12,13,14,15],
    'Battery_Voltage':[13.5,13.6,13.7,13.8,13.9,14],
    'Engine_Load':[75,76,77,78,79,80],
}

df = pd.DataFrame(data)

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))




# Include other parameters on the graph lines
ax1.plot(df['Timestamp'], df['Vehicle_Speed'], color='g', marker='s', label='Vehicle Speed')
ax1.plot(df['Timestamp'], df['Engine_Temperature'], color='r', marker='^', label='Engine Temperature')
ax1.plot(df['Timestamp'], df['Fuel_Level'], color='r', marker='^', label='Fuel_Level')
ax1.plot(df['Timestamp'], df['Oil_Pressure'], color='b', marker='^', label='Oil_Pressure')
ax1.plot(df['Timestamp'], df['Coolant_Level'], color='y', marker='^', label='Coolant_Level')
ax1.plot(df['Timestamp'], df['Brake_Pedal_Position'], color='g', marker='^', label='Brake_Pedal_Position')
ax1.plot(df['Timestamp'], df['Steering_Angle'], color='r', marker='^', label='Steering_Angle')
ax1.plot(df['Timestamp'], df['Acceleration_Pedal_Position'], color='b', marker='^', label='Acceleration_Pedal_Position')
ax1.plot(df['Timestamp'], df['Transmission_Oil_Temperature'], color='y', marker='^', label='ETransmission_Oil_Temperature')
ax1.plot(df['Timestamp'], df['Fuel_Consumption_Rate'], color='g', marker='^', label='Fuel_Consumption_Rate')
ax1.plot(df['Timestamp'], df['Battery_Voltage'], color='r', marker='^', label='Battery_Voltage')
ax1.plot(df['Timestamp'], df['Engine_Load'], color='b', marker='^', label='Engine_Load')
# Add other parameters as needed

# Label the axes and add a legend
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Engine_RPM')
ax1.set_title('Line Chart with Timestamp on X-axis')
ax1.legend()

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()