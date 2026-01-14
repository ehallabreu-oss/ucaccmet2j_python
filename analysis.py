import json

# loading data
with open('precipitation.json') as file:
    data = json.load(file)

# function to get total monthly precipitation, yearly precipitation and relative monthly precipitation given the station
def get_data(station_code):
    
    # filter for station
    station = []
    for dict in data: # 
        if dict['station'] == station_code:
            station.append(dict)

    monthly_precipitation = {}
    total_yearly_precipitation = 0
    
    # compute total monthly precipitation and total yearly precipitation
    for dict in station: 
        date = dict['date']
        month = date.split('-')[1]
        
        if month in monthly_precipitation:
            monthly_precipitation[month] += dict['value']
        else:
            monthly_precipitation[month] = dict['value']

        total_yearly_precipitation += dict['value']

    total_monthly_percipitation = list(monthly_precipitation.values())

    relative_precipitation = []
    
    # compute relative precipitation
    for month in total_monthly_percipitation:
        relative_month = month / total_yearly_precipitation
        relative_precipitation.append(relative_month)

    return total_monthly_percipitation, total_yearly_precipitation, relative_precipitation

seatle_code = 'GHCND:US1WAKG0038'
cincinnati_code = 'GHCND:USW00093814'
maui_code = 'GHCND:USC00513317'
san_diego_code = 'GHCND:US1CASD0032'

# call the function for each station
seatle_monthly, seatle_yearly, seatle_relative = get_data(seatle_code)
cincinnati_monthly, cincinnati_yearly, cincinnati_relative = get_data(cincinnati_code)
maui_monthly, maui_yearly, maui_relative = get_data(maui_code)
san_diego_monthly, san_diego_yearly, san_diego_relative = get_data(san_diego_code)

# compute relative yearly precipitation
seatle_relative_yearly = seatle_yearly / (seatle_yearly + cincinnati_yearly + maui_yearly + san_diego_yearly)
cincinnati_relative_yearly = cincinnati_yearly / (seatle_yearly + cincinnati_yearly + maui_yearly + san_diego_yearly)
maui_relative_yearly = maui_yearly / (seatle_yearly + cincinnati_yearly + maui_yearly + san_diego_yearly)
san_diego_relative_yearly = san_diego_yearly / (seatle_yearly + cincinnati_yearly + maui_yearly + san_diego_yearly)

# save to a json file
precipitation = {
    'Cincinnati': {
        'station': 'GHCND:USW00093814',
        'sate': 'OH',
        'total_monthly_precipitation': cincinnati_monthly,
        'total_yearly_precipitation' : cincinnati_yearly,
        'relative_monthly_precipitation' : cincinnati_relative,
        'relative_yearly_precipitation' : cincinnati_relative_yearly
    },
    'Seattle' : {
        'station': 'GHCND:US1WAKG0038',
        'sate': 'WA',
        'total_monthly_precipitation': seatle_monthly,
        'total_yearly_precipitation' : seatle_yearly,
        'relative_monthly_precipitation' : seatle_relative,
        'relative_yearly_precipitation' : seatle_relative_yearly

    },
    'Maui': {
        'station': 'GHCND:USC00513317',
        'sate': 'HI',
        'total_monthly_precipitation': maui_monthly,
        'total_yearly_precipitation' : maui_yearly,
        'relative_monthly_precipitation' : maui_relative,
        'relative_yearly_precipitation' : maui_relative_yearly

    },
    'San Diego': {
        'station': 'GHCND:US1CASD0032',
        'sate': 'CA',
        'total_monthly_precipitation': san_diego_monthly,
        'total_yearly_precipitation' : san_diego_yearly,
        'relative_monthly_precipitation' : san_diego_relative,
        'relative_yearly_precipitation' : san_diego_relative_yearly

    },
}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation, file, indent=4)