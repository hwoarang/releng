#!/usr/bin/env python

# Copyright (c) 2016 Orange and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0

import logging
import unittest

from utils import reporting_utils


class reportingUtilsTesting(unittest.TestCase):

    logging.disable(logging.CRITICAL)

    def setUp(self):
        self.test = reporting_utils

    def test_getConfig(self):
        self.assertEqual(self.test.get_config("general.period"), 10)
# TODO
# ...

if __name__ == "__main__":
    unittest.main(verbosity=2)
