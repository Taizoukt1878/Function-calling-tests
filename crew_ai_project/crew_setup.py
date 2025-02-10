from crewai import Crew, Process
from tasks import task_ui, task_dm, task_rga
from agents import user_interaction_agent, decision_agent, response_generator_agent
from open_ai_client import llm

# Create a Crew instance to orchestrate agents and tasks
crew = Crew(
    agents=[user_interaction_agent, decision_agent, response_generator_agent],
    tasks=[task_ui, task_dm, task_rga],
    process=Process.sequential,
    function_calling_llm=llm,
    verbose=True
)
