import time
from db import pool
from crew_setup import crew

def create_chat_logs_table(pool=pool):
    """Ensure the chat_logs table exists before logging chats."""
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS chat_logs_time (
                    id SERIAL PRIMARY KEY,
                    agent_name TEXT NOT NULL,
                    user_message TEXT NOT NULL,
                    agent_response TEXT NOT NULL,
                    execution_time FLOAT DEFAULT 0.0,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
    print("✅ Table 'chat_logs_time' is ready!")

def log_chat(agent_name: str, user_message: str, agent_response: str, execution_time : float, pool=pool):
    """Log chat interactions into PostgreSQL using the connection pool."""
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO chat_logs_time (agent_name, user_message, agent_response, execution_time) VALUES (%s, %s, %s, %s)",
                    (agent_name, user_message, agent_response, execution_time)
                )
        print("✅ Chat logged successfully!")
    except Exception as e:
        print(f"❌ Error logging chat: {e}")

# Ensure table exists at startup
create_chat_logs_table()


def run_and_log_crew(user_input: str):
    """Runs the Crew AI system and logs user input & final response."""
    try:
        # Run Crew and get the final response
        start_time = time.time()
        crew_response = crew.kickoff(inputs={"user_input": user_input})
        end_time = time.time()

        # Log the final Crew response
        print("📤 Logging Crew response...")
        log_chat(agent_name="Crew AI", user_message=user_input, agent_response=crew_response.raw, execution_time=end_time-start_time)

        return crew_response
    except Exception as e:
        print(f"❌ Error in Crew execution: {e}")
        return "An error occurred while processing your request."