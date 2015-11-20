import csv
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__file__)

def load_csv(filename):
  logger.info("load csv")
  with open(filename, "rb") as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter="\t")
    items = [r for r in spamreader]
    logger.debug("items: {}".format(len(items)))
    return spamreader.fieldnames, items

header, data = load_csv("logging_basic.csv")