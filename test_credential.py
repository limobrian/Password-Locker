import unittest

from credential import Credential


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = Credential("Gmail", "limo", "brianlimo") 

    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_credential.platform, "Gmail")
        self.assertEqual(self.new_credential.username, "limo")
        self.assertEqual(self.new_credential.password, "brianlimo")

    def tearDown(self):
    
        Credential.credentials = []

    def test_save_credential(self):
        """
        test if credential is saved in the credentials list
        """
        self.new_credential.save_credential()  
        self.assertEqual(len(Credential.credentials), 1)

    def test_display_credentials(self):
        """
        test display credentials method
        """
        self.assertEqual(Credential.display_credentials(),Credential.credentials)

if __name__ == '__main__':
    unittest.main()