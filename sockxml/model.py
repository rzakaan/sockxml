from typing import List
    
class InterfacePacketXML:
    name='MsgUnknown' 
    rx='false'
    tx='false'

class InterfaceXML:
    def __init__(self):
        self.name=''
        self.description=''
        self.bitOrder='' 
        self.inByteOrder='' 
        self.outByteOrder='' 
        self.settings='' 
        self.type='' 
        self.mode='' 
        self.packets=[]
    
    def __str__(self):
        v  ='Interface {}\n'.format(self.name)
        v +='|--> description({})\n'.format(self.description)
        v +='|--> bitOrder({})\n'.format(self.bitOrder)
        v +='|--> inByteOrder({})\n'.format(self.inByteOrder)
        v +='|--> outByteOrder({})\n'.format(self.outByteOrder)
        v +='|--> type({})\n'.format(self.type)
        v +='|--> mode({})\n'.format(self.mode)
        v +='|--> settings({})\n'.format(self.settings)
        v +='|--> packets({})\n'.format(', '.join([i.name for i in self.packets]))
        return v

class DataFieldXML:
    def __init__(self):
        self.name=''
        self.size=''
        self.description=''
        self.minvalue=''
        self.maxvalue=''
        self.type='' 
        self.formattype='' 
        self.resolution=''
    
    def __str__(self):
        v  ='DataField {}({})\n'.format(self.name, self.size)
        v +='|--> minValue({})\n'.format(self.minvalue)
        v +='|--> maxValue({})\n'.format(self.maxvalue)
        v +='|--> dataType({})\n'.format(self.type)
        v +='|--> dataFormatType({})\n'.format(self.formattype)
        v +='|--> resolution({})\n'.format(self.resolution)
        return v

class EnumXML:
    def __init__(self):
        self.name=''
        self.size=''
        self.description=''
        self.minvalue=''
        self.maxvalue=''
        self.format_type='' 
        self.values=[]

    def __str__(self):
        v  ='Enumeration {}({})\n'.format(self.name, self.size)
        v +='|--> minValue({})\n'.format(self.minvalue)
        v +='|--> maxValue({})\n'.format(self.maxvalue)
        v +='|--> dataFormatType({})\n'.format(self.format_type)
        v +='|--> description({})\n'.format(self.description)
        return v

class EnumValueXML:
    def __init__(self):
        self.enumName=''
        self.enumValue=''
        self.description=''

    def __str__(self):
        v  ='|--> {}({})'.format(self.enumName, self.enumValue)
        return v

class RecordXML:
    def __init__(self):    
        self.name=''
        self.elements: RecordElementXML=[]
    
    def __str__(self):
        v  ='Record {}\n'.format(self.name)
        for r in self.elements:
            v += '|--> {}\n'.format(r)
        return v

class RecordElementXML:
    def __init__(self):
        self.name=''
        self.recordelementtype='' 
        self.datatypename='' 
        self.fieldtype='' 

    def __str__(self):
        v  ='RecordElement {}({} -> {})'.format(self.name, self.recordelementtype, self.datatypename)
        return v

class MessageHeaderXML:
    def __init__(self):
        self.records=[]
    
    def __str__(self):
        v = 'MessageHeader\n'
        for r in self.records:
            v += '|--> {}\n'.format(r)
        
        return v

class MessageXML:
    def __init__(self):
        self.mid=''
        self.name=''
        self.elements=[] 

    def __str__(self):
        v  ='Message {}({})'.format(self.name, self.mid)
        return v

class SockXMLConfiguration():
    def __init__(self) -> None:
        self.interfaces: List[InterfaceXML] = list()
        self.datafields: List[DataFieldXML]
        self.enumerations: List[EnumXML] = list()
        self.complextypes: List[RecordXML] = list()
        self.messageHeader: List[MessageHeaderXML] = list()
        self.messages: List[MessageXML] = list()