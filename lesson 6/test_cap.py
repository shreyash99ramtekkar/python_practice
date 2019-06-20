import cap
import unittest

class TestCap(unittest.TestCase):
	"""docstring for TestClass"""
	def test_one_word(self):
		text = 'python'
		result = cap.cap_test(text)
		self.assertEqual(result,'Python')

	def test_two_word(self):
		text = 'python programming'
		result = cap.cap_test(text)
		self.assertEqual(result,'Python Programming')
if __name__ == '__main__':
	unittest.main()
			
		