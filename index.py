python
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
public_transport_data = pd.read_csv('public_transport_usage.csv')
real_estate_data = pd.read_excel('real_estate_transactions.xlsx')
healthcare_data = pd.read_json('healthcare_utilization.json')
energy_data = pd.read_excel('water_power_production.xlsx')

# Analyze Public Transport Data
bus_usage = public_transport_data.groupby('route')['passengers'].sum()
bus_usage.plot(kind='bar', title='Bus Usage by Route')
plt.xlabel('Route')
plt.ylabel('Number of Passengers')
plt.show()

# Analyze Real Estate Data
median_prices = real_estate_data.groupby('property_type')['sale_price'].median()
median_prices.plot(kind='barh', title='Median Sale Prices by Property Type')
plt.xlabel('Median Sale Price')
plt.show()

# Analyze Healthcare Data
service_usage = healthcare_data.groupby('service_type')['patient_count'].sum()
service_usage.plot(kind='pie', title='Healthcare Service Usage')
plt.ylabel('')
plt.show()

# Analyze Energy Data
production_capacity = energy_data.groupby('company')['daily_capacity'].sum()
production_capacity.plot(kind='bar', title='Daily Production Capacity by Company')
plt.xlabel('Company')
plt.ylabel('Daily Capacity (Million Cubic Meters)')
plt.show()

