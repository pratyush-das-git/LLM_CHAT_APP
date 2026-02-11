import logging

def get_logger(name="chatbot"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler=logging.StreamHandler()
    # Create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    handler.setFormatter(formatter)

    # Add the handlers to the logger
    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger