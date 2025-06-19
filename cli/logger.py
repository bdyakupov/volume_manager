import logging
import os


# create logs directory if not exist
os.makedirs("logs", exist_ok=True)


# logger settings
logging.basicConfig(
    filename="logs/cli.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# disable httpx internal logger
logging.getLogger("httpx").disabled = True


def log_action(func):
    async def wrapper(*args, **kwargs):
        command = func.__name__.replace("_", "-")
        logging.info(f"Command: {command} | Arguments: {kwargs}")
        try:
            result = await func(*args, **kwargs)
            logging.info(f"Result '{command}': success")
            return result
        except Exception as e:
            logging.error(f"Runtime error: '{command}': {str(e)[:50]}")
            raise e
    return wrapper