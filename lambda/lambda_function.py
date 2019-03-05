import json

from google.oauth2 import service_account
from googleapiclient import discovery

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './credentials.json'

SPREADSHEET_ID = "1xuScrH253ULpsq-RKLGCqbDQagieUNMQsjtGJ1uQbVw"


def lambda_handler(event, context):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = discovery.build('sheets', 'v4', credentials=credentials)
    range_ = "RSVP!A:B"
    value_input_option = 'USER_ENTERED'
    value_range_body = {
        "values": [
            json.loads(event["body"]),
        ]
    }
    request = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_,
        valueInputOption=value_input_option,
        body=value_range_body,
    )
    return {
        "statusCode": 201,
        "body": json.dumps(request.execute()),
    }


if __name__ == '__main__':
    lambda_handler()
