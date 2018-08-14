import requests
import datetime as dt
from requests_ntlm import HttpNtlmAuth

user = 'User-01'
password = 'passW00rd'
today_date = dt.datetime.today().strftime('%m%d%y')
free_day_format = dt.datetime.today().strftime('%Y-%m-%d')


def getDateLines():
    today = dt.datetime.today()
    if today.weekday() == 0 | today.weekday() == 1:
        date = today - dt.timedelta(days=4)
        return date.strftime('%Y - %m-%d')
    else:
        date = today - dt.timedelta(days=2)
        return date.strftime('%Y - %m-%d')


def download_files(dictionary):
    session = requests.Session()
    session.auth = HttpNtlmAuth(user, password)
    for record in dictionary:
        if dt.datetime.today().weekday() in record['recurrency']:
            r = session.get(record.get('link'))
            with open(record['savein'] + record['newname'], 'wb') as f:
                f.write(r.content)


files_dictionary = [
    {
        'key': 'excs',
        'recurrency': [1, 3],
        'link': 'https://teams.organization.com/sharepoint/location a/excess report.xlsm',
        'savein': 'C:/path/to/save/file/',
        'newname': 'excess report' + today_date + '.xlsm'
    },
    {
        'key': 'excs2',
        'recurrency': [0, 1, 2, 3, 4],
        'link': 'https://teams.organization.com/sharepoint/location a/excess report2 ' + getDateLines() + '.xlsm',
        'savein': 'C:/path/to/save/file2/',
        'newname': 'excess report2 ' + getDateLines() + '.xlsm'
    },
    {
        'key': 'excs3',
        'recurrency': [4],
        'link': 'https://teams.organization.com/sharepoint/location a/excess report3 ' + free_day_format + '.xlsb',
        'savein': 'C:/path/to/save/file3/',
        'newname': 'excess report3 ' + free_day_format + '.xlsb'
    }
]

download_files(files_dictionary)
