import requests
import datetime as dt
import pandas as pd
from requests_ntlm import HttpNtlmAuth
from datetime import datetime

user = 'User-01'
password = 'passW00rd'
files_dictionary = {
    "excs": {
        'link': 'https://teams.organization.com/sharepoint/location a/excess report.xlsm',
        'savein': 'C:/path/to/save/file/',
        'newname': '',
        'dateformat': '%Y-%m-%d'
    }
}


def getfilename(link, date_format):
    today_date = dt.datetime.today().strftime(date_format)
    data = link.split("/")
    data = data[-1].split(".")
    data = data[0] + " " + today_date + "." + data[1]
    return data


def download_file(data_dic):
    df = pd.DataFrame(data=data_dic)
    session = requests.Session()
    session.auth = HttpNtlmAuth(user, password)
    r = session.get(df.excs.link)
    df.excs.newname = getfilename(df.excs.link, df.excs.dateformat)
    open(df.excs.savein + df.excs.newname, 'wb').write(r.content)


download_file(files_dictionary)

