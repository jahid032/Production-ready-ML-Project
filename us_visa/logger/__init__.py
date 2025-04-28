import logging
import os
from datetime import datetime

# Instead of from_root(), directly get the project root
project_root = os.getcwd()  # current working directory when you run demo.py

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'
logs_folder = os.path.join(project_root, log_dir)

# Make sure the folder exists first
os.makedirs(logs_folder, exist_ok=True)

logs_path = os.path.join(logs_folder, LOG_FILE)

# Now configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
