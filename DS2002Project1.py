import json
import requests
import sys

#url gives the exchange rate between the euro and over 100 other currencies
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json'
#url2 gives the full name of for each currency abbreviation
url2 = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'

header_var = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# These two lines allow me to get the information from the respective URLs
euro = requests.request("GET", url, headers=header_var)
currencies = requests.request("GET", url2, headers=header_var)

try:
    # These two lines convert the requests from above into readable python dictionaries
    euro_json = euro.json()
    currencies_json = currencies.json()

#By using except, the processor can produce an informative error if something goes wrong.
#In this case, the error would likely be caused by an issue with the URLs, so that is mentioned in the error message
except:
    print("A json object cannot be created. Ensure that the URLs are correct.")
    sys.exit()

#These two lines give the full name and conversion rate for usd
usd_name = currencies_json['usd']
usd_rate = euro_json['eur']['usd']

#These two lines give the full name and conversion rate for jpy
jpy_name = currencies_json['jpy']
jpy_rate = euro_json['eur']['jpy']

#These two lines give the full name and conversion rate for gbp
gbp_name = currencies_json['gbp']
gbp_rate = euro_json['eur']['gbp']

#These two lines give the full name and conversion rate for aud
aud_name = currencies_json['aud']
aud_rate = euro_json['eur']['aud']

#These two lines give the full name and conversion rate for cad
cad_name = currencies_json['cad']
cad_rate = euro_json['eur']['cad']

#These two lines give the full name and conversion rate for chf
chf_name = currencies_json['chf']
chf_rate = euro_json['eur']['chf']

#These two lines give the full name and conversion rate for cny
cny_name = currencies_json['cny']
cny_rate = euro_json['eur']['cny']

#These two lines give the full name and conversion rate for hkd
hkd_name = currencies_json['hkd']
hkd_rate = euro_json['eur']['hkd']

#These two lines give the full name and conversion rate for nzd
nzd_name = currencies_json['nzd']
nzd_rate = euro_json['eur']['nzd']

#This is creating a dictionary of all the exchange rates
#Format: key = currency full name, value = exchange rate
dict = {
    usd_name : usd_rate,
    jpy_name : jpy_rate,
    gbp_name : gbp_rate,
    aud_name : aud_rate,
    cad_name : cad_rate,
    chf_name : chf_rate,
    cny_name : cny_rate,
    hkd_name : hkd_rate,
    nzd_name : nzd_rate
}

#This line converts the dictionary into a json object
json_object = json.dumps(dict)

#These lines write the json object as a local file
with open("euro.json", "w") as outfile:
    outfile.write(json_object)
    outfile.close()


"""This data processor takes in two data files, one giving the exchange rate between the euro and many other
currencies, and the other giving the abbreviation and full name of the currencies. In order to make the data more 
useful for the viewer, the processor produces a JSON file of the full name of the other top 10 most traded currencies,
(according to https://www.ig.com/us/trading-strategies/what-are-the-top-10-most-traded-currencies-in-the-world-200115)
and the exchange rate from Euro to these other currencies."""