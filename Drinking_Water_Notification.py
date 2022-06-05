from ast import While
import time
from plyer import notification
if __name__=="__main__":
    #while True:
        notification.notify(
          title="Please Drink Water",
          message="HEY AVINASH YOU NEED TO DRINK WATER",
          app_name="Water Notification",
          app_icon="icon.ico",
          timeout=12
    )
#time.sleep(30)