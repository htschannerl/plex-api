import logging
import warnings
import datetime
import os
import requests


def getItemLibrary(libId):
    logging.info("Getting the items of library ID " + libId)
    api_url = "http://plex.tschannerl.com:32400/library/sections/" + libId + "/all"
    my_headers = {'X-Plex-Token': apikey, 'Accept': 'application/json'}

    response = requests.get(api_url,headers=my_headers,verify=False)
    json_response = response.json()
    if response.status_code == 200:
        return json_response
    else:
        logging.info(json_response)
        return "Error"


if __name__ == '__main__':
    apikey = input("Inform the API KEY: ")
    warnings.filterwarnings('ignore')
    moment = datetime.datetime.now().strftime('%Y-%m-%m-%H%M%S')
    logdir = "./logs/"
    if not os.path.isdir(logdir):
        os.mkdir(logdir)
    logname = logdir + moment + ".log"

    logging.basicConfig(filename=logname,
                        filemode='a',
                        format='%(asctime)s,%(msecs)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

    items = getItemLibrary('25')
    for item in items['MediaContainer']['Metadata']:
        totalMedia = len(item['Media'])
        #for media in item['Media']:
            #print(len(media['Part']))

