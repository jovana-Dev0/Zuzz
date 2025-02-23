import logging

def setup_logger():
    logging.basicConfig(
        filename="zuzz.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("Zuzz")

logger = setup_logger()
