import requests
import json
import re

SENSORS = ['BOILER', 'BOILERS_RETURN', 'FEEDER', ' ', ' ', 'CWU', ' ', ' ', 'CO', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def server_response():
    """[summary]
    
    Function is monitoring Arduino's server with temparatures sensors.
    Returns:
        [json data type]: [boiler's tempartures in json data type]
    """
    try:

        data = requests.get('http://192.168.1.2/t.json')
        
        # used json.loads instade data.json()
        json_data = json.loads(data.text, encoding='utf-8')
    except ValueError:
        pass
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
    
    _ , temps = json_data_validator()

    #print(temp_boiler, temp_feeder)
    
    boilter_temp = temps[SENSORS[0]]
    boilter_return = temps[SENSORS[1]]
    feeder = temps[SENSORS[2]]
    cwu = temps[SENSORS[5]]
    co = temps[SENSORS[8]]

    return boilter_temp, boilter_return, feeder, cwu, co

def read_config(ip)-> str:
    try:
        response = requests.get('http://192.168.1.2/config.txt')
    
    except requests.exceptions.HTTPError as err_http:
        print('Http error', err_http)
    
    except requests.exceptions.ConnectionError as err_conect:
        print('Connecton error', err_conect)

    print(response.status_code)

    data = response.text
    
    return data

def find_value(data:str, record)-> tuple:
  
    pattern = f'(\W)+({record})+(\D)+[a-zA-Z0-9]+'
    
    result = re.findall(pattern, data)

    search_result = re.search(pattern, data)

    position_left, position_right = search_result.span()
    # print(position_left, position_right)
    
    data = data[:position_left] + f'\n{record}=13' + data[position_right:]
