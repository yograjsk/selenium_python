import unittest

'''
setUp = before every test method
tearDown = after every test method

setupClass = executed only once before first test method
tearDownClass = executed after last test method

setUpModule = executed only once before the module
tearDownModule = executed only once after the module
'''

def setUpModule():
    print("___run before module access")

def tearDownModule():
    print("___run after module last access")

class FrameworkStructure(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("launch application login page")

    @classmethod
    def tearDownClass(cls):
        print("close the application page")

    @classmethod
    def setUp(self):
        print("logining into the application")

    @classmethod
    def tearDown(self):
        print("logining out of the application")

    def test_checkWelcome(self):
        # print("login")
        print("checking welcome user text")
        # print("logout")

    def test_createUser(self):
        # print("login")
        print("creating user")
        # print("logout")

    def test_editUser(self):
        # print("login")
        print("editing user")
        # print("logout")

    def test_deleteUser(self):
        # print("login")
        print("deleting user")
        # print("logout")

if __name__ == "__main__":
    unittest.main()

