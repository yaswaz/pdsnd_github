import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_is_not_valid = True
    while city_is_not_valid:
        try:
            city = input('Will you like to see the data for Chicago, New York City or Washington?: ').lower().strip()
            if CITY_DATA[city]:
                city_is_not_valid = False
        except:
            print('City entry is not valid')

     # TO DO: get user input for month (all, january, february, ... , june)
    month_is_not_valid = True
    while month_is_not_valid:
        try:

            months = {'january': '1', 'february': '2', 'march': '3', 'april': '4', 'may': '5', 'june': '6', 'all': '7'}
            month = input('What Month Will You Like To Filter By (January to June Only)? Type "all" for no month filter: ').lower().strip()

            if months[month]:
                month_is_not_valid = False
        except:
            print('Your month input is not valid')

 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_is_not_valid = True
    while day_is_not_valid:
        try:
            days = {'monday': '1', 'tuesday': '2', 'wednesday': '3', 'thursday': '4', 'friday': '5', 'saturday': '6', 'sunday': '7', 'all':                    '8'}
            day = input('What Day Of The Week Will You Like To Filter By? Type "all" for no filter: ').lower().strip()

            if days[day]:
                day_is_not_valid = False
        except:
            print('Your day input is not valid')



    print('-'*40)
    return city, month, day

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    count = df['day_of_week'].value_counts()[0]
    print('The Most Popular Day of the Week is {}, with a Count of {}'.format(popular_day_of_week, count))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    pop_count = df['hour'].value_counts()[0]
    print('The Most Popular Start Hour is {}, with a Count of {}'.format(popular_hour, pop_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    pop_start_station_count = df['Start Station'].value_counts()[0]
    print('The Most Popular Start Start Station is {}, with a Count of {}'.format(popular_start_station, pop_start_station_count))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    pop_end_station_count = df['End Station'].value_counts()[0]
    print('The Most Popular End Station is {}, with a Count of {}'.format(popular_end_station, pop_end_station_count))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination_station = df['Start Station' and 'End Station'].mode()[0]
    pop_combination_count = df['Start Station' and 'End Station'].value_counts()[0]
    print('The Most Frequent Combination is {}, with a Count of {}'.format(popular_combination_station, pop_combination_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types Count:', user_types)

    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print('Gender Type Count:', gender_type)
    except:
        print('No Entries for Gender')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print('Earliest Birth Year:', earliest_birth)

        latest_birth = df['Birth Year'].max()
        print('Latest Birth Year:', latest_birth)

        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', most_common_birth_year)
    except:
        print('No Entries for Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Prompts user to if they want to see raw data, displays data if the answer is 'yes',
    and continues the prompts and displays until the user says 'no'"""

    while True:
        raw_data = input('Would you like to see first 5 rows raw data? Enter yes or no?: ')
        row_start = 0
        row_end = 5
        if raw_data.lower() == 'yes':
            print(df[row_start : row_end])
        elif raw_data.lower() == 'no':
            break
        else:
            print('Entry not valid! Please enter Yes or No')
        while row_end < 300002:
            raw_data = input('Would you like to see more raw data? Enter yes or no?: ')
            if raw_data.lower() == 'yes':
                row_start += 5
                row_end += 5
                print(df[row_start : row_end])
            elif raw_data.lower() == 'no':
                break
            else:
                print('Entry not valid! Please enter Yes or No')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
