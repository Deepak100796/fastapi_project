import logging

logger = logging.getLogger("uvicorn.access")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.setLevel(logging.INFO)
logger.addHandler(handler)
