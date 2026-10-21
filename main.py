from weather_manager import WeatherManager
from twilio_manager import TwilioManager
from infobip_manager import InfobipManager

LOCATION_LAT = 61.035965
LOCATION_LNG = 69.047623


wm = WeatherManager(LOCATION_LAT, LOCATION_LNG)
if wm.check_for_rain():
    tm = TwilioManager()
    tm.send_message()

    infom = InfobipManager()
    infom.send_message()
