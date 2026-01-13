import json

with open('ucaccmet2j_python/precipitation.json') as file:
    data = json.load(file)

seatle = []

for dict in data: # 
    if dict['station'] == 'GHCND:US1WAKG0038':
        seatle.append(dict)

monthly_precipitation = {}
yearly_precipitation = {}

for dict in seatle: 
    date = dict['date']
    year = date.split('-')[0]
    month = date.split('-')[1]
    
    if month in monthly_precipitation:
        monthly_precipitation[month] += dict['value']
    else:
        monthly_precipitation[month] = dict['value']

    if year in yearly_precipitation:
        yearly_precipitation[year] += dict['value']
    else:
        yearly_precipitation[year] = dict['value']

total_monthly_percipitation = []
for key in monthly_precipitation:
    total_monthly_percipitation.append(monthly_precipitation[key])

total_yearly_precipitation = []
for key in yearly_precipitation:
    total_yearly_precipitation.append(yearly_precipitation[key])

print(len(total_yearly_precipitation))
print(total_yearly_precipitation)

relative_precipitation = []
for year in total_yearly_precipitation:
    for month in total_monthly_percipitation:
        relative_month = month / year
        relative_precipitation.append(relative_month)

print(relative_precipitation)

# data = {
#     'Seatle' : {
#         'station': 'GHCND:US1WAKG0038',
#         'total_monthly_percipitation': total_monthly_percipitation,


#     }
# }

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
