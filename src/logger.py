import logging
import os
from datetime import datetime

# Define the log file name using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the absolute path for the 'logs' directory
logs_path = os.path.join(os.getcwd(), "logs")

# Create the 'logs' folder if it does not exist already
os.makedirs(logs_path, exist_ok=True)

# Combine the folder path and file name to get the final log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test block to verify if logging execution operates cleanly
if __name__ == "__main__":
    logging.info("Logging has started successfully.")