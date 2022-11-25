import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#created the function get_filters() to filter out the given dataset
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('insert the city by which you want to filter. \n').lower()
    while city not in CITY_DATA:
        city = input('insert a valid city by which you want to filter. \n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('insert the month by which you want to filter, or all. \n').lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december','all']
    while month not in months:
        month=input('insert a valid month by which you want to filter. \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('insert the day by which you want to filter, or all. \n').lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while day not in days:
        day=input('insert a valid day by which you want to filter. \n').lower()

    print('-'*40)
    return city, month, day

#created the function load_data to load the data
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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december','all']
        month=months.index(month)+1
        df=df[df['month']==month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

#created the function time_stats(df) to analyze the data related to time.
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month=df['month'].mode()[0]
    print(f'The most common month is: {month}')

    # TO DO: display the most common day of week
    day=df['day_of_week'].mode()[0]
    print(f'the most common day of week is: {day}')

    # TO DO: display the most common start hour
    hour=df['hour'].mode()[0]
    print(f'the most common start hour is: {hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#created the function station_stats(df) that analyzes the data related to station
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstation=df['Start Station'].mode()[0]
    print(f'most commonly used start station is: {startstation}')

    # TO DO: display most commonly used end station
    end=df['End Station'].mode()[0]
    print(f'most commonly used end station is: {end}')

    # TO DO: display most frequent combination of start station and end station trip
    combined= df['Start Station'] + ' --> ' +df['End Station'] 
    combined=combined.mode()[0]
    print(f'most frequent combination of start station and end station trip is: {combined}' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#created the function trip_duration_stats(df) that analyzes the data related to trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total=df['Trip Duration'].sum()
    print(f'total travel time is: {total}sec')

    # TO DO: display mean travel time
    mean=df['Trip Duration'].mean()
    print(f'mean travel time is: {mean}sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
#created the function user_stats(df) that analyzes the data related to user
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype=df['User Type'].value_counts()
    print(f'counts of the user types: \n {usertype}')

    # TO DO: Display counts of gender
    if city != 'washington':
        gender=df['Gender'].value_counts()
        print(f'counts of the user gender: \n {gender}')

    # TO DO: Display earliest, most recent, and most common year of birth
        early=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        com=df['Birth Year'].mode()[0]
        print(f'earliest, most recent, and most common year of birth are : {early} , {recent} , {com}')
    else: print(' \n Chicago dataset does not have Gender nor Birth year data yet!.' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#some extra additions for command message
def choice(msg, choices=('y', 'n')):
    """Return a valid input from the user given an array of possible answers.
    """

    while True:
        choice = input(msg).lower().strip()
        # terminate the program if the input is end
        if choice == 'end':
            raise SystemExit
        # triggers if the input has only one name
        elif ',' not in choice:
            if choice in choices:
                break
        # triggers if the input has more than one name
        elif ',' in choice:
            choice = [i.strip().lower() for i in choice.split(',')]
            if list(filter(lambda x: x in choices, choice)) == choice:
                break

        msg = ("\nSomething is not right. Please mind the formatting and "
                  "be sure to enter a valid option:\n>")

    return choice

#ask user whether they want to see raw data or not
def raw_data(df, point):
    """Display 5 lines of sorted raw data each time."""
    print("\nYou opted to view raw data.")
    # this variable holds where the user last stopped
    if point > 0:
        last_point = choice("\n Would you like to continue from where you stopped last time? \n [y] Yes\n [n] No\n\n>")
        if last_point == 'n':
            point = 0
            
    # sort data by column
    if point == 0:
        show_df = choice( "\n What would you like to see first \n Hit Enter to view All.\n \n [st] Start Time\n [et] End Time\n[td] Trip Duration\n [ss] Start Station\n [es] End Station\n\n>", ('st', 'et', 'td', 'ss', 'es', '')) 
        if show_df == 'st':
            df = df.sort_values(['Start Time'])
        elif show_df == 'et':
            df = df.sort_values(['End Time'])
        elif show_df == 'td':
            df = df.sort_values(['Trip Duration'])
        elif show_df == 'ss':
            df = df.sort_values(['Start Station'])
        elif show_df == 'es':
            df = df.sort_values(['End Station'])
        elif show_df == '':
            pass
    # each loop displays 5 lines of raw data
    while True:
        for i in range(point, len(df.index)):
            print(df.iloc[point:point+5].to_string()+"\n")
            point += 5

            if choice("Do you want to keep printing the raw data?"
                      "\n\n[y]Yes\n[n]No\n\n>") == 'y':
                continue
            else:
                break
        break
    return point

#main function to run on the command line
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        point= 0
        while True:
            select_data = choice("\nKindly select the information you would like to show .\n\n [ts] Time Stats\n [ss] Station Stats\n [tds] Trip Duration Stats\n [us] User Stats\n [rd] Display Raw Data\n[r] Restart\n\n>", ('ts', 'ss', 'tds', 'us', 'rd', 'r'))
            if select_data == 'ts':
                time_stats(df)
            elif select_data == 'ss':
                station_stats(df)
            elif select_data == 'tds':
                trip_duration_stats(df)
            elif select_data == 'us':
                user_stats(df, city)
            elif select_data == 'rd':
                point = raw_data(df, point)
            elif select_data == 'r':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
