# tests

import unittest
from compression import compress, decompress

class TestCompression(unittest.TestCase):

	def setUp(self):
		"""setup list of tuples (first, second)
			such that second is expected output of compress(first)"""
		self.toTestList = [('',''),('A','A'),('AA','AA0'),('AAA','AA1'),
					('AAAA', 'AA2'),('AAAAAAAAAA','AA8'),('AAAAAAAAAAA','AA9'),
					('AAAAAAAAAAAA','AA9A'),('AAAAAAAAAAAAA','AA9AA0'),
					('AAAAAAAAAAAAAA','AA9AA1'),('ABAC','ABAC'),('AAB','AA0B'),
					('AABB','AA0BB0'),('AAACBBC', 'AA1CBB0C')]

	def test_compress_decompress(self):
		for testCase in self.toTestList:
			# test compress output
			self.assertEqual(compress(testCase[0]),testCase[1])
			# test decompress output -- compressing then decompressing
			self.assertEqual(decompress(compress(testCase[0])),testCase[0])


	def test_invalid_cases(self):
		# compress should raise exception for invalid input
		self.assertRaises(AssertionError, compress, ('a'))
		self.assertRaises(AssertionError, compress, ('0'))
		self.assertRaises(AssertionError, compress, ('!'))
		self.assertRaises(AssertionError, compress, ('Aa'))

		# decompress should raise exception for invalid input
		self.assertRaises(AssertionError, decompress, ('a'))
		self.assertRaises(AssertionError, decompress, ('0'))
		self.assertRaises(AssertionError, decompress, ('!'))
		self.assertRaises(AssertionError, decompress, ('A0'))
		self.assertRaises(AssertionError, decompress, ('AB0'))
		self.assertRaises(AssertionError, decompress, ('AA11'))
		self.assertRaises(AssertionError, decompress, ('AA1A1'))
		self.assertRaises(AssertionError, decompress, ('0A'))



if __name__ == '__main__':
    unittest.main()

