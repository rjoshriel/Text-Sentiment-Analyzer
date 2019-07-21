import unittest
from BL_login import BL_login
from DAL_Login import DAL_login
class Test(unittest.TestCase): 
    def testingSort(self):
        bl=BL_login()
        dal=DAL_login()
        self.assertTrue(bl.check_user("ken"),dal.check_user("ken"))
    def testingAddUser(self):
        bl=BL_login()
        dal=DAL_login()
        self.assertFalse(bl.add_user("edward"),dal.add_user("edward"))
if __name__ == '__main__': 
	unittest.main() 
