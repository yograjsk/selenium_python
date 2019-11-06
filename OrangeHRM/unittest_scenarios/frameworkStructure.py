import unittest

def setUpModule():
    print("setupModule")

def tearDownModule():
    print("tearDownModule")

class FWstructure(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("login to the application")

    @classmethod
    def tearDown(self):
        print("logout of the application")

    @classmethod
    def setUpClass(cls):
        print("setupClass - login to the application")

    @classmethod
    def tearDownClass(cls):
        print("teardown Class - logout of the application")

    def test_verify_login(self):
        print("verifying login")

    def test_create_user(self):
        print("creating user")

    def test_edit_user(self):
        print("editing user")

    def test_delete_user(self):
        print("deleting user")

if __name__ == "__main__":
    unittest.main()

