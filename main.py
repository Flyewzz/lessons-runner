import subprocess
import sys
import unittest

# from tests.LoginTest import LoginTest
# from tests.config import config

if __name__ == '__main__':
    suite = unittest.TestSuite((

        unittest.makeSuite(LoginTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
