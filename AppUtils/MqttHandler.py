import paho.mqtt.publish as publish

publish.single("paho/test/topic", "payload", hostname="mqtt://13.201.128.149:1883")