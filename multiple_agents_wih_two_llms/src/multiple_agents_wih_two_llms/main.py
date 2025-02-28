from crewai.flow.flow import start, listen, Flow
from multiple_agents_wih_two_llms.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):
    @start()
    def run_dev_crew(self):
        output = (
            DevCrew()
            .crew()
            .kickoff(inputs={"problem":"write python code for addition two numbers"})
        )
        return output.raw
    


def kickoff():
    obj = DevFlow()
    result = obj.kickoff()
    print(result)

