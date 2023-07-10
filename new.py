import streamlit as st # streamlit for web app
# import libraries
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting
import seaborn as sns # advanced plotting, statistics
import warnings # ignore warnings
warnings.filterwarnings('ignore') # filter warnings
df=pd.read_csv('https://raw.githubusercontent.com/aaqibqadeer/Hotel-booking-demand/master/hotel_bookings.csv') # read data
display(df.head()) # display first 5 rows
display('Number of rows and columns:', df.shape) # rows, columns
display('Columns:', df.columns) # columns 0 for canceled, 1 for not canceled
display(df.info()) # information about the data ( null values, data types)
df['reservation_status_date']=pd.to_datetime(df['reservation_status_date']) # convert to datetime
display(df.describe(include='object')) # describe categorical columns (unique, top, freq)
for col in df.describe(include='object').columns: # loop
    print(col) # print column name
    print(df[col].unique()) # print unique values
    print('-------------------') # print line
display(df.isnull().sum()) # check for missing values
df=df.drop(['company', 'agent'], axis=1) # drop columns
df.dropna(inplace=True) # drop missing values
display(df.isnull().sum()) # check for missing values
display(df.describe()) # summary statistics for numerical columns
plt.figure(figsize=(12,8)) # figure size
sns.boxplot(x='hotel', y='adr', data=df) # boxplot (price of room types per night and hotel type)
plt.title('Price of room types per night and hotel type', weight='bold') # title
plt.xlabel('Hotel', weight='bold') # x-axis label
plt.ylabel('Price in USD', weight='bold') # y-axis label
plt.savefig('adr.png') # save plot
plt.show() # show plot
df=df[df['adr']<5000] # remove outliers
cancelled_percentage=df['is_canceled'].value_counts( normalize=True) # percentage of canceled bookings
display(cancelled_percentage) # display percentage
plt.figure(figsize=(5,5)) # figure size
plt.title('Reservation Status Count') # title
np.random.seed(42) # random seed for reproducibility
plt.bar(['Not Cancelled', 'Cancelled'],df['is_canceled'].value_counts(), color=np.random.rand(3,),edgecolor='k',width=0.7) # barplot
plt.xlabel('Count') # x-axis label
plt.ylabel('Reservation Status') # y-axis label
plt.show() # show plot
plt.figure(figsize=(8,4)) # figure size
ax1=sns.countplot(x='hotel', hue='is_canceled', data=df, palette='rainbow') # countplot (hotel type and reservation status) hue is used to differentiate between the two reservation status
legend_labels, _=ax1.get_legend_handles_labels() # get legend labels
ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., labels=['Not Cancelled', 'Cancelled']) # legend
plt.title('Reservation Status for each Hotel Type', weight='bold') # title
plt.show() # show plot 
resert_hotel=df[df['hotel']=='Resort Hotel'] # resort hotel
resert_hotel['is_canceled'].value_counts(normalize=True) # percentage of canceled bookings
city_hotel=df[df['hotel']=='City Hotel'] # city hotel
city_hotel['is_canceled'].value_counts(normalize=True) # percentage of canceled bookings
resert_hotel=resert_hotel.groupby('reservation_status_date')[['adr']].mean() # average daily rate
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean() # average daily rate
plt.figure(figsize=(20,8)) # figure size
plt.plot(resert_hotel.index, resert_hotel['adr'], label='Resort Hotel', color='lime') # line plot
plt.plot(city_hotel.index, city_hotel['adr'], label='City Hotel', color='salmon') # line plot
plt.title('Average Daily Rate over Time', weight='bold') # title
plt.legend() # legend
plt.show() # show plot
df['month']=df['reservation_status_date'].dt.month # month column (reservation status date)
plt.figure(figsize=(16,8)) # figure size 
ax1=sns.countplot(x='month', hue='is_canceled', data=df, palette='bright') # countplot (month and reservation status) hue is used to differentiate between the two reservation status
legend_labels, _=ax1.get_legend_handles_labels() # get legend labels
ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., labels=['Not Cancelled', 'Cancelled']) # legend
plt.title('Reservation Status for each Month', weight='bold') # title
plt.show() # show plot
plt.figure(figsize=(15,8)) # figure size
sns.barplot(x='month', y='adr', data=df[df['is_canceled']==1].groupby('month')[['adr']].mean().reset_index(), palette='bright') # barplot (month and adr)
plt.title('Average Daily Rate for each Month', weight='bold') # title
plt.show() # show plot
cancelled_data=df[df['is_canceled']==1] # cancelled data
not_cancelled_data=df[df['is_canceled']==0] # not cancelled data
top_10_countries=cancelled_data['country'].value_counts()[:10] # top 10 countries  
plt.figure(figsize=(8,8)) # figure size
plt.pie(top_10_countries, labels=top_10_countries.index, autopct='%.2f%%') # pie chart (top 10 countries)
plt.title('Top 10 Countries', weight='bold') # title
plt.show() # show plot
display(df['market_segment'].value_counts()) # count of market segments
display(df['market_segment'].value_counts(normalize=True)) # percentage of market segments
display(cancelled_data['market_segment'].value_counts(normalize=True)) # percentage of market segments
cancelled_df_adr=cancelled_data.groupby('reservation_status_date')[['adr']].mean() # average daily rate
cancelled_df_adr.reset_index(inplace=True) # reset index
cancelled_df_adr.sort_values('reservation_status_date', inplace=True) # sort values
not_cancelled_df_adr=not_cancelled_data.groupby('reservation_status_date')[['adr']].mean() # average daily rate
not_cancelled_df_adr.reset_index(inplace=True) # reset index
not_cancelled_df_adr.sort_values('reservation_status_date', inplace=True) # sort values
plt.figure(figsize=(20,8)) # figure size
plt.title('Average Daily Rate over Time', weight='bold') # title
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label='Cancelled', color='lime') # line plot
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label='Not Cancelled', color='salmon') # line plot
plt.legend() # legend
plt.show() # show plot