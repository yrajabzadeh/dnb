import urllib.request, json

#parsing url
res = urllib.request.urlopen('https://dot.ca.gov/contact-us/.json').read()
json_res = json.loads(res)
counter = 0

##parsing json
for item in json_res['data']['children']:
    counter += 1
    print ("[")
    print ("{")
    print ("office_name", item['data']['title'], "office_link", item['data']['title'], "office_address", item['data']['title'], 
    "office_city", item['data']['title'], "office_zip", item['data']['title'], "office_phone", item['data']['title'],
    "mail_address", item['data']['title'], "mail_pobox", item['data']['title'], "mail_city", item['data']['title'],
    "mail_state", item['data']['title'], "mail_zip", item['data']['title'], "mail_phone", item['data']['title'] )
    print ("},")
    print ("]")
    print ("...")
    print("Number of listings: ", counter)
