from qhue import Bridge
import winsound

BRIDGE_IP='192.168.50.58'
USERNAME='OCY9HRvqpGIvDusGAVDwMEV0CMDW1NvacFKvqf8N'
bridge = Bridge(BRIDGE_IP, USERNAME)

def start_game(lights):
    for light in lights:
        bridge.lights[light].state(on=False)

    while bridge.sensors().get('152').get('state').get('presence') == False:
        pass

    for light in lights:
        bridge.lights[light].state(on=True)
    winsound.PlaySound('i_see_you.wav', winsound.SND_ASYNC)

sophie_room_lights = bridge.groups().get('1').get('lights')
living_room_lights = bridge.groups().get('3').get('lights')

start_game(living_room_lights)