import xml.etree.ElementTree as ET
from typing import List
from sockxml.model import *

class XMLReader:
    def __init__(self):
        self.tags = ['interfaces', 'datafields', 'enumerations', 'complexTypes', 'messageHeader', 'messages']

        self.interfaces = []
        self.datafields = []
        self.enumerations = []
        self.complextypes = []
        self.messageHeader = MessageHeaderXML()
        self.messages: List[MessageXML] = []

    @staticmethod
    def attr_exists(element: ET.Element, attrib: str):
        if attrib in element.attrib:
            return True
        else:
            return False

    @staticmethod
    def get_attr(element: ET.Element, attrib: str):
        if XMLReader.attr_exists(element, attrib):
            return element.attrib[attrib]
        return ''

    def parse(self, file_name: str):
        try:
            tree = ET.parse(file_name)
            root: ET.Element = tree.getroot()
            self.__recursive_parse(root)

            conf = SockXMLConfiguration()
            conf.interfaces = self.interfaces
            conf.datafields = self.datafields
            conf.enumerations = self.enumerations
            conf.complextypes = self.complextypes
            conf.messageHeader = self.messageHeader
            conf.messages = self.messages
            return conf

        except Exception as e:
          print(e)


    def __recursive_parse(self, element: ET.Element):
        if element.tag == "interfaces":
            self.interfaces = self.__read_interface(element)

        if element.tag == "datafields":
            self.datafields = self.__read_datafield(element)

        elif element.tag == "enumerations":
            self.enumerations = self.__read_enumeration(element)

        elif element.tag == "complexTypes":
            self.complextypes = self.__read_complex(element)
        
        elif element.tag == "messageHeader":
            self.messageHeader = self.__read_message_header(element)

        elif element.tag == "messages":
            self.messages = self.__read_message(element)
        
        if element.tag in self.tags:
            # recursive function break
            return

        for e in element:
            self.__recursive_parse(e)

    def __read_message_header(self, element: ET.Element):
        searched = element.findall('messageHeader')
        item_list = []
        for i in searched:
            item = MessageHeaderXML()
            item.name = self.get_attr(i,'name')
            item.description = self.get_attr(i, 'description')
            item_list.append(item)


    def __read_interface(self, element: ET.Element) -> list[InterfaceXML]:
        searched = element.findall('interface')
        item_list = []
        for i in searched:
            # set interface attributes
            item = InterfaceXML()
            item.name = XMLReader.get_attr(i,'name')
            item.bitOrder = XMLReader.get_attr(i, 'bitOrder')
            item.inbyteorder = XMLReader.get_attr(i, 'inByteOrder')
            item.outbyteorder = XMLReader.get_attr(i, 'outByteOrder')
            item.settings = XMLReader.get_attr(i, 'settings')
            item.type = XMLReader.get_attr(i, 'type')
            item.mode = XMLReader.get_attr(i, 'mode')
            item.description = XMLReader.get_attr(i, 'description')
            item_list.append(item)
            
            # set packets
            packets = i.findall('packet')
            for p in packets:
                pack = InterfacePacketXML()
                pack.name = XMLReader.get_attr(p, 'name')
                pack.rx = XMLReader.get_attr(p, 'rx')
                pack.tx = XMLReader.get_attr(p, 'tx')
                item.packets.append(pack)
            
        return item_list

    def __read_datafield(self, element: ET.Element):        
        searched = element.findall('data')
        item_list = []
        for i in searched:
            item = DataFieldXML()
            item.name = self.get_attr(i,'name')
            item.size = int(self.get_attr(i, 'size'))
            item.minvalue = self.get_attr(i, 'minValue')
            item.maxvalue = self.get_attr(i, 'maxValue')
            item.type = self.get_attr(i, 'dataType')
            item.formattype = self.get_attr(i, 'dataFormatType')
            item.resolution = self.get_attr(i, 'resolution')
            item.description = self.get_attr(i, 'description')
            item_list.append(item)
            
        return item_list

    
    def __read_enumeration(self, element: ET.Element):
        searched = element.findall('enum')
        item_list = []
        for i in searched:
            item = EnumXML()
            item.name = self.get_attr(i,'name')
            item.size = self.get_attr(i, 'size')
            item.minvalue = self.get_attr(i, 'minValue')
            item.maxvalue = self.get_attr(i, 'maxValue')
            item.format_type = self.get_attr(i, 'dataFormatType')
            item.description = self.get_attr(i, 'description')
            item_list.append(item)
            
            values = i.findall('value')
            for val in values:
                v = EnumValueXML()
                v.enumName = self.get_attr(val, 'enumName')
                v.enumValue = self.get_attr(val, 'enumValue')
                v.description = self.get_attr(val, 'description')
                item.values.append(v)
            
        return item_list
    
    
    def __read_complex(self, element: ET.Element):
        searched = element.findall('record')
        record_list = []
        
        for i in searched:
            record = RecordXML()
            record.name = self.get_attr(i, 'name')
            record_list.append(record)

            elements = i.findall('element')
            for e in elements:
                item = RecordElementXML()
                item.name = self.get_attr(e,'name')
                item.value = self.get_attr(e, 'value')
                item.datatypename = self.get_attr(e, 'dataTypeName')
                item.recordelementtype = self.get_attr(e, 'recordElementType')
                item.fieldtype = self.get_attr(e, 'fieldType')
                record.elements.append(item)

        return record_list


    def __read_message_header(element: ET.Element):
        root = element.find('complex')
        searched = root.findall('record')
        header = MessageHeaderXML()
        
        for i in searched:
            if XMLReader.get_attr(i, 'recordType') == 'messageHeader':
                for e in i.findall('element'):
                    item = RecordElementXML()
                    item.name = XMLReader.get_attr(e,'name')
                    item.datatypename = XMLReader.get_attr(e, 'dataTypeName')
                    item.recordelementtype = XMLReader.get_attr(e, 'recordElementType')
                    item.fieldtype = XMLReader.get_attr(e, 'fieldType')
                    header.records.append(item)
            
        return header


    def __read_message(self, element: ET.Element):
        searched = element.findall('message')
        messages = []
        for i in searched:
            m = MessageXML()
            m.mid = self.get_attr(i, 'mid')
            m.name = self.get_attr(i, 'name')
            messages.append(m)
            for e in i.findall('element'):
                item = RecordElementXML()
                item.name = self.get_attr(e, 'name')
                item.datatypename = self.get_attr(e, 'dataTypeName')
                item.recordelementtype = self.get_attr(e, 'recordElementType')
                item.fieldtype = self.get_attr(e, 'fieldType')
                m.elements.append(item)
        
        return messages