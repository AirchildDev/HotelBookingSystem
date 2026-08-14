import logging
import os

# Create logs folder if it does not exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/hotel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
