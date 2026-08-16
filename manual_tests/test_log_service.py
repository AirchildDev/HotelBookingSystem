from services.log_service import process_logs
from database.schema import create_tables

create_tables()

process_logs()