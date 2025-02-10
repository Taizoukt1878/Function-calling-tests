from dotenv import load_dotenv
from crew_setup import crew
from logger import setup_logger

logger = setup_logger()

# Load API key from .env file
load_dotenv()

# Run the Crew AI System
if __name__ == "__main__":
    logger.info("Starting Crew AI system with function calling...")

    while True:
        user_input = input("Ask something (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            logger.info("Shutting down system.")
            break

        # Crew AI dynamically chooses the correct tool
        print(f"User Input: {user_input}")
        structured_request = crew.kickoff(inputs={"user_input": user_input})
        
        print(f"Response: {structured_request}")
