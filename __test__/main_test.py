import unittest
import unittest.mock
from unittest.mock import Mock()
from sockxml.sockxml import XMLReader
from sockxml.model import *

class TestCoreMethods(unittest.TestCase):
    
    FILE_NAME = "sock.xml"
    valid_XML_str = '''
    <root>
      <interfaces name='interface'>
        <interface bitOrder='Intel' inByteOrder='BigEndian' outByteOrder='LittleEndian' settings='127.0.0.0:8080' type='Tcp' mode='Server' name='MessageInputOutput' description="description for">
            <packet name='MsgHeatBeat' rx='true' />
            <packet name='MsgTimeSync' tx='true' />
            <packet name='MsgTest' tx='true' />
            <packet name='MsgFault' tx='true' />
        </interface>
    </interfaces>
    
    <datafields name='datafield'>
        <data dataFormatType='bnr' dataType='uint' name='sInt8Type'  minValue='-128' maxValue='127' size='8' resolution='' description='' />
        <data dataFormatType='bnr' dataType='uint' name='sInt16Type' minValue='-32768' maxValue='32767' size='16' resolution='' description='' />
        <data dataFormatType='bnr' dataType='uint' name='sInt32Type' minValue='-2147483648' maxValue='2147483647' size='32' resolution='' description='' />
        <data dataFormatType='bnr' dataType='uint' name='sInt64Type' minValue='0' maxValue='127' size='64' resolution='' description='' />
        <data dataFormatType='ieee754' dataType='float' name='float32Type' minValue='-1000' maxValue='1000' size='32' resolution='' description='' />
        <data dataFormatType='ieee754' dataType='float' name='float64Type' minValue='-1000' maxValue='1000' size='64' resolution='' description='' />
    </datafields>
    
    <enumerations name='enumeration'>
        <enum name='EnumAirPlot' size='8' dataFormatType='bnr' minValue='0' maxValue='64' description=''>
            <value enumName='AIR' enumValue='0' description='' />
            <value enumName='SURFACE' enumValue='1' description=''/>
            <value enumName='IFF' enumValue='2' description=''/>
        </enum>
    </enumerations>
    
    <complex name='complextype'>
        <record recordType='messageHeader' name='messageHeader'>
            <element recordElementType='datafield' dataTypeName='uInt8Type' name='messageId' value='' fieldType='id' />
            <element recordElementType='datafield' dataTypeName='uInt8Type' name='messageLength' value='' fieldType='payloadSize' />    
        </record>
        <record name='PositionType'>
            <element recordElementType='datafield' dataTypeName='float64Type' name='x' value='' description='' />
            <element recordElementType='datafield' dataTypeName='float64Type' name='y' value='' description='' />
            <element recordElementType='datafield' dataTypeName='float64Type' name='z' value='' description='' />
        </record>
        <record name='StaticArrayReport' recordType='array'>
            <array arrayElementType='datafield' dataTypeName='float64Type' size='4'>
                <element value='' />
                <element value='' />
                <element value='' />
                <element value='' />
            </array>
        </record>
        <record name='DynamicArrayReport' recordType='array'>
            <array arrayElementType='datafield' dataTypeName='float64Type' elementCountField=''>
                <element value='' />
                <element value='' />
                <element value='' />
                <element value='' />
            </array>
        </record>
    </complex>
    
    <messages>
        <message mid='0x01' name='MsgHeartBeat'>
           <element recordElementType='datafield' dataTypeName='sInt8Type' name='byteVar' value='' fieldType='None' />
           <element recordElementType='datafield' dataTypeName='sInt16Type' name='shortVar' value='' fieldType='None' />
           <element recordElementType='datafield' dataTypeName='sInt32Type' name='intVar' value='' fieldType='None' />
           <element recordElementType='datafield' dataTypeName='sInt64Type' name='longVar' value='' fieldType='None' />
           <element recordElementType='enumeration' dataTypeName='EnumAirPlot' name='plot' value='AIR' fieldType='None' />
           <element recordElementType='record' dataTypeName='PositionType' name='position' value='' fieldType='None' />
        </message>
        
        <message mid='0x02' name='MsgTrackPosition'>
           <element recordElementType='datafield' dataTypeName='float64Type' name='timestamp' value='' fieldType='None' />
           <element recordElementType='record' dataTypeName='PositionType' name='trackPosition' value='' fieldType='None' />
        </message> 
    </messages>
    </root>
    '''

    valid_XML_etree = ETree.XML(valid_XML_str)
    # invalid_XML_etree = ETree.XML(invalid_XML_str)
    
    def print_list(self, lst: List):
        NUM=20
        print(NUM * '-'  + " %s size %d"  % (lst.__class__, len(lst) ))
        for item in lst:
            print(item)

    def test_read_xml_config_mandatory_parameters_missing(self):
        xml_file = 'hnas_nfs.xml'
        self.mock_object(os, 'access', mock.Mock(return_value=True))
        self.mock_object(ETree, 'parse', mock.Mock(return_value=ETree.ElementTree))
        self.mock_object(ETree.ElementTree, 'getroot', mock.Mock(return_value=valid_XML_etree))
        self.assertRaises(exception.ParameterNotFound, hnas_utils.read_xml_config, xml_file, service_parameters, optional_parameters)

    
    @mock.patch('sockxml.sockxml.etree')
    def test_parse(mock_xml):
        reader = XMLReader()
        data = reader.parse('resource/sock.xml')
        mock_xml.parse.assert_called_with(FILE_NAME)        
        print(mock_xml.return_value)

        
        
if __name__ == "__main__":
    unittest.main()
