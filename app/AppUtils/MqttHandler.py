from dotenv import load_dotenv
import paho.mqtt.publish as publish
import os
import enum
import asyncio

load_dotenv()

class MqttSecrets(enum.Enum):
    HOST:str = os.getenv('MQTT_HOST')
    PORT:int = int(os.getenv('MQTT_PORT'))

    @classmethod
    def validate(cls):
        required = ['HOST','PORT']
        for field in required:
            if not getattr(cls, field).value:
                raise ValueError(f"Missing required field: {field}")
            
MqttSecrets.validate()

async def trigger_esp(Customer:str,
                      Liters:float,
                      Topic:str,
                      Host:str=MqttSecrets.HOST.value,
                      port:int=MqttSecrets.PORT.value) -> None:
    
    payload = f'{{"Customer": "{Customer}", "Liters": {Liters}}}'

    publish.single(topic=Topic,
                   payload=payload,
                   hostname=Host,
                   port=port,
                   qos=1)

# asyncio.run(trigger_esp("Sam",1.0,"paho/test/topic"))