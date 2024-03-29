from typing import List


class InterfacePacketXML:
    name = 'MsgUnknown'
    rx = 'false'
    tx = 'false'


class InterfaceXML:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.bitorder = ''
        self.inbyteorder = ''
        self.outbyteorder = ''
        self.settings = ''
        self.type = ''
        self.mode = ''
        self.packets = []

    def __str__(self):
        v = 'Interface {}\n'.format(self.name)
        v += '|--> description({})\n'.format(self.description)
        v += '|--> bitorder({})\n'.format(self.bitorder)
        v += '|--> inbyteorder({})\n'.format(self.inbyteorder)
        v += '|--> outbyteorder({})\n'.format(self.outbyteorder)
        v += '|--> type({})\n'.format(self.type)
        v += '|--> mode({})\n'.format(self.mode)
        v += '|--> settings({})\n'.format(self.settings)
        v += '|--> packets({})\n'.format(
            ', '.join([i.name for i in self.packets]))
        return v


class DataFieldXML:
    def __init__(self):
        self.name = ''
        self.size = ''
        self.description = ''
        self.minvalue = ''
        self.maxvalue = ''
        self.type = ''
        self.format = ''
        self.resolution = ''

    def __str__(self):
        v = 'DataField {}({})\n'.format(self.name, self.size)
        v += '|--> minvalue({})\n'.format(self.minvalue)
        v += '|--> maxvalue({})\n'.format(self.maxvalue)
        v += '|--> type({})\n'.format(self.type)
        v += '|--> formattype({})\n'.format(self.format)
        v += '|--> resolution({})\n'.format(self.resolution)
        return v


class EnumXML:
    def __init__(self):
        self.name = ''
        self.size = ''
        self.description = ''
        self.minvalue = ''
        self.maxvalue = ''
        self.formattype = ''
        self.values = []

    def __str__(self):
        v = 'Enumeration {}({})\n'.format(self.name, self.size)
        v += '|--> minvalue({})\n'.format(self.minvalue)
        v += '|--> maxvalue({})\n'.format(self.maxvalue)
        v += '|--> formattype({})\n'.format(self.formattype)
        v += '|--> description({})\n'.format(self.description)
        return v


class EnumValueXML:
    def __init__(self):
        self.name = ''
        self.value = ''
        self.description = ''

    def __str__(self):
        v = '|--> {}({})'.format(self.name, self.value)
        return v


class RecordXML:
    def __init__(self):
        self.name = ''
        self.elements: RecordElementXML = []

    def __str__(self):
        v = 'Record {}\n'.format(self.name)
        for r in self.elements:
            v += '|--> {}\n'.format(r)
        return v


class RecordElementXML:
    def __init__(self):
        self.name = ''
        self.recordelementtype = ''
        self.datatypename = ''
        self.fieldtype = ''

    def __str__(self):
        v = 'RecordElement {}({} -> {})'.format(self.name,
                                                self.recordelementtype, self.datatypename)
        return v


class MessageHeaderXML:
    def __init__(self):
        self.records = []

    def __str__(self):
        v = 'MessageHeader\n'
        for r in self.records:
            v += '|--> {}\n'.format(r)

        return v


class MessageXML:
    def __init__(self):
        self.mid = ''
        self.name = ''
        self.elements = []

    def __str__(self):
        v = 'Message {}({})'.format(self.name, self.mid)
        return v


class SockXMLConfiguration():
    def __init__(self) -> None:
        self.interfaces: List[InterfaceXML] = list()
        self.datafields: List[DataFieldXML]
        self.enumerations: List[EnumXML] = list()
        self.complextypes: List[RecordXML] = list()
        self.messageHeader: MessageHeaderXML = None
        self.messages: List[MessageXML] = list()
