from crewai import Crew, Process
from tasks import task_dm
from agents import decision_agent
from llm_config import llm
# from typing import Callable
# import streamlit as st

# Custom Tool wrapper to trackS tool usage
# class ToolTracker:
#     def __init__(self, tool: Callable, name: str):
#         self.tool = tool
#         self.name = name
#         self.description = tool.description
#         self._run = tool._run
        
#     def __call__(self, *args, **kwargs):
#         # Update Streamlit with current tool being used
#         st.session_state.current_tool = self.name
#         return self.tool(*args, **kwargs)

# # Function to wrap all tools in an agent
# def wrap_agent_tools(agent: Agent) -> Agent:
#     wrapped_tools = []
#     for tool in agent.tools:
#         wrapped_tool = ToolTracker(tool, tool.name)
#         wrapped_tools.append(wrapped_tool)
#     agent.tools = wrapped_tools
#     return agent

# user_interaction_agent = wrap_agent_tools(user_interaction_agent)
# decision_agent = wrap_agent_tools(decision_agent)


# Create a Crew instance to orchestrate agents and tasks
crew = Crew(
    agents=[decision_agent],
    tasks=[task_dm],
    process=Process.sequential,
    function_calling_llm=llm,
    verbose=True
)
