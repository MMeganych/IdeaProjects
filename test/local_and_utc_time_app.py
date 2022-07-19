from datetime import datetime
import pytz


country_names_dict = {
    'AD': 'Europe/Andorra',
    'AE': 'Asia/Dubai',
    'AF': 'Asia/Kabul',
    'AG': 'America/Antigua',
    'AI': 'America/Anguilla',
    'AL': 'Europe/Tirane',
    'AM': 'Asia/Yerevan',
    'AO': 'Africa/Luanda',
    'AZ': 'Asia/Baku',
    'BA': 'Europe/Sarajevo',
    'BB': 'America/Barbados',
    'BD': 'Asia/Dhaka',
    'BE': 'Europe/Brussels',
    'BF': 'Africa/Ouagadougou',
    'BG': 'Europe/Sofia',
    'BH': 'Asia/Bahrain'
}
for key in country_names_dict:
    print(key, "('", country_names_dict[key], "')")
print('Please enter a two-letter code of the country to choose the timezone (or "q" to quite): ')
while True:
    user_input = input().upper()
    if user_input in country_names_dict.keys() and len(user_input) == 2:
        tz_country = pytz.timezone(country_names_dict[user_input])
        print('Local time is', datetime.now(tz=tz_country))
        print('UTC time is', datetime.utcnow())
    elif user_input == 'Q':
        break
    else:
        print('Please enter the correct data')
pass
