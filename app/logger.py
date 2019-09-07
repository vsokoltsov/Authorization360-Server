import os
import logging
import google.cloud.logging  # Don't conflict with standard logging
from google.cloud.logging.handlers import CloudLoggingHandler, setup_logging

PLATFORM = os.environ.get('PLATFORM')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if PLATFORM == 'GCP':
    client = google.cloud.logging.Client()
    handler = CloudLoggingHandler(client)
    setup_logging(handler)

