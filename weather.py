import requests
import json
from os import getenv # 取得 API KEY 用
from dotenv import load_dotenv

load_dotenv()

locations = ["臺南市"]
dataid = "F-C0032-001"
apikey = getenv("CWA_API_KEY")
format = "JSON"
# URL_OLD = f"https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/{dataid}?Authorization={apikey}&format={format}&locationName={','.join(locations)}"
URL_NEW = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={apikey}&format={format}&locationName={','.join(locations)}"


def getWeatherData():
    request = requests.get(URL_NEW)
    print(URL_NEW)
    if request.status_code == 200:

        result_json = json.loads(request.text)
        # print(result_json)
        # json.loads() : 把文字 (json格式的文字) 轉換成字典
        # json.dumps() : 把字典轉換成文字 (json格式的文字)

        weather_list = []
        weather_element = result_json['records']['location'][0]['weatherElement']
        for index, element in enumerate(weather_element):
            for time_index, time in enumerate(element['time']):
                if index == 0:
                    data = {
                        'startTime':  time['startTime'],
                        'endTime': time['endTime'],
                        element['elementName']: time['parameter']['parameterName'],
                    }
                    weather_list.append(data)
                else:
                    try:
                        weather_list[time_index][element['elementName']
                                                 ] = f"{time['parameter']['parameterName']}{time['parameter']['parameterUnit']}"
                    except KeyError:
                        weather_list[time_index][element['elementName']
                                                 ] = f"{time['parameter']['parameterName']}"
        return weather_list
    return
