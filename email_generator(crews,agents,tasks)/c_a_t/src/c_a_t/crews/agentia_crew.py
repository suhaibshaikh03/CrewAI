from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class AgentCrew:
    """Agent Crew"""

    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def email_composer(self) -> Agent:
        return Agent(
            config=self.agents_config["email_composer"],
        )

    @task
    def write_email(self) -> Task:
        return Task(
            config=self.tasks_config["write_email"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
