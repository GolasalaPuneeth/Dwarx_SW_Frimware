from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

class gadgets:
    
    @staticmethod
    def get_ist_time():
        return datetime.now(IST)
