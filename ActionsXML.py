

class Actions:  
    def __init__(self):
        self.ActionsDicit = {"cond":self.cond,"Return":self.Return,"Action":self.Action,"ReturnBase":self.ReturnBase
                             ,"ValorCompra":self.ValorCompra}
        self.ClonePlay = None
    def cond(self,DictiList):
        self.ClonePlay  = DictiList
        if ">" in DictiList["cond"] :
            return DictiList["Value"] > DictiList["cond"].split(">")[1] 
        
    def Return(self,DictiList):
        DictiList["Return"].replace("@x",DictiList["Value"])
        return DictiList["Return"]
    
    def Action(self,DictiList):
        return {"ActionBase_XML":DictiList.get("Action")}

    def ReturnBase(self,DictiList):
            return DictiList.get("ReturnBase")
    
    def ValorCompra(self,DictiList):
            return int(DictiList.get("ValorCompra"))*int(DictiList["Value"])
