import unittest
import configparser
import sys
from unittest.mock import patch
from btconfig import parser

class CommandTest(unittest.TestCase):
    
    def setUp(self):
        self.parser = parser.Parser()

    def test_simple_subcommand(self):
        def simple(target):
            return target

        self.parser.create_subcommand('simple', simple)
        testargs = ["prog", "simple", "target"]

        with patch.object(sys, 'argv', testargs):
            res = self.parser.parse()
            assert res == "target"
    
    def test_multiple_subcommands(self):
        def one(target):
            return "%s called one" % target

        def two(target):
            return "%s called two" % target
        
        self.parser.create_subcommand('one', one)
        self.parser.create_subcommand('two', two)

        arg1 = ["prog", "one", "first"]
        arg2 = ["prog", "two", "second"]

        with patch.object(sys, 'argv', arg1):
            res = self.parser.parse()
            assert res == "first called one"

        
        with patch.object(sys, 'argv', arg2):
            res = self.parser.parse()
            assert res == "second called two"

        
        

#if __name__ == "__main__":
#    unittest.main()