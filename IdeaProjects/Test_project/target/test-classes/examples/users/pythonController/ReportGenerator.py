import os
import webbrowser
import configparser
import shutil
import datetime
import examples.users.config_url as conf
from pathlib import Path
import glob

import subprocess

ini_path = Path(__file__).parents[6]
iniFilepath = os.path.join(ini_path,'config.ini').replace('\\', '/')
config = configparser.ConfigParser()
config.read(iniFilepath)
historytestcases = config["url"]["history_testcases"]
historyreports = config["url"]["history_report"]

for k, v in conf.url.items():
    # read parameter excel
    if k == "report":
        report = v
    elif k == "testcases":
        testcases = v
    elif k == "gatling_report_path":
        gatling_report_path = v

#config = configparser.ConfigParser()
#config.read(r"C:\Users\tushar.khushal.lakhe\IdeaProjects\KarateDemo\src\test\java\examples\users\config.ini")

#print(historytestcases)
#print(historyreports)

now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H%M%S"))

#print((os.path.join(report,'overview-features.html')))


#subprocess.call(["mvn", "clean", "test","-compile gatling:test"], shell=True)

# report moving

source_report = report
destination_report = os.path.join(historyreports,timestamp+"/")
shutil.copytree(source_report, destination_report)

# Report Opening
webbrowser.open_new_tab(os.path.join(historyreports,timestamp+"/",'overview-features.html'))
"""
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




for f in glob.glob(gatling_report_path+'\*'):
    a = (os.path.split(f)[-1])
gatling_report = os.path.join(gatling_report_path,a,'index.html').replace('\\', '/')

print(a)
src_gatling_report = gatling_report
dest_gatling_report = os.path.join(historyreports,'gatling_reports',timestamp+"/")
shutil.copytree(src_gatling_report, dest_gatling_report)

webbrowser.open_new_tab(os.path.join(historyreports,'gatling_reports',timestamp+"/",'overview-features.html'))

print(gatling_report)
"""