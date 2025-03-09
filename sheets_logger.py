import gspread
from oauth2client.service_account import ServiceAccountCredentials

def log_to_sheets(user_name, time, message):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Attendance_Log").sheet1
    sheet.append_row([user_name, time, message])
