echo off
echo ##############################################################

echo ###################  Initialising Test #######################

echo ##############################################################


echo ##############################################################

echo ################  Validating user inputs  ####################

echo ##############################################################
cd %~dp0\\SmartAPIautomationframework\src\test\java\

python -m examples.users.pythonController.DataValidator

echo ##############################################################

echo ################ User inputs validation Completed ###########

echo ##############################################################

echo ##############################################################

echo ################  Generating Feature Files  ##################

echo ##############################################################

cd  %~dp0\\SmartAPIautomationframework\src\test\java\

python -m examples.users.pythonController.FeatureGenerator

echo ##############################################################

echo ###########  Feature Files Generated successfully ############

echo ##############################################################

cd %~dp0\\SmartAPIautomationframework\

echo ##############################################################

echo ###################  Test Execution begins  ###################

cd  %~dp0\\SmartAPIautomationframework\src\test\java\

python -m examples.users.pythonController.ReportGenerator


pause


