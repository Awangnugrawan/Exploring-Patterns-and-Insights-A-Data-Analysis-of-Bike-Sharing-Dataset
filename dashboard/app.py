import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
hour = pd.read_csv(r'main_data.csv')

# Calculate the recency (R) for each customer
hour['datetime'] = pd.to_datetime(hour['datetime'])
max_datetime = hour['datetime'].max().to_pydatetime().date()
hour['recency'] = hour['datetime'].apply(lambda x: (max_datetime - x.date()).days)

# Calculate the frequency (F) for each customer
hour['frequency'] = hour['registered'] + hour['casual']

# Calculate the monetary value (M) for each customer
hour['monetary'] = hour['total_count']

# Select the relevant columns for the RFM analysis
rfm_data = hour[['recency', 'frequency', 'monetary', 'weekday']]

# Function to create the first plot
def plot_hourly_bike_sharing_by_season():
    fig, ax = plt.subplots(figsize=(20, 5))
    sns.pointplot(data=hour, x='hour', y='total_count', hue='season', ax=ax)
    ax.set(title='Hourly Bike Sharing Count by Season')
    st.pyplot(fig)

# Function to create the second plot
def plot_comparison_between_2011_and_2012():
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.set_style('white')
    sns.barplot(x='month', y='total_count', data=hour[['month', 'total_count', 'year']], hue='year', ax=ax)
    ax.set_title('Comparison of Bike Sharing Counts Between 2011 and 2012 by Month')
    st.pyplot(fig)

# Function to create the third plot
def plot_impact_of_weather_on_total_bike_rental():
    fig, ax = plt.subplots(figsize=(25, 8))
    sns.set_style('white')
    sns.barplot(x='month', y='total_count', data=hour[['month', 'total_count', 'weather']], hue='weather', ax=ax)
    ax.set_title('Impact of Weather on Total Bike Rental Count by Month')
    st.pyplot(fig)

# Function to create the fourth plot
def plot_last_transaction_day():
    last_transaction_day = rfm_data[rfm_data['recency'] == rfm_data['recency'].min()]['weekday'].values[0]
    plt.figure(figsize=(8, 6))
    sns.countplot(x='weekday', data=rfm_data.sort_values(by="recency", ascending=True).head(30), palette='viridis')
    plt.xlabel('Weekday')
    plt.ylabel('Number of Transactions')
    plt.title(f"Last Transaction Day: {last_transaction_day}", fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

# Function to create the fifth plot
def plot_most_frequency_day():
    freq_transaction_day = rfm_data[rfm_data['frequency'] == rfm_data['frequency'].max()]['weekday'].values[0]
    plt.figure(figsize=(8, 6))
    sns.countplot(x='weekday', data=rfm_data.sort_values(by="frequency", ascending=False).head(30), palette='viridis')
    plt.xlabel('Weekday')
    plt.ylabel('Number of Transactions')
    plt.title(f"Most Frequency: {freq_transaction_day}", fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

# Function to create the sixth plot
def plot_most_monetary_day():
    monetary_transaction_day = rfm_data[rfm_data['monetary'] == rfm_data['monetary'].max()]['weekday'].values[0]
    plt.figure(figsize=(8, 6))
    sns.countplot(x='weekday', data=rfm_data.sort_values(by="monetary", ascending=False).head(30), palette='viridis')
    plt.xlabel('Weekday')
    plt.ylabel('Number of Transactions')
    plt.title(f"Most Monetary: {monetary_transaction_day}", fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title='Bike Rental Dashboard', page_icon='🚲', layout='wide')
    st.title('Bike Rental Dashboard')
    st.header('Hourly Bike Sharing Count by Season')
    plot_hourly_bike_sharing_by_season()

    st.header('Comparison of Bike Sharing Counts Between 2011 and 2012 by Month')
    plot_comparison_between_2011_and_2012()

    st.header('Impact of Weather on Total Bike Rental Count by Month')
    plot_impact_of_weather_on_total_bike_rental()

    st.header('Last Transaction Day')
    plot_last_transaction_day()

    st.header('Most Frequency Day')
    plot_most_frequency_day()

    st.header('Most Monetary Day')
    plot_most_monetary_day()


if __name__ == '__main__':
    main()
  
