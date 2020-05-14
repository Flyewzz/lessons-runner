import subprocess
import sys
import unittest

from usecases.ConnectWebinar import ConnectWebinar
# from tests.config import config

if __name__ == '__main__':
    suite = unittest.TestSuite((

        unittest.makeSuite(ConnectWebinar),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
