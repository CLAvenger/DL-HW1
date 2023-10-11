import requests,json,re

url="https://ptable.com/JSON/properties-90d5338.json"
req=requests.get(url)
data=json.loads(req.text)
symbols=[data[i]['symbol'] for i in range(1,len(data))]
symbol=input("input the element symbol: ")

prop=data[symbols.index(symbol)+1]
weight=prop['weight']
energy_levels=prop['electrons']
electronegativity=prop['electroneg']
melt_k=float(prop['melt'])
boil_k=float(prop['boil'])
melt_c=melt_k-273.15
boil_c=boil_k-273.15
melt_f=melt_c*9/5+32
boil_f=boil_c*9/5+32
# print(melt_c,boil_c,melt_f,boil_f)

url_compounds="https://ptable.com/JSON/compounds/formula="+symbol
req=requests.get(url_compounds)
data=json.loads(req.text)
# print(data['formula'])
# print(data['matches'])
num=data['totalresults']
num=num if num<5 else 5
compounds=[data['matches'][-i-1]['molecularformula'] for i in range(num)]
for x in compounds:
    if x==symbol:
        compounds.remove(x)
print(compounds)
