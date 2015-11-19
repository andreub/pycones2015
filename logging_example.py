import logging

# OneLineExceptionFormatter
class OLEF(logging.Formatter):
   def formatException(self, exc_info):
        result = super(OLEF, self).formatException(exc_info)
        return repr(result)
   def format(self, record):
        s = super(OLEF, self).format(record)
        if record.exc_text: s = s.replace('\n', '')
        return s

def logging_setup(filename):
    logger=logging.getLogger() #root logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    formatter = OLEF('%(asctime)s | %(name)s | %(message)s')
    fh = logging.FileHandler(filename, mode='a')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

class MyDb:
    pass
dryrun=False
def main():
    logging_setup(filename='test.log')
    db = MyDb()
    l = "mordor"
    try:
        if not dryrun:
            logging.info("going to add locality")
            l_id = db.add_locality(l)
        4/0
        logging.debug("ADDED L: %s" % l)
    except Exception as error:
        logging.exception(error)

main()
