import urllib.parse
import requests
from requests.auth import HTTPBasicAuth
import json


#Program allows user to request clients from Phorest API and post vouchers back for searched clients
#Assuming that I can use clientID instead of businessID for post /api/business/{businessId}/voucher
# kevin.walsh@phorest.com

#get client info#

url = ('https://api-gateway-dev.phorest.com/third-party-api-server/api/business/eTC3QY5W3p_HmGHezKfxJw/client?size=20&page=0')

#allow email or phone input
inputParameter = input('EmailAddress or PhoneNumber: ')
if inputParameter.find("@") == -1:
   parameter = { 'phone' : inputParameter}
else:
   parameter = {'email': inputParameter}

jsonData = requests.get(url, params=parameter, auth = ('global/cloud@apiexamples.com', 'VMlRo/eh+Xd8M~l')).json()
#print(jsonData)
print()

#get client ID
clientId = jsonData['_embedded']['clients'][0]['clientId']
clientName = jsonData['_embedded']['clients'][0]['firstName']

#post voucher#

#Ask for voucher amount
voucherAmount = input('Please enter voucher amount: ')
floatVoucherAmount = float(voucherAmount)
print()
#Get Voucher Info for specific client
getVoucherUrl = ('https://api-gateway-dev.phorest.com/third-party-api-server/api/business/eTC3QY5W3p_HmGHezKfxJw/voucher?')

getClientVoucherUrl = getVoucherUrl + urllib.parse.urlencode({'clientId': clientId})
voucherData = requests.get(getClientVoucherUrl, auth = ('global/cloud@apiexamples.com', 'VMlRo/eh+Xd8M~l')).json()

#update voucher information for client

newOriginalBal = voucherData['_embedded']['vouchers'][0]['originalBalance'] + floatVoucherAmount
newRemainingBal = voucherData['_embedded']['vouchers'][0]['remainingBalance'] + floatVoucherAmount

voucherData['_embedded']['vouchers'][0]['originalBalance'] = newOriginalBal
voucherData['_embedded']['vouchers'][0]['remainingBalance']= newRemainingBal

print()

requestJson = json.dumps(voucherData)

#make POST request with updated voucher information
postVoucherUrl = ('https://api-gateway-dev.phorest.com/third-party-api-server/api/business/eTC3QY5W3p_HmGHezKfxJw/voucher')

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
response = requests.post(postVoucherUrl, data=requestJson, headers=headers, auth = ('global/cloud@apiexamples.com', 'VMlRo/eh+Xd8M~l'))

strReponse = str(response)
if strReponse == "<Response [400]>":
   print("€" + voucherAmount + " was successfully added to " + clientName + "'s account." )


