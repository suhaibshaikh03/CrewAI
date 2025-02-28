from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM

llm1 = LLM(model="ollama/deepseek-r1:1.5b", base_url="http://localhost:11434")
llm2 = LLM(model="gemini-2.0-flash-exp")

@CrewBase
class DevCrew:
    """Dev Crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["junior_python_developer"],
            llm=llm1,
        )
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_python_developer"],
            llm=llm2,
        )
    
    @task
    def write_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_code"],
        )
    @task
    def review_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_code"],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        

        return Crew(
            agents=self.agents,  
            tasks=self.tasks,  
            process=Process.sequential,
            verbose=True,
        )
