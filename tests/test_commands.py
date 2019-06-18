import unittest
import configparser
from btconfig import command, cli

class CommandTest(unittest.TestCase):
    
    def setUp(self):
        config = configparser.ConfigParser()
        config['raspberry'] = { 'test-1' : 'first', 'test-2': 'second' }
        self.cmd = command.Command(config)


    def test_command_works_with_target(self):      
        self.assertEqual(self.cmd.command("echo %s", "test-1"), "first\n", "command should return the value of 'test-1' from config")
    
    def test_command_works_with_target_2(self):
        self.assertEqual(self.cmd.command("echo %s", "test-2"), "second\n", "command should return value of 'test-2' from config")

    def test_command_works_without_target(self):
        self.assertEqual(self.cmd.command("echo %s", ""), "first\nsecond\n", "command should return both values from config")



#if __name__ == "__main__":
#    unittest.main()