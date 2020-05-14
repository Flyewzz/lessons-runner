import subprocess
import sys
import unittest

from usecases.ConnectWebinar import ConnectWebinar
# from tests.config import config

if __name__ == '__main__':
    action = None
    conference_type = sys.argv[1]
    if conference_type == 'webinar':
        action = unittest.makeSuite(ConnectWebinar)
    suite = unittest.TestSuite((
        action,
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
