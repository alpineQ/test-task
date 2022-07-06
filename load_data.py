""" Модуль выгрзуки данных из Google Spreadsheets """
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def load_data(spreadsheet_id: str, spreadsheet_range: str):
    """
    Загрузка данных из документа с spreadsheet_id в диапазоне spreadsheet_range
    """
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(
        "./credentials.json",
        ['https://www.googleapis.com/auth/spreadsheets']
    ).authorize(httplib2.Http())
    service_account = build('sheets', 'v4', http=creds_service)

    resp = service_account.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=spreadsheet_range
    ).execute()
    return resp


if '__main__' == __name__:
    data = load_data("1o9Uk_nmSLMRIX3oifxkfyALSVbFFzn4JQ0C9UhG40NU", "Sheet1!A1:C51")
    print(data)
