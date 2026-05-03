import csv
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL

CSV_FILE = 'database.csv'


def check_csv_has_data(filepath):
    if not Path(filepath).exists():
        return False, 0

    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            data_rows = len(rows) - 1 if len(rows) > 1 else 0
            return data_rows > 0, data_rows
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False, 0


def send_email_alert(row_count):
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = f'Alert: database.csv contains {row_count} record(s)'
    msg.set_content(f"""\
Alert: your database.csv file contains data.

Records found: {row_count}
File: {CSV_FILE}

Please review the contents at your earliest convenience.

This is an automated message from your PythonAnywhere scheduled task.
""")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print(f"Alert email sent to {RECIPIENT_EMAIL}")


def main():
    print(f"Checking {CSV_FILE}...")
    has_data, row_count = check_csv_has_data(CSV_FILE)

    if has_data:
        print(f"Data found: {row_count} row(s). Sending alert...")
        send_email_alert(row_count)
    else:
        print("No data found or file doesn't exist. No alert sent.")


if __name__ == "__main__":
    main()
