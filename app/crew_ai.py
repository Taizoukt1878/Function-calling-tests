import os
from crewai import Agent, Task, Crew, LLM
# from dotenv import load_dotenv
# from openai import OpenAI

# Load API key from .env file
os.environ["OPENAI_API_KEY"] = "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"
# load_dotenv(dotenv_path=".env")
print(os.getenv("OPENAI_API_KEY"))
llm = LLM(model="nvidia_nim/meta/llama-3.1-70b-instruct", base_url="https://integrate.api.nvidia.com/v1")

# Sample predefined functions
def get_weather(city):
    return f"The weather in {city} is sunny with 25°C."

def get_time():
    from datetime import datetime
    return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

# Define the Decision-Making Agent (DMA)
decision_agent = Agent(
    role="Decision-Making Agent",
    goal="Determine the correct function to execute based on user requests.",
    backstory="A highly efficient AI system designed to process user requests and execute predefined functions.",
    allow_delegation=False,
    llm=llm,
    # tools=[get_weather, get_time]
)

# Define the User Interaction Agent (UIA)
user_interaction_agent = Agent(
    role="User Interaction Agent",
    goal="Engage with the user, process their requests, and forward structured data.",
    backstory="A friendly AI that interacts with users and ensures their requests are understood.",
    allow_delegation=True,
    llm=llm
)

# Define the Task for UIA
task_ui = Task(
    description="Receive user input and structure the request for processing.",
    agent=user_interaction_agent,
    expected_output="Receive user input and structure the request for processing.",
)

# Define the Task for DMA
task_dm = Task(
    description="Analyze the request and execute the correct function.",
    agent=decision_agent,
    expected_output="Analyze the request and execute the correct function using tools."
)

# Create a Crew to orchestrate the agents
crew = Crew(
    agents=[user_interaction_agent, decision_agent],
    tasks=[task_ui, task_dm],
    verbose=True
)

# Function to process user input
def process_request(user_input):
    if "weather" in user_input.lower():
        return get_weather("Casablanca")
    elif "time" in user_input.lower():
        return get_time()
    else:
        return "Sorry, I don't understand that request."

# Run the Crew AI System
while True:
    user_input = input("Ask something (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    structured_request = crew.kickoff(inputs={"user_input": user_input})
    result = process_request(user_input)
    
    print(f"Response: {structured_request}")
