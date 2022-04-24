import logging
from Thingspeak import Thingspeak

# packages needed:
#   sudo apt install python3-pip python3-virtualevn
#   pip install RPi.GPIO
#   pip install twilio

# Setup logging
#logLevel = logging.CRITICAL
#logLevel = logging.ERROR
#logLevel = logging.WARNING
#logLevel = logging.INFO
logLevel = logging.DEBUG
logFormat = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
logDateFormat = '%Y-%m-%d %H:%M:%S'
#logHandlers = [logging.FileHandler(logFilename)]
logHandlers = [logging.StreamHandler()]
#logHandlers = [logging.FileHandler(logFilename), logging.StreamHandler()]
logging.basicConfig(level = logLevel, format = logFormat, datefmt = logDateFormat, handlers = logHandlers)
logger = logging.getLogger(__name__)


THINGSPEAK_CHANNEL		= 00000
THINGSPEAK_KEY			= '---KEY-HERE-----'

channel = Thingspeak(channel=THINGSPEAK_CHANNEL, apiKey=THINGSPEAK_KEY)
channel.field[channel.field_name(name='Field1')] = 100
channel.post_update()

