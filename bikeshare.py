import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_city_list = ["chicago", "new york city", "washington"]
valid_month_list = ["january", "february", "march", "april", 
                    "may", "june", "all"]
valid_day_of_week_list = ["sunday", "monday", "tuesday", "wednesday", 
                          "thursday", "friday", "saturday", "all"]
month_name_dict = {1: "January", 
                   2: "February", 
                   3: "March", 
                   4: "April", 
                   5: "May",
                   6: "June"}

def get_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city = input("Which city (Chicago, New York City or Washington) would you like to explore? ").lower()
    while city not in valid_city_list:
        city = input("Please enter one of the following city names verbatim: Chicago, New York City or Washington. " ).lower()
    print('-'*40)
    return city

def get_month():
    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    # get user input for month (all, january, february, ... , june)
    month = input("Which month (january thru june) would you like to explore? Type the full name of the month--no abbreviations--or type 'all' (no quotation marks) to get info for all months) ").lower()
    while month not in valid_month_list:
        month = input("Please enter a valid month (january thru june, full name, no abbreviations) or 'all' (no quotation marks) for info on all months ").lower()
    return month
def get_day():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week would you like to explore? Type the full name of the day--no abbreviations--or type 'all' (no quotation marks) to get info for all days of the week) ").lower()
    while day not in valid_day_of_week_list:
        day = input("Please enter a valid day (full name, no abbreviations) or 'all' (no quotation marks) for info on all days ").lower()
    return day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    print(city)
    # add city name as a column
    df['city'] = city.lower()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {}.".format(month_name_dict[df.month.mode()[0]]))


    # display the most common day of week
    print("The most common day of the week is: {}.".format(df.day_of_week.mode()[0]))


    # display the most common start hour
    print("The most common start hour is: {}:00.".format(df['Start Time'].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: {}.".format(df["Start Station"].mode()[0]))
    

    # display most commonly used end station
    print("The most commonly used end station is: {}.".format(df["End Station"].mode()[0]))


    # display most frequent combination of start station and end station trip
    df["Start End Stations"] = "From " + df["Start Station"] + " to " + df["End Station"]
    print("The most frequent combination of start station and end station is: {}.".format(df["Start End Stations"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Trip Duration: {0:,.2f} minutes".format(df["Trip Duration"].sum()/60))


    # display mean travel time
    print("Mean Trip Duration: {0:,.2f} minutes".format(df["Trip Duration"].mean()/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of User Types: {}".format(df["User Type"].value_counts()))

    print(df['city'][0])
#     if df['city'][0] != 'washington':
#         # Display counts of gender
#         print("\nCount of Gender: {}".format(df["Gender"].value_counts()))
#         # Display earliest, most recent, and most common year of birth
#         print("\nEarliest birth year: {}.".format(df["Birth Year"].min()))
#         print("Most recent birth year: {}.".format(df["Birth Year"].max()))
#         print("Most common birth year: {}.".format(df["Birth Year"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 0
    while True:
        see_raw_data_yes_or_no = input('Do you want to see the raw data? Enter yes or no.\n')
        if see_raw_data_yes_or_no.lower() != 'yes':
            break
        print(df.iloc[i:i+5])
        i+=5
def main():
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
