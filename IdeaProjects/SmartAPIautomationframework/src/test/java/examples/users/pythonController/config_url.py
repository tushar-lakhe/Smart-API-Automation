import os
import configparser
from pathlib import Path

reportpath = Path(__file__).parents[6]
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config = configparser.ConfigParser()
param_path = os.path.join(path,'inputData','ParameterFile.xlsx').replace('\\', '/')
json_path = os.path.join(path,'intermidiateFiles','karate_src.json').replace('\\', '/')
testcases_path_api = os.path.join(path,'test_cases/api/').replace('\\', '/')
testcases_path_perf = os.path.join(path,'test_cases/perf/').replace('\\', '/')
report_path = os.path.join(reportpath,'target','cucumber-html-reports').replace('\\', '/')
simulation_file_path = os.path.join(path,'simulation_files/').replace('\\', '/')
gatling_report_path = os.path.join(reportpath,'target','gatling').replace('\\', '/')


#print(testcases_path_perf)

url = {
    "input_parameter_file": param_path,
    "jsonforkarate": json_path,
    "testcases_api": testcases_path_api,
    "testcases_perf": testcases_path_perf,
    "report": report_path,
    "simulation_file_path": simulation_file_path,
    "gatling_report_path": gatling_report_path
}

#print(os.path.normpath(os.getcwd() + os.sep + os.pardir))
#print(os.chdir('../Test/src/test/java'))




