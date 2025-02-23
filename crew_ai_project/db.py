from psycopg_pool import ConnectionPool
from settings import get_settings
import os
# current_path = os.path.dirname(os.path.abspath(__file__))
# print(f"Current path: {current_path}")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/anouar/Desktop/projects/Function-calling-tests/crew_ai_project/third-opus-411016-07dafea77499.json"

def get_db_pool():
    settings = get_settings()
    gcp_pg_creds = settings.GOOGLE_POSTGRES_CREDENTIALS


    conninfo = (
        f"dbname={gcp_pg_creds['gcp_pg_history_database']} "
        f"user={gcp_pg_creds['gcp_pg_history_user']} "
        f"password={gcp_pg_creds['gcp_pg_history_password']} "
        f"host={gcp_pg_creds['gcp_pg_history_ip']} "
        f"port={gcp_pg_creds['gcp_pg_history_port']} "
        "sslmode=require"
    )

    connection_kwargs = {"autocommit": True, "prepare_threshold": 0}
    pool = ConnectionPool(
        conninfo=conninfo,
        max_size=20,
        min_size=1,
        kwargs=connection_kwargs
    )

    return pool

pool = get_db_pool()
# def fetch_chat_logs():
#     pool = get_db_pool()
#     try:
#         with pool.connection() as conn:
#             with conn.cursor() as cur:
#                 cur.execute("SELECT * FROM chat_logs_time")
#                 chat_logs = cur.fetchall()
#                 return chat_logs
#     except Exception as e:
#         print(f"Error fetching chat logs: {e}")
#         return None

# # Example usage
# if __name__ == "__main__":
#     logs = fetch_chat_logs()
#     if logs:
#         for log in logs:
#             print(log)

