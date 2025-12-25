import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import os

# Configuration
CSV_FILE = 'database.csv'
SENDER_EMAIL = 'your_email@gmail.com'  # Replace with your email
SENDER_PASSWORD = 'your_app_password'  # Replace with your app password
RECIPIENT_EMAIL = 'recipient@example.com'  # Replace with recipient email
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def check_csv_has_data(filepath):
    """Check if CSV file exists and has data rows (beyond header)."""
    if not Path(filepath).exists():
        return False, 0
    
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            # Check if there are rows beyond the header
            data_rows = len(rows) - 1 if len(rows) > 1 else 0
            has_data = data_rows > 0
            
            return has_data, data_rows
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False, 0

def send_email_alert(row_count):
    """Send an email alert about CSV contents."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f'Alert: Database.csv Contains {row_count} Record(s)'
        
        # Email body
        body = f"""
        Alert: Your database.csv file contains data!
        
        Number of records found: {row_count}
        File: {CSV_FILE}
        
        Please review the contents at your earliest convenience.
        
        This is an automated message from your PythonAnywhere scheduled task.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        print(f"Alert email sent successfully to {RECIPIENT_EMAIL}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def main():
    """Main function to check CSV and send alert if needed."""
    print(f"Checking {CSV_FILE}...")
    
    has_data, row_count = check_csv_has_data(CSV_FILE)
    
    if has_data:
        print(f"Data found: {row_count} row(s). Sending alert...")
        send_email_alert(row_count)
    else:
        print("No data found in CSV or file doesn't exist. No alert sent.")

if __name__ == "__main__":
    main()
