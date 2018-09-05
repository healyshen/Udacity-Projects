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
    city = ""
    city = input("Please provide a city among: chicago, new york city, washington!\n").lower()
    city_valid = False

    while not city_valid:
      if city not in ("chicago", "new york city", "washington"):
        city = input("Please try again: chicago, new york city, washington\n")
      else:
        city_valid = True

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    month = input("Please provide a month for which you would like to analyze among between january and june; if you would like to analyze all months, please input the word, all!\n").lower()
    month_valid = False

    while not month_valid:
      if month not in ("all", "january", "february", "march", "april", "may", "june"):
        month = input("Please try again.\n")
      else:
        month_valid = True

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    day = input("Please provide a day of the week for which you would like to analyze; if you would like to analyze all days, please input the word, all!\n").lower()
    day_valid = False

    while not day_valid:
      if day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
        day = input("Please try again.\n")
      else:
        day_valid = True

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    return df


    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day_of_week != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_of_week.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    mode_month = df['month'].mode()[0]
    print("\nThe most popular month is: ",mode_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    mode_day = df['day'].mode()[0]
    print("\nThe most popular day is: ",mode_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mode_hour= df['hour'].mode()[0]
    print("\nThe most popular hour is: ",mode_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start = df['Start Station'].mode()[0]
    print("\nThe most popular start station is: ",mode_start)

    # TO DO: display most commonly used end station
    mode_end = df['End Station'].mode()[0]
    print("\nThe most popular end station is: ",mode_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" combined with "+df['End Station']
    mode_combination = df['combination'].mode()[0]
    print("\nThe most popular combination of start and end stations is: ",mode_combination)    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df["Trip Duration"].sum()
    print("\nThe total trip duration was",total_duration)
    
    # TO DO: display mean travel time
    mean_duration=df["Trip Duration"].mean()
    print("\nThe average trip duration was",mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user=df['User Type'].value_counts()
    print("The user type statistics are: ",user)

    # TO DO: Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print("The gender statistics are: ",gender)
    except KeyError:
        print("Gender statistics are not available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        common=df['Birth Year'].mode()
        print('The earliest birth year is {}, the most recent birth year is {}, and the most common birth year is {}'.format(earliest, recent, common))
    except KeyError:
        print("Year of birth statistics are not available for Washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
