import unittest
from internetmeter import ConfigLoader


class CfgLoaderTest(unittest.TestCase):
    def test_load(self):
        self.assertRaises(AssertionError, lambda: ConfigLoader(''))
        cfg = ConfigLoader('../settings.cfg')
        self.assertEqual(cfg.get_size(), 4)


if __name__ == '__main__':
    unittest.main()
