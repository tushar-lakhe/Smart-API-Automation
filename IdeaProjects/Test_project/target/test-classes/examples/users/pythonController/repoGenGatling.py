import os
import webbrowser
import configparser
import shutil
import datetime
import examples.users.config_url as conf
from pathlib import Path
import glob

ini_path = Path(__file__).parents[6]
iniFilepath = os.path.join(ini_path,'config.ini').replace('\\', '/')
config = configparser.ConfigParser()
config.read(iniFilepath)
historytestcases = config["url"]["history_testcases"]
historyreports = config["url"]["history_report"]


for k, v in conf.url.items():
    # read parameter excel
    if k == "testcases":
        testcases = v
    elif k == "gatling_report_path":
        gatling_report_path = v


now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H%M%S"))


# Report moving

source_report = gatling_report_path
destination_report = os.path.join(historyreports,'gatling/',timestamp+"/")
shutil.copytree(source_report, destination_report)

for f in glob.glob(destination_report+'*'):
    a = (os.path.split(f)[-1])
    if a.startswith('simulation'):
        webbrowser.open_new_tab(os.path.join(historyreports,'gatling',timestamp+"/",a,'index.html'))

# testcases moving and deleting

source_testcases = testcases
destination = os.path.join(historytestcases,timestamp)
shutil.copytree(testcases, destination)

dir = testcases
for files in os.listdir(dir):
    path = os.path.join(dir, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
