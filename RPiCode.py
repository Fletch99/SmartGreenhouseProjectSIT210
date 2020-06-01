import paho.mqtt.client as mqtt         # Import the MQTT library
import time                 # The time library is useful for delays
 
# Our "on message" event
def messageFunction (client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic + message)
 
 
ourClient = mqtt.Client("makerio_mqtt")     # Create a MQTT client object
ourClient.connect("test.mosquitto.org", 1883)   # Connect to the test MQTT broker
 # Subscribe to the topic AC_unit(Edit this for different Publishes)
 
 #This is where you add differnt messages
 # MAKE SURE WHATS IN THE BRACKETS IS EXACTLY THE SAME AS IN YOUR ARGON CODE

ourClient.subscribe("Greenhouse Temp: ")
ourClient.subscribe("Greenhouse Humidity: ")


ourClient.subscribe("Outdoor Temp: ")
ourClient.subscribe("Outdoor Pressure: ")


ourClient.subscribe("Plant 1 Moisture: ")


ourClient.on_message = messageFunction      # Attach the messageFunction to subscription
ourClient.loop_start()              # Start the MQTT client
 
 
# Main program loop
while(1):
    time.sleep(1)               # Sleep for a second
