from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from c_a_t.crews.agentia_crew import AgentCrew
from random import randint

class State(BaseModel):
    word : int = 200
    email : str = ""

class AgenticFlow(Flow[State]):
    @start()
    def generate_word_count(self):
        print("Generate word count")
        self.state.word = randint(150,200)

    @listen(generate_word_count)
    def generate_email(self):
        print("Generating Email")
        result = (
            AgentCrew()
            .crew()
            .kickoff(inputs={"word": self.state.word})
        )
        self.state.email = result.raw

    @listen(generate_email)
    def save_email(self):
        print("saving email")
        with open("email.txt", "w") as f:
            f.write(self.state.email)


def kickoff():
    obj = AgenticFlow()
    obj.kickoff()

def plot():
    obj = AgenticFlow()
    obj.plot()