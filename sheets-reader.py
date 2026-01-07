import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import time

# -------------------------------
# Google Sheets setup
# -------------------------------
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google-sheets.json", scope)
client = gspread.authorize(creds)

# Open your sheet (replace with your sheet name)
sheet = client.open("AI_Leads").sheet1

# Track which rows we already sent
sent_rows = set()

# -------------------------------
# Loop to send new leads continuously
# -------------------------------
while True:
    rows = sheet.get_all_records()
    
    for i, row in enumerate(rows):
        if i in sent_rows:
            continue  # skip already sent rows

        lead_data = {
            "name": str(row["name"]),
            "phone": str(row["phone"]),
            "service": str(row["service"]),
            "location": str(row["location"])
        }

        try:
            response = requests.post("http://127.0.0.1:8000/lead", json=lead_data)
            print(response.json())
            sent_rows.add(i)  # mark row as sent
        except Exception as e:
            print("Failed to send lead:", e)

    # Wait 10 seconds before checking again
    time.sleep(10)
