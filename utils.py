import requests
import json

SENSORS = ['BOILER', 'BOILERS_RETURN', 'FEEDER', ' ', ' ', 'CWU', ' ', ' ', 'CO', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def server_response():
    """[summary]
    
    Function is monitoring Arduino's server with temparatures sensors.
    Returns:
        [json data type]: [boiler's tempartures in json data type]
    """
    data = requests.get('http://192.168.1.2/t.json')
    
    # used json.loads instade data.json()
    json_data = json.loads(data.text, encoding='utf-8')

    # print(type(json_data))

    if data.status_code == 200 and json_data is not None:
        return json_data
    
    else:
        print(f'Server does not response !!!')
        return server_response()

def json_data_validator():
    """[summary]
    Filtering jason data, to specify a boiler and feeder temps also bolier's status with all temperatures 
    Returns:
        [boiler_and_feeder_temps]: dict with boiler and feeder temp
        [boiler_ststus]: f-string with all bolier's sensors
    """
    WIDTH = 40
    json_data = server_response()

    boiler_status = ''

    boiler_and_feeder_temps = {}
    
    # YOU CAN USE ZIP FUNCTION !!!!
    for index, data in enumerate(json_data['thermos']):
        if data['t'] == 0.0:
            continue
        else:
            boiler_and_feeder_temps[SENSORS[index]] = data['t']
            boiler_status += SENSORS[index] + ':' + '    ' + str(data["t"]) + '\n'
        
    return boiler_status, boiler_and_feeder_temps

def check_temparatures():
    """[summary]
    Function is checking boilers temperatures 
    
    Returns:
        temp_boiler:int [returns boiler temperature]
        temp_feeder:int [returns feeder temperature]
        temperatures:int [returns CWU and RETURN temperatures]
    """
    boiler, feeder = SENSORS[0], SENSORS[2]
    temperatures, temp_range = json_data_validator()

    temp_boiler = str(temp_range[boiler])
    temp_feeder = str(temp_range[feeder])

    # print(temp_boiler, temp_feeder)
    
    # print(temperatures)

    return temp_boiler, temp_feeder, temperatures