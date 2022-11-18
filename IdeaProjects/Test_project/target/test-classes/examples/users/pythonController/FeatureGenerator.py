import ujson as json
import examples.users.config_url as conf
import os

for k,v in conf.url.items():
    if k == "jsonforkarate":
        featureinputjson = v
    elif k == "testcases":
        testcases = v
    elif k == "simulation_file_path":
        simulation_file_path = v

json_for_karate = open(featureinputjson)
dict3 = json.load(json_for_karate)

#print(dict3)

for i in dict3:
    if i["execution_flag"] == "Yes":
        try:
            if i["method"] == 'POST' and i["json_payload"] != "None":
                file1 = open(testcases+i["test_case_id"]+".feature", "w")
                file1.write('\nFeature: ' +i["test_case_id"] + ' Post Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def '+i["test_case_id"] + " = " + str(i["json_payload"]))
                if i["headers"] != None:
                    file1.write('\n\t\t * def '+i["test_case_id"]+"_headers"+ " = " + str(i["headers"]))
                    file1.write('\n\n\tScenario: POST User Scenario for '+i["test_case_id"])
                    file1.write('\n\n\t\t'+'Given url '+'"'+i["url"]+'"')
                    file1.write("\n\t\tAnd headers "+i["test_case_id"]+"_headers")
                    file1.write("\n\t\tAnd request "+i["test_case_id"] +"\n")
                elif i["headers"] == None:
                    file1.write('\n\n\tScenario: POST User Scenario for '+i["test_case_id"])
                    file1.write('\n\n\t\t'+'Given url '+'"'+i["url"]+'"')
                    file1.write("\n\t\tAnd request "+i["test_case_id"] +"\n")
                file1.write("\t\tWhen method "+str(i["method"])+"\n\t\tThen status "+str(i["status"])+"\n")

                file1.close()
                with open(testcases+i["test_case_id"]+".feature",  'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False',': false').replace(': True',': true')

                with open(testcases+i["test_case_id"]+".feature", "w") as file:
                    file.write(replace_string)
            elif i["method"] == 'GET':
                    file1 = open(testcases+i["test_case_id"]+".feature", "w")
                    file1.write('\nFeature: ' +i["test_case_id"] + ' GET Request\n')
                    if i["headers"] != None:
                        file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                        file1.write(' * def '+i["test_case_id"]+"_headers"+ " = " + str(i["headers"]))
                        file1.write('\n\n\tScenario: GET Request Scenario for '+i["test_case_id"])
                        file1.write('\n\n\t\tGiven url '+'"'+i["url"]+'"')
                        file1.write("\n\t\tAnd headers "+i["test_case_id"]+"_headers\n")
                    elif i["headers"] == None:
                        file1.write('\n\n\tScenario: GET Request Scenario for '+i["test_case_id"])
                        file1.write('\n\n\t\tGiven url '+'"'+i["url"]+'"')
                    file1.write("\t\tWhen method "+str(i["method"])+"\n\t\tThen status "+str(i["status"])+"\n")

                    file1.close()

                    with open(testcases+i["test_case_id"]+".feature",  'r+') as f:
                        file_source = f.read()
                        replace_string = file_source.replace(': False',': false').replace(': True',': true')

                    with open(testcases+i["test_case_id"]+".feature", "w") as file:
                        file.write(replace_string)
            elif str(i["method"]).replace(" ","") == 'POST,GET':
                file1 = open(testcases+i["test_case_id"]+".feature", "w")
                file1.write('\nFeature: ' +i["test_case_id"] + ' Auth scenario\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\t\t')
                file1.write('\n\n\tScenario: Oauth Scenario for '+i["test_case_id"])
                temp_url = ""
                auth = []
                for u in (i["url"].split(",")):
                    file1.write('\n\n\t\tGiven url '+'"'+u+'"')
                    temp_url = u
                    break
                for k,v in eval(i["headers"]).items():
                    file1.write("\n\t\t* form field "+k+" = '"+v+"'")
                file1.write("\n\t\tWhen method POST\n\t\tThen status "+str(i["status"]))
                for p in (i["json_payload"].split(",")):
                        file1.write("\n\t\t* def "+(p).strip()+" = response."+(p).strip())
                        auth.append(p)

                for url in (i["url"].split(",")):
                    if url.strip() != temp_url.strip():
                        file1.write('\n\n\t\tGiven url '+'"'+url.strip()+'"')
                file1.write("\n\t\tAnd header Authorization = "+auth[0]+"+' '+"+(auth[1]).strip())
                file1.write("\n\t\tWhen method GET\n\t\tThen status 200\n")

        except:
            if i["json_payload"] != "None" and i["queue_name"] != None and i["headers"] != None:
                file1 = open(testcases+i["test_case_id"]+".feature", "w")
                file1.write('\nFeature: ' +i["test_case_id"] + ' Queue message request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def '+"queueUtils" + " = " + "Java.type('examples.users.queueUtils')\n\t\t")
                file1.write(' * def '+'queueRequestBody = ("'+str(i["json_payload"])+'")')
                if i["headers"] != None:
                    for k, v in eval(i["headers"]).items():
                        file1.write("\n\t\t * def "+k+" = '"+v+"'")
                file1.write("\n\t\t * def connectionUrl = '"+i["url"]+"'")
                file1.write("\n\t\t * def delay =  20")
                file1.write('\n\n\tScenario: Message Queue Scenario for '+i["test_case_id"])
                file1.write("\n\n\t\tGiven queueUtils.createConnection(connectionUrl, username, password)")
                if i['mq_message_type'] == 'TextMessage':
                    file1.write("\n\t\tWhen queueUtils.sendText('"+i["queue_name"]+"'" +",queueRequestBody, delay)")
                elif i['mq_message_type'] == 'ObjectMessage':
                    file1.write("\n\t\tWhen queueUtils.sendObject('"+i["queue_name"]+"'" +",queueRequestBody, delay)")
                file1.write("\n\t\tThen print 'Message successfully posted on queue: "+i["queue_name"]+" !!!'")
                file1.close()

                with open(testcases+i["test_case_id"]+".feature",  'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False',': false').replace(': True',': true')

                with open(testcases+i["test_case_id"]+".feature", "w") as file:
                    file.write(replace_string)

## Simulation file generator ####
for j in dict3:
    if j["execution_flag"] == "Yes" and j["perf_test"] == 'Yes':
        file2 = open(simulation_file_path+"simulation.scala", "w")
        file2.write('package examples.users.simulation_files\n')
        file2.write('\nimport com.intuit.karate.gatling.PreDef._\nimport io.gatling.core.Predef._\nimport scala.concurrent.duration._\nimport scala.language.postfixOps')
        file2.write('\n\nclass simulation extends Simulation{')

if os.path.exists(os.path.join(simulation_file_path,'simulation.scala').replace('\\', '/')):
    for j in dict3:
        if j["execution_flag"] == "Yes" and j["perf_test"] == 'Yes':
            file2.write('\n\tval '+j["test_case_id"]+' = scenario(scenarioName = "'+(str(j["test_case_id"]))+'"'+').exec(karateFeature("classpath:examples/users/test_cases/'+j["test_case_id"]+'.feature"))')
    file2.write('\n\tsetUp(\n\t\t')
    for j in dict3:
        if j["execution_flag"] == "Yes" and j["perf_test"] == 'Yes':
            file2.write(j["test_case_id"]+'.inject(rampUsers(users = '+str(j["number_of_users"])+') during('+str(j["duration_in_seconds"])+' seconds)),\n\t\t')
    file2.write('\n\t)\n}')
