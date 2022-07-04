import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago':'chicago.csv',
             'new york city':'new_york_city.csv',
             'washington':'new_york_city.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyse.

    Returns:
         city = input("choose a city name (chicago, new york city, washington):").lower()  (str) city - name of the city
         (str) month - name of the month to filter by, or "all" to apply no month filter
         (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data')
    city = input("choose a city name out of the options listed from the dataset (chicago, new york city, washington):").lower()
    while city not in CITY_DATA.keys():
      print('Please enter a valid city available from the dataset')
      city = input('choose a city name(s) from the dataset (chicago, new york city, washington):')

    months = ['january','february','march','april','may','june','all']
    while True:
            month = input("Choose a month or 'all' from the dataset to continue (all, january, february, march, april, may, june):").lower()
            if month in months:
                break
            else:
                print('invalid input, please choose from the listed options')

    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    while True:
            day = input("Please select a day of the week you would like to analyse:").lower()
            if day in days:
                 break
            else:
                  print('invalid input')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    loads data for the specified city and filters by month and day if applicable

    Args
    ----------
    city : string
        name of the city to analyse.
    month : string
        name of the month to filter by, or "all" to apply no month filter.
    day : string
        name of the day to filter by, or "all" to apply no month filter.

    Returns
    -------
    df - Pandas DataFrame containing city data filtered by month and day.

    """
    df = pd.read_csv(CITY_DATA[city])

    df['start time'] = pd.to_datetime(df['start time'])

    df['month'] = df['start time'].dt.month
    df['day of the week'] = df['start time'].dt.weekday_name
    df['start hour'] = df['start time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day of the week'] == day.title()]


        return df

def time_stats(df):
    """display statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel....\n')
    start_time = time.time()

    print('the most commmon month is : {}'.format(df['month'].mode()[0]))

    print('the most common day is : {}'.format(df['day of the week'].mode()[0]))

    print('the most common hour is : {}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Dsplays statistics on the most popular stations and trips."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most common start station is : {}'.format(df['Start Station'].mode()[0]))

    print('The most common end station is :{}'.format(df['End Station'].mode()[0]))


    df['route']-df['Start Station']+','+df['End Station']


    df['route']-df['Start Station']+','+df['End Station']


    most_popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print ('The most common route is:{}'.format(df['route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total travel time:',(df['Trip Duration'].sum()).round())

    print('Average Travel time:',df(['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCaculating User Stats...\n')
    start_time = time.time()

    print(df['User typer'].value_counts().to_frame())



    pd.set_option('display.max_columns',200)

    if city != 'washington':
        print(df['gender'].value_counts().to_frame())

        print('The most common year of birth is :',int(df['Birth Year'].mode()[0]))
        print('The most recent year of birth is :',int(df['Birth Year'].max()))
        print('The earliest year of birth is :',int(df['Birth Year'].min()))
    else:
        print('There is no data for this city')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    """Prompt the user as to whether or not they want to display the raw data"""
    print('\nThe Raw Data is available should you want to view it... \n')

    index=0
    user_input = input('would you like to display 5 rows of data?, please type yes or no').lower()
    if  user_input not in ['yes' or 'no']:
        print('invalid selection, please type yes or no')
        user_input=input('would you like to display 5 rows of data?, please type yes or no').lower()
    elif user_input != 'yes':
        print('Thank you')

    else:
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index += 5
            user_input = input('would you like to display more than 5 rows of raw data?').lower()
            if user_input != 'yes':
                print('Thank you')
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? enter yes or no.\n')
        if restart.lower() != 'yes':
         print('thank you')
         break

if __name__ == "__main__":
	main()
