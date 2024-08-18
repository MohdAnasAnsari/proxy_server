# src/utils/logger.py

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='logs/events.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

def log_event(event):
    """Log an event."""
    logging.info(event)

def log_error(error):
    """Log an error."""
    logging.error(error)
