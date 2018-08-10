import requests
import datetime as dt
from requests_ntlm import HttpNtlmAuth

user = 'User-01'
password = 'passW00rd'


def getfilename(link, date_format):
    today_date = dt.datetime.today().strftime(date_format)
    data = link.split("/")
    data = data[-1].split(".")
    data = data[0] + " " + today_date + "." + data[1]
    return data


def download_file(record):
    session = requests.Session()
    session.auth = HttpNtlmAuth(user, password)
    r = session.get(record.get('link'))
    record['newname'] = getfilename(record['link'], record['dateformat'])
    with open(record['savein'] + record['newname'], 'wb') as f:
        f.write(r.content)


files_dictionary = [
    {
        'key': 'excs',
        'link': 'https://teams.organization.com/sharepoint/location a/excess report.xlsm',
        'savein': 'C:/path/to/save/file/',
        'newname': '',
        'dateformat': '%Y-%m-%d'
    },
    {
        'key': 'excs2',
        'link': 'https://teams.organization.com/sharepoint/location a/excess report2.xlsm',
        'savein': 'C:/path/to/save/file2/',
        'newname': '',
        'dateformat': '%Y-%m-%d'
    },
]

download_file(files_dictionary[0])
