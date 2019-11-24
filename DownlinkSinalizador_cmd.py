import urllib2
import json
#import http.client

data = '{"app_id":"parkingout_01","dev_id":"so_18","rf_chain": 1,"port": 1,"payload_raw":"AQICQBA=", "nw_proto": "ICMP", "actions": "ALLOW", "priority": "10"}'
url = 'https://integrations.thethingsnetwork.org/ttn-brazil/api/v2/down/parkingout_01/test?key=ttn-account-v2.rP1vpjDKAy6lm2usGmpZ5UNTJ6jC1IXxMXppdDUE7YA'
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)

content = '''{
  "app_id": "parkingout_01",
  "dev_id": "so_18",
  "rf_chain": "1",
  "port": "1",
  "payload_raw": "AQICQBA="
}'''
data = json.loads(content)
print(data.get("app_id"))
print(data.get("dev_id"))
print(data.get("rf_chain"))
print(data.get("port"))
print(data.get("payload_raw"))

#conn = http.client.HTTPSConnection('enpyhwc1x18o.x.pipedream.net')
#conn.request("POST", "/", '{ "name": "Luke Skywalker" }', {'Content-Type': 'application/json'})


# if (data == ('{"app_id":"parkingout_01","dev_id":"so_18","rf_chain": 1,"port": 1,"payload_raw":"AQICQBA=", "nw_proto": "ICMP", "actions": "ALLOW", "priority": "10"}'))
# print("Se 'payload_raw : Base64'AQICQBA=' == H'01 02 02 40 10' == 40 = Vaga Livre & 10 = Timer")
# print("Se 'payload_raw : Base64'AQICgBA=' == H'01 02 02 80 10' == 80 = Vaga Ocupada & 10 = Timer")
# print("Se 'payload_raw : Base64'AQICQAU=' == H'01 02 02 40 05' == 40 = Vaga Livre & 05 = Timer")
# print("Se 'payload_raw : Base64'AQICgAU=' == H'01 02 02 80 05' == 40 = Vaga Ocupada & 05 = Timer")
# print("\nDownlink enviado para 'so_18' com sucesso")

f.close()

print("Downlink enviado com sucesso")