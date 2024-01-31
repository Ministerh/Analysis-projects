import pandas as pd


def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts().to_list()

    average_age_of_men = df[df['sex'] == 'Male']['age'].mean()

    # percentage of people with bachelors degree
    percentage_bach_degree = round(df['education'].value_counts()['Bachelors']/df['education'].count() * 100, 1)

    # percenatge of people with advace education
    
    advance_edcuation = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich =round( advance_edcuation['salary'].value_counts()['>50K']/advance_edcuation['salary'].count() * 100, 1)
    
    #percenatge of people without advance education
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round(lower_education['salary'].value_counts()['>50K']/lower_education['salary'].count() * 100, 1)

    # What is the minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]

    rich_percentage =round(num_min_workers['salary'].value_counts()['>50K']/num_min_workers['salary'].count() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()

    # the percentage
    highest_earning_df = df[df['salary'] == '>50K']['native-country']
    highest_earning_country_percentage = round(highest_earning_df.value_counts().max()/highest_earning_df.count() * 100, 1)

    # the most popular work for those earning >50K 

    # popular_in_india = df[df['native-country'] == 'India']
    # high_salary =popular_in_india[popular_in_india['salary'] == '>50K']['occupation'].value_counts().idxmax()

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_of_men)
        print(f"Percentage with Bachelors degrees: {percentage_bach_degree}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_of_men,
        'percentage_bachelors': percentage_bach_degree,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }