#Removes request warnings from console
import json
import jsonpath
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def test_get_fnd_uc_data():
    N_day_from_tmr = 1
    host = "https://pda.weather.gov.hk/locspc/data/fnd_uc.xml"

    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Accept-Language": "zh-tw",
        "User-Agent": "locspc 6.2.4, UIDeviceType: iPhone 5s, systemVersion: 12.4.6",
        "Host": "pda.weather.gov.hk"
        }
    try:
        print("start try sending request")
        response = requests.get(url=host, headers=headers, verify=False, allow_redirects=True, timeout=30)
        # print(response.text)
        json_res = response.json()

        # Adding assertions here
        print("Assertion starts from here:")
        assert response.status_code == 200
        # assert response['general_situation'] is not None

        # To get humidity data of specific days---> Q:1 days from tomorrow(the day after tomorrow)
        get_n_day_humidity_data(json_res, N_day_from_tmr)


    except requests.exceptions.HTTPError as err_h:
        print("Http Error: ", err_h)
    except requests.exceptions.ConnectionError as err_c:
        print("Error Connecting: ", err_c)
    except requests.exceptions.TooManyRedirects as err_tmr:
        print("Too Many Timeout: ", err_tmr)
    except requests.exceptions.Timeout as err_t:
        print("Timeout Error: ", err_t)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else --- ", err)
        raise SystemExit(err)




def get_n_day_humidity_data(json_response, param_n_days_from_tmr):
    if param_n_days_from_tmr is None:
        print("Error: value of N_Days is Null to continue")
    else:
        print("Get Humidity data of "+ str(param_n_days_from_tmr) + " days-from-Tomorrow : (zero-day = Tomorrow)")

        # json index start from "0", first day of weather (tomorrow) will be index "0",
        max_rh = jsonpath.jsonpath(json_response,"$.[forecast_detail]["+str(param_n_days_from_tmr)+"][max_rh]")
        min_rh = jsonpath.jsonpath(json_response,"$.[forecast_detail]["+str(param_n_days_from_tmr)+"][min_rh]")
        print("Expecting Humidity(%) is between : " + str(min_rh) + " - " + str(max_rh) )


if __name__ == '__main__':
    test_get_fnd_uc_data()
