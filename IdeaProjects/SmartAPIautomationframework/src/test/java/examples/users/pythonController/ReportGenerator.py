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

now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H%M%S"))

print(ini_path)
    
if len(os.listdir(testcases_api)) != 0:
    os.chdir(ini_path)
    subprocess.run('mvn clean test')
    # report moving
    source_report = report
    destination_report = os.path.join(historyreports,'cucumber_api',timestamp+"/")
    shutil.copytree(source_report, destination_report)
    print("########################### API Test Execution Completed ###################################")
    # Report Opening
    print("############################## Opening Api Test Report #####################################")
    webbrowser.open_new_tab(os.path.join(historyreports,'cucumber_api',timestamp+"/",'overview-features.html'))

if Path(os.path.join(simulation_file_path,'simulation.scala')).is_file():
    os.chdir(os.path.join(ini_path,'IdeaProjects'))
    subprocess.run('mvn clean test-compile gatling:test')
    source_report = gatling_report_path
    destination_report = os.path.join(historyreports,'gatling_performance/',timestamp+"/")
    shutil.copytree(source_report, destination_report)
    print("############################ Performance Test Execution Completed ##################################")
    for f in glob.glob(destination_report+'*'):
        a = (os.path.split(f)[-1])
        if a.startswith('simulation'):
            print("############################## Opening Perf Test Report #####################################")
            webbrowser.open_new_tab(os.path.join(historyreports,'gatling_performance',timestamp+"/",a,'index.html'))

# deleting data from intermidiate json

file = open(intemidiate_json, "w")
file.truncate()
file.close()

# testcases moving and deleting

#source_testcases = testcases_api
#destination = os.path.join(historytestcases,timestamp)
#shutil.copytree(testcases_api, destination)

api_tc = testcases_api
for files in os.listdir(api_tc):
    path = os.path.join(api_tc, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)

perf_tc = testcases_perf
for files in os.listdir(perf_tc):
    path = os.path.join(perf_tc, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)


# deleting simulation file
try:
    os.remove(simulation_file_path+'simulation.scala')
except OSError:
    exit()
