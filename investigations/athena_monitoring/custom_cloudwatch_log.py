# https://github.com/kislyuk/watchtower

import watchtower, logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler(log_group_name="soumaya_test"))
logger.info(dict(table="apple", details={}))
logger.info(dict(table="banana", details={}))
logger.info(dict(table="orange", details={}))
logger.info(dict(table="apple", details={}))


# Log Insights query:
# stats count(@timestamp) by table
# orange 1
# apple 2
# banana 1