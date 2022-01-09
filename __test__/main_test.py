import os, unittest
from sockxml.sockxml import XMLReader
from sockxml.model import *

class TestSockXML(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TEST_DIR = os.path.join("__test__", 'data')

        cls.FILE_PATH = os.path.join(os.curdir, cls.TEST_DIR, "sock.xml")
        cls.INCORRET_FILE_PATH = os.path.join('.', cls.TEST_DIR, 'incorret.xml')
        cls.NOT_FOUND_FILE_PATH = os.path.join('.', 'unkown_file.xml')
    
    @classmethod
    def tearDownClass(cls):
        cls.FILE_NAME = "None"

    def print_list(self, lst: List):
        NUM=20
        print(NUM * '-'  + " %s size %d"  % (lst.__class__, len(lst) ))
        for item in lst:
            print(item)
    
    def test_file_not_found(self):
        xml = XMLReader()
        
        # typee check if file is not found
        data = xml.parse(self.NOT_FOUND_FILE_PATH)
        self.assertEqual(type(data), list)
        self.assertTrue(len(data) == 0)

        # typee check if fail reading file
        data = xml.parse(self.INCORRET_FILE_PATH)
        self.assertIsInstance(data, list)

    def test_parse(self):
        
        xml = XMLReader()
        data = xml.parse(self.FILE_PATH)
        
        # type check
        self.assertIsInstance(data, SockXMLConfiguration)
        
if __name__ == "__main__":
    unittest.main()
