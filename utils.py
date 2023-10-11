import requests,json

url="https://ptable.com/JSON/properties-90d5338.json"
symbol=input("input the element symbol: ")
req=requests.get(url)
data=json.loads(req.text)
# print(data[1]['symbol'])
symbols=[data[i]['symbol'] for i in range(1,len(data))]
print(data[symbols.index(symbol)+1])