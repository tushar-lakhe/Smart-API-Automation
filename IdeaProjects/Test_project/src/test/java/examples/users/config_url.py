import os
import configparser
from pathlib import Path

reportpath = Path(__file__).parents[5]
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config = configparser.ConfigParser()
param_path = os.path.join(path,'inputData','ParameterFile.xlsx').replace('\\', '/')
json_path = os.path.join(path,'intermidiateFiles','karate_src.json').replace('\\', '/')
testcases_path = os.path.join(path,'test_cases/').replace('\\', '/')
simulation_file_path = os.path.join(path,'simulation_files/').replace('\\', '/')
report_path = os.path.join(reportpath,'target','cucumber-html-reports').replace('\\', '/')
gatling_report_path = os.path.join(reportpath,'target','gatling').replace('\\', '/')


url = {
    "input_parameter_file": param_path,
    "jsonforkarate": json_path,
    "testcases": testcases_path,
    "report": report_path,
    "simulation_file_path": simulation_file_path,
    "gatling_report_path": gatling_report_path
}

#print(os.path.normpath(os.getcwd() + os.sep + os.pardir))
#print(os.chdir('../Test/src/test/java'))



