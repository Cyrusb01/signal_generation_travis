import os

from dotenv import load_dotenv

load_dotenv()


RESEARCH_DB_USER = os.getenv("RESEARCH_DB_USER")
RESEARCH_DB_PASS = os.getenv("RESEARCH_DB_PASS")
RESEARCH_DB_HOST = os.getenv("RESEARCH_DB_HOST")
RESEARCH_DB_PORT = os.getenv("RESEARCH_DB_PORT")
RESEARCH_DB_NAME = os.getenv("RESEARCH_DB_NAME")

SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
SLACK_TOKEN = os.getenv("SLACK_CHANNEL")

RESEARCH_PG_URI = f"postgresql://{RESEARCH_DB_USER}:{RESEARCH_DB_PASS}@{RESEARCH_DB_HOST}:{RESEARCH_DB_PORT}/{RESEARCH_DB_NAME}"
