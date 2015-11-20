import ConfigParser
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__file__)

CONFIG_FILE = 'app.conf'

config = ConfigParser.RawConfigParser()
config.read(CONFIG_FILE)

auth_info = config._sections['auth']
print """
user: {user}
pass: {password}
server: {server}
""".format(**auth_info)

try:
  mycolor = config.get('preferences','color')
  print "my defined color: {}".format(mycolor)
except ConfigParser.NoOptionError as error:
  log.error(error)


