import xml.etree.ElementTree as ET
import ActionsXML as act

class MiglanXml:
    def __init__(self,FilePath=f"./Rules.xml"):
        self.FilePath = FilePath
        self.CloneList = None
        self.SessionNode = []
        self.Actions = act.Actions()
        self.Records_items = None
        self.ParamNode = None

    def RecordsItems(self,RecordList:dict):
        self.Records_items = RecordList
    def ReplaceParans(self,NodeValue:str,Parans:list):
        for i in Parans:
            try:
                NodeValue = NodeValue.replace(i,Parans[i])
            except:
                pass
        return NodeValue
    def ExecuteAllNodes(self,Parans:list):
        root = ET.parse(self.FilePath).getroot()
        output = []
        self.ParamNode = Parans
        for  ch in root:
            value = {ch.tag:mXML.ExecuteRule(ch.tag,Parans),"text":ch.text}
            output.append(value)
            self.SessionNode.append(value)
            if ch.attrib.get("break"):
                ValueAttr = str(ch.attrib.get("break").split("=")[1])
                tagValue = str(value.get(ch.tag)[ch.attrib.get("break").split("=")[0]])
                if ValueAttr == tagValue:
                    break
        return output

    def Get(self,NodeName:str):
        tree = ET.parse(self.FilePath)
        root = tree.getroot()
        for elem in root.findall(NodeName):
            return elem.attrib
        
    def ExecuteRule(self,NodeName:str,Parans):
        Node = self.Get(NodeName)
        AttributesNode = {}
        if Node:
            for i in Node:
                Node[i] = self.LoadRecords(Node[i])
                Node[i] = self.ReplaceParans(Node[i],Parans)
                AttributesNode[i] = Node[i]        
        return self.AppplyRules(AttributesNode)

    def LoadRecords(self,Node):
        string_item = str(Node)
        if self.Records_items:

            for i in self.Records_items:
                string_item = str(string_item).replace(i,self.Records_items[i])
        return string_item
    def AppplyRules(self,Nodelist):
        actions = act.Actions()
        List_returns = []
        for i in Nodelist:
            self.Actions = actions.ActionsDicit.get(i)
            if i == "ref":
                GetReferencial = Nodelist[i].split(".")
                for a in self.SessionNode:
                    if a.get(GetReferencial[0]):
                        List_returns.append({i:a.get(GetReferencial[0])[GetReferencial[1]]})
            if self.Actions:
                if(isinstance(self.Actions,str)):
                    self.CloneList =  Nodelist
                    List_returns.append(self.ExecuteRule(self.Actions,["0","0"]))
                else:
                    if self.CloneList:
                        List_returns.append({i:self.Actions(self.CloneList)})
                        self.CloneList = None
                    else:
                        for x in Nodelist:
                            Nodelist[x] = self.ReplaceParans(Nodelist[x],self.ParamNode)
                            Nodelist[x] = self.LoadRecords(Nodelist[x])
                        List_returns.append({i:self.Actions(Nodelist)})
        Temp_list =[]
        if(isinstance(List_returns,list)):
            for i in List_returns: 
                if(i.get("Action")):
                    var = self.ExecuteRule(i.get("Action").get("ActionBase_XML"),["0","0"])
                    Temp_list.append(var)
        for i in Temp_list:
            List_returns.append(i)
        valueFinal = {}
        for i in List_returns:
            if isinstance(i,dict):
                for key, value in i.items():
                    valueFinal[key] = value
            for ij in i:
                 if isinstance(ij,dict):
                    for key, value in ij.items():
                        valueFinal[key] = value
        return valueFinal

#testes 
mXML = MiglanXml(f"C:/Users/ncata/Documents/Projetos/Miglan1.0/python/Rules.xml")

ShopDTO = {"@item":"Caderno","@valor":"5"}
ValuesInput = {"@x":"3"}
mXML.RecordsItems(ShopDTO)

ExecRules = mXML.ExecuteAllNodes(ValuesInput)
print(ExecRules)