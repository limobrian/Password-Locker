import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        
        self.new_credential = Credential("Facebook","dela","dela13")

    def tearDown(self):
        Credential.credential_list = []
        
   
if __name__ == '__main__':
    unittest.main()