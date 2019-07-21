from DAL_Reviews import DAL_rev

import unittest
#import DAL_Reviews


class TestCase(unittest.TestCase):

	def test_goodReview(self):
		DAL_Review=DAL_rev()
		result=DAL_Review.goodReview()
		self.assertTrue(result)

	def test_badReview(self):
		DAL_Review=DAL_rev()
		result=DAL_Review.badReview()
		self.assertIs(5,5)
		
	def test_sorting(self):
		DAL_Review=DAL_rev()
		result=DAL_Review.sorting()
		self.assertTrue(result)

