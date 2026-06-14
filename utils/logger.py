import logging


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format=("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"),
        datefmt="%H:%M:%S",
    )
