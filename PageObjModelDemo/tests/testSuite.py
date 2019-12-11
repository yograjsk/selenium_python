import unittest
from PageObjModelDemo.tests.googleSearchTest import GoogleSearch
from PageObjModelDemo.tests.newLogin import NewLoginTests
from PageObjModelDemo.tests.loginTests import LoginTests
from PageObjModelDemo.Utilities.Utils import Utils



testCase1 = unittest.TestLoader().loadTestsFromTestCase(GoogleSearch)
testCase2 = unittest.TestLoader().loadTestsFromTestCase(NewLoginTests)
testCase3 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

smokeTest = unittest.TestSuite([testCase1, testCase2])
regressionTest = unittest.TestSuite([testCase1, testCase2, testCase3])

u = Utils()
config = u.propertiesFileReader("../Configuration/config.properties")
suiteToRun = config["suiteName"]

# unittest.TextTestRunner().run(regressionTest)

if suiteToRun == 'smoke':
    print("Running Smoke Suite")
    unittest.TextTestRunner().run(smokeTest)
if suiteToRun == "regression":
    print("Running Regression Suite")
    unittest.TextTestRunner().run(regressionTest)

