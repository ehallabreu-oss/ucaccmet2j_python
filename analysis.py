import json

with open('ucaccmet2j_python/precipitation.json') as file:
    data = json.load(file)

def get_data(station_code):
    station = []
    for dict in data: # 
        if dict['station'] == station_code:
            station.append(dict)

    monthly_precipitation = {}
    yearly_precipitation = {}

    for dict in station: 
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

    relative_precipitation = []
    for year in total_yearly_precipitation:
        for month in total_monthly_percipitation:
            relative_month = month / year
            relative_precipitation.append(relative_month)

    return total_monthly_percipitation, total_yearly_precipitation, relative_precipitation

seatle_code = 'GHCND:US1WAKG0038'
cincinnati_code = 'GHCND:USW00093814'
maui_code = 'GHCND:USC00513317'
san_diego_code = 'GHCND:US1CASD0032'

seatle_monthly, seatle_yearly, seatle_relative = get_data(seatle_code)
cincinnati_monthly, cincinnati_yearly, cincinnati_relative = get_data(cincinnati_code)
maui_monthly, maui_yearly, maui_relative = get_data(maui_code)
san_diego_monthly, san_diego_yearly, san_diego_relative = get_data(san_diego_code)


precipitation = {
    'Seatle' : {
        'station': 'GHCND:US1WAKG0038',
        'sate': 'WA',
        'total_monthly_precipitation': seatle_monthly,
        'total_yearly_precipitation' : seatle_yearly,
        'relative_monthtly_precipitation' : seatle_relative
    },
    'Cincinnati': {
        'station': 'GHCND:USW00093814',
        'sate': 'OH',
        'total_monthly_precipitation': cincinnati_monthly,
        'total_yearly_precipitation' : cincinnati_yearly,
        'relative_monthtly_precipitation' : cincinnati_relative
    },
    'Maui': {
        'station': 'GHCND:USC00513317',
        'sate': 'HI',
        'total_monthly_precipitation': maui_monthly,
        'total_yearly_precipitation' : maui_yearly,
        'relative_monthtly_precipitation' : maui_relative
    },
    'San Diego': {
        'station': 'GHCND:US1CASD0032',
        'sate': 'CA',
        'total_monthly_precipitation': san_diego_monthly,
        'total_yearly_precipitation' : san_diego_yearly,
        'relative_monthtly_precipitation' : san_diego_relative
    },
}


with open('ucaccmet2j_python/results_precipitation.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation, file, indent=4)
