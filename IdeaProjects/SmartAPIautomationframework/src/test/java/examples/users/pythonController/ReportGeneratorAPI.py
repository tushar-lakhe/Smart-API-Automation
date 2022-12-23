import os
import webbrowser
import configparser
import shutil
import datetime
import config_url as conf
from pathlib import Path
import glob
import os
import subprocess

ini_path = Path(__file__).parents[7]
iniFilepath = os.path.join(ini_path,'config.ini').replace('\\', '/')
config = configparser.ConfigParser()
config.read(iniFilepath)
#historytestcases = config["url"]["history_testcases"]
historyreports = config["url"]["history_report"]

for k, v in conf.url.items():
    # read parameter excel
    if k == "report":
        report = v
    elif k == "testcases_api":
        testcases_api = v
    elif k == "testcases_perf":
        testcases_perf = v
    elif k == "jsonforkarate":
        intemidiate_json = v
    elif k == "simulation_file_path":
        simulation_file_path = v
    elif k == "gatling_report_path":
        gatling_report_path = v

    
if len(os.listdir(testcases_api)) != 0:
    os.chdir(os.path.join(ini_path,'SmartAPIautomationframework'))
    os.system('mvn clean test')
      
