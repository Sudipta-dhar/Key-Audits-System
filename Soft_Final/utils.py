import logging

logging.basicConfig(filename='audit.log', level=logging.INFO)

def log_operation(username, operation):
    logging.info(f'User: {username}, Operation: {operation}, Status: Success')
