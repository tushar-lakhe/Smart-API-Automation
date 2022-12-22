echo "##############################################################"
echo "###################  Initialising Test #######################"
echo "##############################################################"
echo "##############################################################"
echo "#################  Validating user inputs ####################"
echo "##############################################################"
python3 /home/runner/work/Smart-API-Automation/Smart-API-Automation/IdeaProjects/SmartAPIautomationframework/src/test/java/examples/users/pythonController/DataValidator.py
echo "##############################################################"
echo "############ User inputs validation Completed ################"
echo "##############################################################"
echo "##############################################################"
echo "############### Generating Feature Files... ##################"
echo "##############################################################"
python3 /home/runner/work/Smart-API-Automation/Smart-API-Automation/IdeaProjects/SmartAPIautomationframework/src/test/java/examples/users/pythonController/FeatureGenerator.py
echo "##############################################################"
echo "######### Feature Files Generated Successfully ###############"
echo "##############################################################"
echo "##############################################################"
echo "############# Test Execution Begins... #######################"
echo "##############################################################"
python3 /home/runner/work/Smart-API-Automation/Smart-API-Automation/IdeaProjects/SmartAPIautomationframework/src/test/java/examples/users/pythonController/ReportGenerator.py
read -n 1 -p prompt
