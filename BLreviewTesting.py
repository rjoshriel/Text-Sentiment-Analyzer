import unittest
from BL_rev import BL_Reviews
from DAL_Reviews import DAL_rev
class Test(unittest.TestCase): 
    def testingSort(self):
        bl=BL_Reviews()
        dal=DAL_rev()
        self.assertTrue(bl.sorting(),dal.sorting())
    def testingGood(self):
        bl=BL_Reviews()
        dal=DAL_rev()
        self.assertTrue(bl.goodReview(),dal.goodReview())
    def testingBad(self):
        bl=BL_Reviews()
        dal=DAL_rev()
        self.assertTrue(bl.badReview(),dal.badReview())
if __name__ == '__main__': 
	unittest.main() 
