
Feature: r_Test_case_03 Post Request

	Background:
		 * configure report = { showLog: true, showAllSteps: false }
		 * def r_Test_case_03 = {     'id': 'e3be2fba15a2452cb28bf1b08bd7',     'emailAddress': 'pratyush.gupta@takeda.com',     'firstName': 'Suzuki',     'lastName': 'Snow',     'typeRetail': false,     'typeInstitutional': false,     'typeOther': false,     'typeMedia': true,     'company': 'NetStreet',     'prefPressRelease': false,     'prefQE': false,     'prefEvents': false,     'prefStories': false,     'language': 'JP'   }
		 * def r_Test_case_03_headers = {'client_id': '6fbe28135b1c4e10a0b10dccb21889f3', 'client_secret': '7a35C5150CE7404CAeF0492274024ef8'}

	Scenario: POST User Scenario for r_Test_case_03

		Given url "https://api-us-aws-uat2.takeda.com/uat/gca-investorsignup-api/v1/investor/signup"
		And headers r_Test_case_03_headers
		And request r_Test_case_03
		When method POST
		Then status 201
