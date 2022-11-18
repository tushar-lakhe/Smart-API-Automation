package examples.users.simulation_files

import com.intuit.karate.gatling.PreDef._
import io.gatling.core.Predef._
import scala.concurrent.duration._
import scala.language.postfixOps

class simulation extends Simulation{
	val r_Test_case_01 = scenario(scenarioName = "r_Test_case_01").exec(karateFeature("classpath:examples/users/test_cases/r_Test_case_01.feature"))
	setUp(
		r_Test_case_01.inject(rampUsers(users = 100) during(30 seconds)),
		
	)
}