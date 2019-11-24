import urllib2

data = '{"app_id":"parkingout_01","dev_id":"qi_8","rf_chain": 1,"port": 1,"payload_raw":"AQICyAABAAEByAEAAQHIAQABAT8I", "nw_proto": "ICMP", "actions": "ALLOW", "priority": "10"}'
url = 'https://integrations.thethingsnetwork.org/ttn-brazil/api/v2/down/parkingout_01/test?key=ttn-account-v2.rP1vpjDKAy6lm2usGmpZ5UNTJ6jC1IXxMXppdDUE7YA'
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)
print("app_id : parkingout_01,\ndev_id : qi_8,")
print("rf_chain : 1,\nport : 1,")
print("payload_raw : AQICyAABAAEByAEAAQHIAQABAT8I")
print("\nDownlink enviado para 'qi_8' com sucesso")

f.close()

