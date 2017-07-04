import unittest
from unittest.mock import patch

import hitcount

class HitCountTest(unittest.TestCase):
  def testOneHit(self):
    hitcount.hit("user1")
    self.assertEqual(1, hitcount.getHit('user1'))

if __name__ == '__main__':
  unittest.main()
		
