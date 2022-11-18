
Feature: rest_Test_case_01 GET Request

	Background:
		 * configure report = { showLog: true, showAllSteps: false }
		 * def rest_Test_case_01_headers = {'client_id': 'ea3de08abe424c47a5cb157366741538','client_secret': '7cFf22441B4441FE91E6F31cFA0bE6F3'}

	Scenario: GET Request Scenario for rest_Test_case_01

		Given url "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/fd604b43-365c-42e8-810f-733a2b7f411f/american-flights-api/2.0.1/m/flights?destination=SFO"
		And headers rest_Test_case_01_headers
		When method GET
		Then status 200
