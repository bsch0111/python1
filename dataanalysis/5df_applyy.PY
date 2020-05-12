import pandas as pd

data_list = [{'all day' : '2020-03-02'},
             {'all day' : '2019-04-07'},
             {'all day' : '2020-04-29'}
             ]
df = pd.DataFrame(data_list,columns=['all day'])

def extract_year(all_day):
    return all_day.split('-')[0]

#하나의 매개변수를 받는 apply
df['year'] = df['all day'].apply(extract_year)

def get_age(year, current_year):
    return current_year - int(year)

#두개의 매개변수를 받는 apply
df['age'] = df['year'].apply(get_age, current_year = 2020)

def intro(age, prefix, suffix):
    return prefix + str(age) + suffix

#세개의 매개변수를 받는 apply
df['intro1'] = df['age'].apply(get_intro, prefix='we met', suffix='.')

#열을 매개변수로 받는 apply
def get_intro2(row):
    return "we meet" + str(row['all day']) + '. and year is ' + str(row['year'])

df['intro2'] = df.apply(get_intro2, axis=1)
