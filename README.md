# Bike Rental Dashboard

Data Set
=========================================
Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 

[CERTIFICATE ANALISI DATA DENGAN PYTHON](https://www.dicoding.com/certificates/ERZRGJ22NPYV)

## Setup environment
`conda create --name main-ds python=3.9.6`

`conda activate main-ds`

`pip install numpy pandas  matplotlib seaborn jupyter streamlit babel`

## Run steamlit app
`streamlit run app.py`
