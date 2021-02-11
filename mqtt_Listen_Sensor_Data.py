import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import sensor_Data_Handler

# MQTT Settings 
MQTT_Broker = ""       #Broker ip or address
MQTT_Port = 1883                    #default
Keep_Alive_Interval = 45
MQTT_Topic = "example/test/#"

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc):
	mqttc.subscribe(MQTT_Topic, 0)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
