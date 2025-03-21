import requests 

api_key = 'c0e71b10de32a5263a84aba1'

source_currency = input('Enter the source currency e.g INR:  ')
amount = float(input('Enter the amount : '))
target_currency = input('Enter the target currency e.g. USD:  ')


url = f' https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}'

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    conversion_rates = data['conversion_rates']
    
    if target_currency  in conversion_rates:
        exchange_rate = conversion_rates[target_currency]
        converted_amount = amount * exchange_rate
        print(f'converted amount is {converted_amount}  {target_currency}')
    else:
        print('Currency not found')
        
else:
    print('Failed to fetch data')