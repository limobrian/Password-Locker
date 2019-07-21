import unittest
from user import User

class Testuser(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("limo", "brian", "limobrian290@gmail.com", "Blankphrase", "brianlimo") 

    def test_init(self):
        """
        testing initialization of class
        """
        self.assertEqual(self.new_user.firstName, "limo")
        self.assertEqual(self.new_user.lastName, "brian")
        self.assertEqual(self.new_user.email, "limobrian290@gmail.com")
        self.assertEqual(self.new_user.username, "limobrian")
        self.assertEqual(self.new_user.password, "brianlimo")

    def tearDown(self):
        """
        restart
        """
        User.create_account = []

    def test_save_account(self):
        """
        testing save account method
        """
        self.new_user.save_account() 
        self.assertEqual(len(User.create_account), 1)


if __name__ == '__main__':
    unittest.main()
