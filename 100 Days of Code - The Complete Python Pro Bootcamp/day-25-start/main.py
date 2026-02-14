import csv
import pandas

# with open('weather_data.csv') as weather_data:
#     # data = weather_data.readlines()
#     temps = []
#     data = csv.reader(weather_data)
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temps.append(int(row[1]))

    # print(temps)

# new_data = pandas.read_csv('weather_data.csv')
# getting columns
# print(new_data['temp'])
# or new_data.temp

# Pandas major data types are data frames and series
# you can use to_dict() and to_list() to convert the, to standard python dictionary and list

# get average
# temps_list = new_data['temp'].to_list()
# print(temps_list)
# temps_sum = 0
# for t in temps_list:
#     temps_sum += t
# avg_temp = temps_sum/len(temps_list)
# print(avg_temp)
#
# print(new_data['temp'].mean())
# print(new_data['temp'].max())


# getting a single row
# pass a condition

# print(new_data[new_data.temp == 24])
# print(new_data[new_data.day == 'Monday'])

# building a dataframe from scratch
# keys dict keys become table/csv headers
# my_dict = {
#     'students': ['amy', 'james', 'angela'],
#     'scores': [76, 56, 65]
# }
#
# data_df = pandas.DataFrame(my_dict)
# print(data_df)
# data_df.to_csv('new_data.csv')

raw_data = pandas.read_csv('squirrel_data.csv')
fur_list = (raw_data['Primary Fur Color'].dropna().to_list())
count_obj = {}

for fur_color in fur_list:
    if fur_color:
        count_obj[fur_color] = count_obj.get(fur_color, 0) + 1

df_transform = {
    'Fur color':[],
    'Count': []
}

for key, value in count_obj.items():
    df_transform['Fur color'].append(key)
    df_transform['Count'].append(value)

df = (pandas.DataFrame(df_transform))
df.to_csv('squirrel_count.csv ')