echo "##############################################################"
echo "###################  Initialising Test #######################"
echo "##############################################################"
echo "##############################################################"
echo "#################  Validating user inputs ####################"
echo "##############################################################"
cd SmartAPIautomationframework/src/test/java/examples/users/pythonController/
ls
python3 DataValidator.py
echo "##############################################################"
echo "############ User inputs validation Completed ################"
echo "##############################################################"
echo "##############################################################"
echo "############### Generating Feature Files... ##################"
echo "##############################################################"
cd /home/runner/work/Smart-API-Automation/Smart-API-Automation/IdeaProjects/SmartAPIautomationframework/src/test/java/examples/users/pythonController
python3 FeatureGenerator.py
echo "##############################################################"
echo "######### Feature Files Generated Successfully ###############"
echo "##############################################################"
echo "##############################################################"
echo "############# Test Execution Begins... #######################"
echo "##############################################################"
cd /home/runner/work/Smart-API-Automation/Smart-API-Automation/IdeaProjects/SmartAPIautomationframework/src/test/java/examples/users/pythonController
python3 ReportGenerator.py
read -n 1 -p prompt
