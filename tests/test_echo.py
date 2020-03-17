#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        ''' This function is called only once for all tests '''
        self.parser = echo.create_parser()
        self.pystring = 'python2'
        if sys.version_info[0] == 3:
            self.pystring = 'python3'

    def test_all_options(self):
        args = ['-tul', 'HeLlO wOrLd']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = 'Hello World'
        self.assertEqual(actual, expected)

    def test_upper_short(self):
        args = ['-u', 'hello world']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = 'HELLO WORLD'
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ['-l', 'HeLlO wOrLd']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = 'hello world'
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ['-t', 'HeLlO wOrLd']
        actual = echo.main(args)
        expected = 'Hello World'
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ['--upper', 'hello world']
        actual = echo.main(args)
        expected = 'HELLO WORLD'
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ['--lower', 'HeLlO wOrLd']
        actual = echo.main(args)
        expected = 'hello world'
        self.assertEqual(actual, expected)

    def test_title_long(self):
        args = ['--title', 'HeLlO wOrLd']
        actual = echo.main(args)
        expected = 'Hello World'
        self.assertEqual(actual, expected)

    def test_help(self):
        ''' Running the program without arguments should show usage. '''
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            [self.pystring, "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode('utf8')
        with open('./USAGE') as file:
            usage = file.read()
        self.assertEquals(stdout, usage)

    def test_no_options(self):
        args = ['HeLlO WoRlD']
        ns = self.parser.parse_args(args)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.lower)


if __name__ == '__main__':
    unittest.main()
