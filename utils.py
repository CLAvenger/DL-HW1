import requests,json
def get_data(symbol):
    url="https://ptable.com/JSON/properties-90d5338.json"
    req=requests.get(url)
    data=json.loads(req.text)
    symbols=[data[i]['symbol'] for i in range(1,len(data))]
    if symbol not in symbols:
        return None,None

    prop=data[symbols.index(symbol)+1]
    weight=prop['weight']
    energy_levels=prop['electrons']
    prop['electrons']=str(prop['electrons'])[1:-1]
    melt_k=float(prop['melt'])
    boil_k=float(prop['boil'])
    
    melt_c=melt_k-273.15
    boil_c=boil_k-273.15
    melt_f=melt_c*9/5+32
    boil_f=boil_c*9/5+32
    prop['melt_c']="{:.5g}".format(melt_c)
    prop['boil_c']="{:.5g}".format(boil_c)
    prop['melt_f']="{:.5g}".format(melt_f)
    prop['boil_f']="{:.5g}".format(boil_f)
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
    compounds=' '.join(compounds)
    # print(compounds)
    return prop,compounds

if __name__=="__main__":
    symbol=input("input the element symbol: ")
    prop,compounds=get_data(symbol)
    print(prop)