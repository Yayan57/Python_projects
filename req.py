import requests

url = "http://luckypro12.com/PS5/includes/sumbit_order_limelight.php"

data = {
    'cc_number': '4007000000027',
    'cc_expmonth': '08',
    'cc_expyear': '21',
    'cc_cvv': '234',
}

response = requests.post(url, data=data).text

print(response)