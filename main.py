from time import sleep

from session import Session
from utils import configure_logging

def main():
    logger = configure_logging()
    session = Session(base_url="https://localhost:5000/v1/api/")
    while True:
        try:
            auth_response = session.auth_status()
            logger.info(f"Session is authenticated and not competing - data: {auth_response}")
            session.keep_alive()
        except Exception as auth_exception:
            logger.error(auth_exception)
            session.reauthenticate()
        finally:
            sleep(10)

if __name__ == "__main__":
    main()