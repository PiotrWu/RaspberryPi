import thingspeak
import time
import adafruit_dht
import board

channel_id =  # put here the ID of the channel you created before
key = '' # update the "WRITE KEY"

dht_device = adafruit_dht.DHT11(board.D17)

def measure(channel):
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if humidity is not None and temperature is not None:
            print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
        else:
            print('Did not receive any reading from sensor. Please check!')
        # update the value
        response = channel.update({'field1': temperature, 'field2': humidity})
    except:
           print("connection failure")

if __name__ == "__main__":
        channel = thingspeak.Channel(id=channel_id, api_key=key)
        while True:
            measure(channel)
        #free account has a limitation of 15sec between the updates
            time.sleep(15)

