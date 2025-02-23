from logger import setup_logger
from chat_logs import run_and_log_crew


def main():
    """Main function to run the Crew AI system with logging."""
    logger = setup_logger()
    logger.info("🚀 Starting Crew AI system with function calling...")

    while True:
        user_input = input("Ask something (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            logger.info("🛑 Shutting down system.")
            break

        # Run the Crew AI system and log interactions
        print(f"👤 User Input: {user_input}")
        structured_request = run_and_log_crew(user_input)
        
        print(f"🤖 Response: {structured_request}")

# Run the script
if __name__ == "__main__":
    main()

# from crew_setup import crew
# from logger import setup_logger

# logger = setup_logger()

# # Run the Crew AI System
# if __name__ == "__main__":
#     logger.info("Starting Crew AI system with function calling...")

#     while True:
#         user_input = input("Ask something (or type 'exit' to quit): ")
#         if user_input.lower() == "exit":
#             logger.info("Shutting down system.")
#             break

#         # Crew AI dynamically chooses the correct tool
#         print(f"User Input: {user_input}")
#         structured_request = crew.kickoff(inputs={"user_input": user_input})
        
#         print(f"Response: {structured_request}")