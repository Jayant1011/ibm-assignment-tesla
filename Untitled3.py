#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install yfinance


# In[4]:


import yfinance as yf

# Define the ticker symbol
ticker_symbol = 'TSLA'

# Download the data
tesla_data = yf.download(ticker_symbol, start='2022-01-01', end='2022-12-31')

# Display the first few rows of the data
print(tesla_data.head())


# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table containing revenue data
    revenue_table = soup.find('table', {'class': 'historical_data_table'})
    
    # Extract the table headers
    headers = [header.text for header in revenue_table.find_all('th')]
    
    # Extract the revenue data
    data = []
    for row in revenue_table.find_all('tr')[1:]:
        row_data = [cell.text for cell in row.find_all('td')]
        data.append(row_data)
    
    # Create a DataFrame
    tesla_revenue = pd.DataFrame(data, columns=headers)
    
    # Display the last five rows of the dataframe
    print(tesla_revenue.tail())
else:
    print('Failed to retrieve data. Status code:', response.status_code)


# In[6]:


# Define the ticker symbol
gme_ticker_symbol = 'GME'

# Download the data
gme_data = yf.download(gme_ticker_symbol, start='2022-01-01', end='2022-12-31')

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows of the data
print(gme_data.head())

# Save the dataframe to a CSV file
gme_data.to_csv('gme_stock_data.csv', index=False)


# In[7]:


import matplotlib.pyplot as plt

# Plot Tesla stock data
plt.plot(tesla_data['Date'], tesla_data['Close'])
plt.title('Tesla Stock Data')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[8]:


# Plot GameStop stock data
plt.plot(gme_data['Date'], gme_data['Close'])
plt.title('GameStop Stock Data')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[ ]:




