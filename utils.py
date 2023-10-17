import requests,json
class element():
    def __init__(self) :
        url="https://ptable.com/JSON/properties-90d5338.json"
        req=requests.get(url)
        self.alldata=json.loads(req.text)
        self.symbols=[self.alldata[i]['symbol'] for i in range(1,len(self.alldata))]
    def get_data(self,symbol):
        if symbol not in self.symbols:
            self.prop,self.compounds=None,None
            return
        self.prop=self.alldata[self.symbols.index(symbol)+1]
        self.prop['electrons']=str(self.prop['electrons'])[1:-1]

        url_compounds="https://ptable.com/JSON/compounds/formula="+symbol
        req=requests.get(url_compounds)
        data=json.loads(req.text)
        num=data['totalresults']
        num=num if num<5 else 5
        compounds=[data['matches'][-i-1]['molecularformula'] for i in range(num)]
        for x in compounds:
            if x==symbol:
                compounds.remove(x)
        self.compounds=' '.join(compounds)

if __name__=="__main__":
    symbol=input("input the element symbol: ")
    ele=element()
    ele.get_data(symbol)
    print(ele.prop)