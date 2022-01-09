import os, unittest
from sockxml.sockxml import XMLReader
from sockxml.model import *

class TestSockXML(unittest.TestCase):

    @classmethod
    def setup(cls):
        cls.TEST_DIR = os.path.join("__test__", 'data')

        cls.FILE_PATH = os.path.join(os.curdir, cls.TEST_DIR, "sock.xml")
        cls.INCORRET_FILE_PATH = os.path.join('.', cls.TEST_DIR, 'incorret.xml')
        cls.NOT_FOUND_FILE_PATH = os.path.join('.', 'unkown_file.xml')

        cls.xml = XMLReader()
        cls.testdata = cls.xml.parse(cls.FILE_PATH)

    @classmethod
    def setUpClass(cls):
        # for unittest
        cls.setup()    

    @classmethod
    def setup_class(cls):
        # for pytest
        cls.setup()
        print("starting class: {} execution".format(cls.__name__))

    @classmethod
    def tearDownClass(cls):
        cls.FILE_NAME = "None"

    def print_list(self, lst: List):
        _NUM=20
        print(_NUM * '-'  + " %s size %d"  % (lst.__class__, len(lst) ))
        for item in lst:
            print(item)

    def test_file_not_found(self):
        xml = XMLReader()
        
        # typee check if file is not found
        data = xml.parse(self.NOT_FOUND_FILE_PATH)
        self.assertEqual(type(data), type(None))

        # typee check if fail reading file
        data = xml.parse(self.INCORRET_FILE_PATH)
        self.assertEqual(type(data), type(None))

    def test_parse(self):
        xml = XMLReader()
        data = xml.parse(self.FILE_PATH)
        
        # type check
        self.assertIsInstance(data, SockXMLConfiguration)

    def test_interfaces(self):
        # type check
        self.assertIsInstance(self.testdata.interfaces, list)
        
        # member chechk
        interface: InterfaceXML = self.testdata.interfaces[0]
        self.assertIsInstance(interface.name, str)
        self.assertIsInstance(interface.bitorder, str)
        self.assertIsInstance(interface.inbyteorder, str)
        self.assertIsInstance(interface.outbyteorder, str)
        self.assertIsInstance(interface.settings, str)
        self.assertIsInstance(interface.type, str)
        self.assertIsInstance(interface.mode, str)
        self.assertIsInstance(interface.description, str)

        self.assertEqual(interface.name, 'MessageInputOutput')
        self.assertEqual(interface.bitorder, 'Intel')
        self.assertEqual(interface.inbyteorder, 'BigEndian')
        self.assertEqual(interface.outbyteorder, 'LittleEndian')
        self.assertEqual(interface.settings, '127.0.0.0:8080')
        self.assertEqual(interface.type, 'Tcp')
        self.assertEqual(interface.mode, 'Server')
        self.assertEqual(interface.description, 'descriptions')
    
    def test_datafields(self):
        # type check
        self.assertIsInstance(self.testdata.datafields, list)
        
        # member chechk
        datafield: DataFieldXML = self.testdata.datafields[0]
        self.assertEqual(datafield.name, 'sInt8Type')
        self.assertEqual(datafield.type, 'uint')
        self.assertEqual(datafield.formattype, 'bnr')
        self.assertEqual(datafield.minvalue, '-128')
        self.assertEqual(datafield.maxvalue, '127')
        self.assertEqual(datafield.size, 8)
        self.assertEqual(datafield.resolution, '')
        self.assertEqual(datafield.description, '')
        
if __name__ == "__main__":
    unittest.main()
