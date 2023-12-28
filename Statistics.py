import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as num
import matplotlib as mpl
sys.path

# Read/Write Excel Files
data = pd.read_excel('/Users/yanthemac/Downloads/Data.xlsx')

# City
city = input("Give a city (in all caps): ")
City = data.query(f'lokaliteit == {city}')

# City Periods
City_q1 = City.query('periode == "Q1"')
City_q2 = City.query('periode == "Q2"')
City_q3 = City.query('periode == "Q3"')
City_q4 = City.query('periode == "Q4"')


# City Median
City_q1_median = City_q1[['mediaan']]
City_q2_median = City_q2[['mediaan']]
City_q3_median = City_q3[['mediaan']]
City_q4_median = City_q4[['mediaan']]

# City Years
City_q1_jaar = City_q1[['jaar']]
City_q2_jaar = City_q2[['jaar']]
City_q3_jaar = City_q3[['jaar']]
City_q4_jaar = City_q4[['jaar']]


plt.plot(City_q1_jaar, City_q1_median, label="Q1")
plt.plot(City_q2_jaar, City_q2_median, label="Q2")
plt.plot(City_q3_jaar, City_q3_median, label="Q3")
plt.plot(City_q4_jaar, City_q4_median, label="Q4")
plt.title(f"{city} House Prices")
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend
plt.show()
