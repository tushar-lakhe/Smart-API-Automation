
Feature: r_Test_case_01 Post Request

	Background:
		 * configure report = { showLog: true, showAllSteps: false }
		 * def r_Test_case_01 = {     'id': 'e3be2fba15a2452cb28bf1b08bd7',     'emailAddress': 'pratyush.gupta@takeda.com',     'firstName': 'Suzuki',     'lastName': 'Snow',     'typeRetail': false,     'typeInstitutional': false,     'typeOther': false,     'typeMedia': true,     'company': 'NetStreet',     'prefPressRelease': false,     'prefQE': false,     'prefEvents': false,     'prefStories': false,     'language': 'JP'   }

	Scenario: POST User Scenario for r_Test_case_01

		Given url "https://api-us-aws-uat2.takeda.com/uat/gca-investorsignup-api/v1/investor/signup"
		And request r_Test_case_01
		When method POST
		Then status 201
