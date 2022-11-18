echo off
timeout 5 >nul
echo ##############################################################

echo ################  starting with execution ####################

echo ##############################################################



echo ##############################################################

echo ################  Validating user inputs  ####################

echo ##############################################################

cd %~dp0\\src\test\java

python -m examples.users.pythonController.DataValidator

echo ##############################################################

echo ################  User inputs validation Completed ###########

echo ##############################################################


echo ##############################################################

echo ################  Generating Feature Files  ##################

echo ##############################################################

cd  %~dp0\\src\test\java\

python -m examples.users.pythonController.FeatureGenerator

echo ##############################################################

echo ############  Feature Files Generated successfully ############

echo ##############################################################

cd %~dp0\\
echo ##############################################################

echo ###################  Test Execution begins  ###################

echo ##############################################################

call mvn clean test


timeout 3 >nul

echo ##############################################################

echo ############## Api execution completed....####################

echo ##############################################################

timeout 5 >nul

timeout 5 >nul

echo ##############################################################

echo ############# opening cucumber report.....####################  

echo ##############################################################

cd  %~dp0\\src\test\java\

python -m examples.users.pythonController.ReportGenerator

timeout 7 >nul

echo ##############################################################

echo ########## Starting Performance Test execution.###############

echo ##############################################################

timeout 2 >nul
cd %~dp0\\
call mvn clean test-compile gatling:test
timeout 5 >nul

echo ##############################################################

echo ############# opening gatling report.....####################  

echo ##############################################################

cd  %~dp0\\src\test\java\

python -m examples.users.pythonController.repoGenGatling



pause


