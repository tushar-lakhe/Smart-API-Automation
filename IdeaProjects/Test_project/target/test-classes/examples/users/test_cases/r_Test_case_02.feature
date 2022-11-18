
Feature: r_Test_case_02 Auth scenario

	Background:
		 * configure report = { showLog: true, showAllSteps: false }		

	Scenario: Oauth Scenario for r_Test_case_02

		Given url "https://oauth.brightcove.com/v4/access_token"
		* form field client_id = 'd8a3a7b4-5af1-43fe-ab09-c634dd7f10fd'
		* form field client_secret = 'v3O3D7hUf6xShy5ondA9Pf2LKwqVA5Jem2KcBQNh8MZT9gHBZXT_4skoXHIheAF5nDudmNYaODV5soLP9fixRQ'
		* form field Content-Type = 'application/x-www-form-urlencoded'
		* form field grant_type = 'client_credentials'
		When method POST
		Then status 200
		* def token_type = response.token_type
		* def access_token = response.access_token

		Given url "https://audience.api.brightcove.com/v1/accounts/3871979173001/view_events?limit=50"
		And header Authorization = token_type+' '+access_token
		When method GET
		Then status 200
