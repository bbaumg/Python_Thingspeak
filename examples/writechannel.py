import Thingspeak

THINGSPEAK_CHANNEL		= 00000
THINGSPEAK_KEY			= '---KEY-HERE-----'

channel = Thingspeak.Thingspeak(channel=THINGSPEAK_CHANNEL, apiKey=THINGSPEAK_KEY)
channel.field[channel.field_name(name='Field1')] = 100
channel.post_update()

