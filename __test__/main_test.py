import unittest
from sockxml.sockxml import XMLReader
from sockxml.model import *

class TestCoreMethods(unittest.TestCase):
    
    def print_list(self, lst: List):
        NUM=20
        print(NUM * '-'  + " %s size %d"  % (lst.__class__, len(lst) ))
        for item in lst:
            print(item)

    def test_read_xml(self):
        reader = XMLReader()
        data = reader.parse('resource/sock.xml')
        self.print_list(data.interfaces)
        self.print_list(data.datafields)
        self.print_list(data.enumerations)
        self.print_list(data.complextypes)
        self.print_list(data.messages)
        print(data.messageHeader)

        
        
if __name__ == "__main__":
    unittest.main()
