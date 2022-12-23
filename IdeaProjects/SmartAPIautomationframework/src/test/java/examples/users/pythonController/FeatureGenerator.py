import ujson as json
import config_url as conf
import os

for k, v in conf.url.items():
    if k == "jsonforkarate":
        featureinputjson = v
    elif k == "testcases_api":
        testcases_api = v
    elif k == "simulation_file_path":
        simulation_file_path = v
    elif k == "testcases_perf":
        testcases_perf = v

json_for_karate = open(featureinputjson)
dict3 = json.load(json_for_karate)


class MethodCall:

    def post_method(self):
        #file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
        #file1.write(' * def ' + i["test_case_id"] + " = " + str(i["json_payload"]))
        if i["headers"] != None:
            file1.write('\n\t\t * def ' + i["test_case_id"] + "_headers" + " = " + str(i["headers"]))
            file1.write('\n\n\tScenario: POST User Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\t' + 'Given url ' + '"' + i["url"] + '"')
            file1.write("\n\t\tAnd headers " + i["test_case_id"] + "_headers")
            file1.write("\n\t\tAnd request " + i["test_case_id"] + "\n")
        elif i["headers"] == None:
            file1.write('\n\n\tScenario: POST User Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\t' + 'Given url ' + '"' + i["url"] + '"')
            file1.write("\n\t\tAnd request " + i["test_case_id"] + "\n")
        file1.write("\t\tWhen method POST\n\t\tThen status " + str(i["status"]) + "\n")

        file1.close()

    def get_method(self):
        if i["headers"] != None:
            file1.write(' * def ' + i["test_case_id"] + "_headers" + " = " + str(i["headers"]))
            file1.write('\n\n\tScenario: GET Request Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\tGiven url ' + '"' + i["url"] + '"')
            file1.write("\n\t\tAnd headers " + i["test_case_id"] + "_headers")
        elif i["headers"] == None:
            file1.write('\n\n\tScenario: GET Request Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\tGiven url ' + '"' + i["url"] + '"')
        file1.write("\n\t\tWhen method GET\n\t\tThen status " + str(i["status"]) + "\n")

        file1.close()

    def put_method(self):
        if i["headers"] != None:
            file1.write('\n\t\t * def ' + i["test_case_id"] + "_headers" + " = " + str(i["headers"]))
            file1.write('\n\n\tScenario: Put User Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\t' + 'Given url ' + '"' + i["url"] + '"')
            file1.write("\n\t\tAnd headers " + i["test_case_id"] + "_headers")
            file1.write("\n\t\tAnd request " + i["test_case_id"] + "\n")
        elif i["headers"] == None:
            file1.write('\n\n\tScenario: Put User Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\t' + 'Given url ' + '"' + i["url"] + '"')
            file1.write("\n\t\tAnd request " + i["test_case_id"] + "\n")
        file1.write("\t\tWhen method PUT \n\t\tThen status " + str(i["status"]) + "\n")

        file1.close()

    def delete_method(self):
        if i["headers"] != None:
            file1.write(' * def ' + i["test_case_id"] + "_headers" + " = " + str(i["headers"]))
            file1.write('\n\n\tScenario: DELETE Request Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\tGiven url ' + '"' + i["url"] + '"')
            file1.write("\n\t\tAnd headers " + i["test_case_id"] + "_headers\n")
        elif i["headers"] == None:
            file1.write('\n\n\tScenario: DELETE Request Scenario for ' + i["test_case_id"])
            file1.write('\n\n\t\tGiven url ' + '"' + i["url"] + '"')
        file1.write("\n\t\tWhen method DELETE\n\t\tThen status " + str(i["status"]) + "\n")

        file1.close()

    def queue_method(self):
        file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
        file1.write(' * def ' + "queueUtils" + " = " + "Java.type('examples.users.queueUtils')\n\t\t")
        file1.write(' * def ' + 'queueRequestBody = ("' + str(i["json_payload"]).replace('"', "'") + '")\n\t\t')
        file1.write(' * def ' + 'username = ("' + str(i["username"]) + '")\n\t\t')
        file1.write(' * def ' + 'password = ("' + str(i["password"]) + '")')
        #                if i["headers"] != None:
        #                    for k, v in eval(i["headers"]).items():
        #                        file1.write("\n\t\t * def "+k+" = '"+v+"'")
        file1.write("\n\t\t * def connectionUrl = '" + i["url"] + "'")
        file1.write("\n\t\t * def delay =  20")
        file1.write('\n\n\tScenario: Message Queue Scenario for ' + i["test_case_id"])
        file1.write("\n\n\t\tGiven queueUtils.createConnection(connectionUrl, username, password)")
        if i['mq_message_type'] == 'TextMessage':
            file1.write("\n\t\tWhen queueUtils.sendText('" + i["queue_name"] + "'" + ",queueRequestBody, delay)")
        elif i['mq_message_type'] == 'ObjectMessage':
            file1.write("\n\t\tWhen queueUtils.sendObject('" + i["queue_name"] + "'" + ",queueRequestBody, delay)")
        file1.write("\n\t\tThen print 'Message successfully posted on queue: " + i["queue_name"] + " !!!'")
        file1.close()


method = MethodCall()

## Feature file generation for Api test ####

for i in dict3:
    if i["execution_flag"] == "Api" or i["execution_flag"] == "Both":

        try:
            if i["method"] == 'POST' and i["json_payload"] != "None":
                #print("POST Method")
                file1 = open(testcases_api + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def ' + i["test_case_id"] + " = " + str(i["json_payload"]))
                method.post_method()
                with open(testcases_api + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_api + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            elif i["method"] == 'GET':
                #print("GET Method")
                file1 = open(testcases_api + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                method.get_method()
                with open(testcases_api + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_api + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            elif i["method"] == 'PUT' and i["json_payload"] != "None":
                #print("PUT Method")
                file1 = open(testcases_api + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def ' + i["test_case_id"] + " = " + str(i["json_payload"]))
                method.put_method()
                with open(testcases_api + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_api + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            elif i["method"] == 'DELETE':
                file1 = open(testcases_api + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                method.delete_method()
                with open(testcases_api + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_api + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

        except:
            if i["queue_type"] == "active_mq" and i["json_payload"] != "None" and i["queue_name"] != None and i["username"] != None and i["password"] != None:
                file1 = open(testcases_api + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' Queue message request\n')
                method.queue_method()
                with open(testcases_api + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_api + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            if i["queue_type"] == "kafka_mq" and i["json_payload"] != "None" and i["queue_name"] != None and i["username"] != None and i["password"] != None:
                file1 = open(testcases_api + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' Queue message request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def ' + "kafkaUtils" + " = " + "Java.type('examples.users.Kafka')\n\t\t")
                file1.write(' * def ' + 'topicRequestBody = ("' + str(i["json_payload"]).replace('"', "'") + '")\n\t\t')
                file1.write(' * def ' + 'username = ("' + str(i["username"]) + '")\n\t\t')
                file1.write(' * def ' + 'password = ("' + str(i["password"]) + '")')
                #                if i["headers"] != None:
                #                    for k, v in eval(i["headers"]).items():
                #                        file1.write("\n\t\t * def "+k+" = '"+v+"'")
                file1.write("\n\t\t * def connectionUrl = '" + i["url"] + "'")
                file1.write('\n\n\tScenario: Message Queue Scenario for ' + i["test_case_id"])
                file1.write("\n\n\t\tGiven kafkaUtils.connect(connectionUrl, username, password)")
                file1.write("\n\t\tWhen kafkaUtils.send('" + i["queue_name"] + "'" + ",topicRequestBody)")
                file1.write("\n\t\tThen print 'Message successfully posted on queue: " + i["queue_name"] + " !!!'")
                file1.close()



    ## Feature file generation for perf test ####

    if i["execution_flag"] == "Performance" or i["execution_flag"] == "Both":
        try:
            if i["method"] == 'POST' and i["json_payload"] != "None":
                #print("POST Method")
                file1 = open(testcases_perf + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def ' + i["test_case_id"] + " = " + str(i["json_payload"]))
                method.post_method()
                with open(testcases_perf + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_perf + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            elif i["method"] == 'GET':
                #print("GET Method")
                file1 = open(testcases_perf + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                method.get_method()
                with open(testcases_perf + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_perf + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            elif i["method"] == 'PUT' and i["json_payload"] != "None":
                #print("PUT Method")
                file1 = open(testcases_perf + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                file1.write(' * def ' + i["test_case_id"] + " = " + str(i["json_payload"]))
                method.put_method()
                with open(testcases_perf + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_perf + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

            elif i["method"] == 'DELETE':
                file1 = open(testcases_perf + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' ' + i["method"] + ' Request\n')
                file1.write('\n\tBackground:\n\t\t * configure report = { showLog: true, showAllSteps: false }\n\t\t')
                method.delete_method()
                with open(testcases_perf + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_perf + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

        except:
            if i["json_payload"] != "None" and i["queue_name"] != None and i["username"] != None and i["password"] != None:
                file1 = open(testcases_perf + i["test_case_id"] + ".feature", "w")
                file1.write('\nFeature: ' + i["test_case_id"] + ' Queue message request\n')
                method.queue_method()
                with open(testcases_perf + i["test_case_id"] + ".feature", 'r+') as f:
                    file_source = f.read()
                    replace_string = file_source.replace(': False', ': false').replace(': True', ': true')
                with open(testcases_perf + i["test_case_id"] + ".feature", "w") as file:
                    file.write(replace_string)

## Simulation file generator ####

for j in dict3:
    if j["execution_flag"] == "Performance" or j["execution_flag"] == "Both":
        file2 = open(simulation_file_path + "simulation.scala", "w")
        file2.write('package examples.users.simulation_files\n')
        file2.write(
            '\nimport com.intuit.karate.gatling.PreDef._\nimport io.gatling.core.Predef._\nimport scala.concurrent.duration._\nimport scala.language.postfixOps')
        file2.write('\n\nclass simulation extends Simulation{')

if os.path.exists(os.path.join(simulation_file_path, 'simulation.scala').replace('\\', '/')):
    for j in dict3:
        if j["number_of_concurrent_users"] != None and j["duration_of_run_in_seconds"] != None and (
                j["execution_flag"] == "Performance" or j["execution_flag"] == "Both"):
            file2.write('\n\tval ' + j["test_case_id"] + ' = scenario( "' + (
                str(j["test_case_id"])) + '"' + ').exec(karateFeature("classpath:examples/users/test_cases/perf/' + j[
                            "test_case_id"] + '.feature"))')
    file2.write('\n\tsetUp(\n\t\t')
    for j in dict3:
        if j["number_of_concurrent_users"] != None and j["duration_of_run_in_seconds"] != None and (
                j["execution_flag"] == "Performance" or j["execution_flag"] == "Both"):
            file2.write(j["test_case_id"] + '.inject(constantConcurrentUsers(' + str(
                j["number_of_concurrent_users"]) + ') during(' + str(
                j["duration_of_run_in_seconds"]) + '.seconds)),\n\t\t')
    file2.write('\n\t)\n}')
