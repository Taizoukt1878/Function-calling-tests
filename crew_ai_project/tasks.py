from crewai import Task
from agents import decision_agent

# Define the Task for UIA
# task_ui = Task(
#     description="Receive user input and structure the request for processing.",
#     agent=user_interaction_agent,
#     expected_output="a clear explanation of the user's request"

# )

# Define the Task for DMA, enabling it to call tools
task_dm = Task(
    description="Analyze the received request and execute the correct tools.",
    agent=decision_agent,
    expected_output="a human-readable response based the result of the executed function"

)
# # Define the Task for RGA
# task_rga = Task(
#     description="Generate a human-readable response from the decision agent's response.",
#     agent=response_generator_agent,
#     expected_output="a human-readable response based on the decision agent's response"
# )
