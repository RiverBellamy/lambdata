'''Unit tests for helper functions'''

import unittest
import helper_functions as hf
import pandas as pd
import numpy as np


class HFTester(unittest.TestCase):
    '''Tester to make sure helper functions work as intended'''

    def test_null_count(self):
        df1 = pd.DataFrame([[1, 2, np.nan], [np.nan, None, 3]])
        df2 = pd.DataFrame([[]])
        self.assertEqual(hf.null_count(df1), 3)
        self.assertEqual(hf.null_count(df2), 0)


if __name__ == '__main__':
    unittest.main()
