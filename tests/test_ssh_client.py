import unittest
from unittest.mock import patch
from btconfig import ssh_client

class FakeClient():
    def exec_command(self, value):
        return value

class MockSSHClient(ssh_client.SSHClient):
    def __init__(self):
        self.connections = { 'm1': FakeClient(), 'm2': FakeClient() }

class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = MockSSHClient()

    def test_runs_all(self):
        assert len(self.client.run('stuff')) == 2

    def test_run_one_runs_one(self):
        assert len(self.client.run('stuff', 'm1')) == 1