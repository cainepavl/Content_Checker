# CSV Database Alert Script

A Python script that monitors a CSV file and sends email alerts when data is detected. Designed to run as a scheduled task on PythonAnywhere.

## Features

- Checks if `database.csv` contains any data rows
- Sends email alerts when data is found
- Counts and reports the number of records
- Easy to configure and schedule

## Requirements

- Python 3.6 or higher
- Access to an email account with SMTP support
- PythonAnywhere account (or any server that can run scheduled Python scripts)

## Installation

1. Download the script to your PythonAnywhere account or local machine
2. Ensure `database.csv` is in the same directory as the script
3. Install Python (usually pre-installed on PythonAnywhere)

No additional Python packages are required - the script uses only standard library modules.

## Configuration

Before running the script, you need to configure the email settings. Open the script and modify these variables:

```python
CSV_FILE = 'database.csv'              # Path to your CSV file
SENDER_EMAIL = 'your_email@gmail.com'  # Your email address
SENDER_PASSWORD = 'your_app_password'  # Your email app password
RECIPIENT_EMAIL = 'recipient@example.com'  # Where to send alerts
SMTP_SERVER = 'smtp.gmail.com'         # SMTP server
SMTP_PORT = 587                        # SMTP port
```

### Gmail Setup

If using Gmail, you'll need an App Password:

1. Enable 2-Factor Authentication on your Google Account
2. Go to Google Account → Security → App passwords
3. Generate a new app password for "Mail"
4. Use this 16-character password in the `SENDER_PASSWORD` field

**Important**: Never use your regular Gmail password in scripts!

### Other Email Providers

For other email providers, update the SMTP settings:

- **Outlook/Hotmail**: `smtp.office365.com`, port 587
- **Yahoo**: `smtp.mail.yahoo.com`, port 587
- **Custom domain**: Check your provider's SMTP settings

## Usage

### Running Manually

```bash
python csv_alert_script.py
```

The script will:
1. Check if `database.csv` exists
2. Count the data rows (excluding header row)
3. Send an email if data is found
4. Print status messages to the console

### Setting Up on PythonAnywhere

1. Upload the script to your PythonAnywhere account
2. Upload or create your `database.csv` file in the same directory
3. Go to the **Tasks** tab in your PythonAnywhere dashboard
4. Click **Create a new scheduled task**
5. Enter the command: `python3 /home/yourusername/path/to/csv_alert_script.py`
6. Choose your schedule (e.g., daily at 9:00 AM)
7. Click **Create**

### Scheduling Options

You can schedule the task to run:
- **Hourly**: For frequent monitoring
- **Daily**: At a specific time each day
- **Custom**: Using cron syntax for more control

## How It Works

1. **File Check**: The script looks for `database.csv` in the specified location
2. **Data Detection**: It reads the CSV and counts rows (excluding the header)
3. **Alert Trigger**: If any data rows exist, an email alert is sent
4. **Email Content**: The email includes the number of records found
5. **Logging**: Status messages are printed (visible in PythonAnywhere logs)

## Email Alert Format

When data is detected, you'll receive an email with:

- **Subject**: "Alert: Database.csv Contains X Record(s)"
- **Body**: Number of records found and file location
- **Timestamp**: Automatically included by your email client

## Troubleshooting

### No Email Received

- Check your email credentials are correct
- Verify your email provider allows SMTP access
- Check the PythonAnywhere error log for details
- Ensure your firewall isn't blocking SMTP connections

### Authentication Errors

- For Gmail, make sure you're using an App Password, not your regular password
- Verify 2-Factor Authentication is enabled (required for Gmail App Passwords)
- Check that "Less secure app access" is not required (use App Passwords instead)

### CSV File Not Found

- Verify the file path is correct
- Use absolute paths if the script runs from a different directory
- Check file permissions (script needs read access)

### Script Not Running on Schedule

- Check the PythonAnywhere task log for errors
- Verify the path to your script is correct
- Ensure you're using `python3` (not just `python`)

## File Structure

```
your_directory/
├── csv_alert_script.py    # The main script
└── database.csv           # Your CSV file to monitor
```

## Customization

You can easily customize the script:

- **Change CSV filename**: Modify the `CSV_FILE` variable
- **Customize email content**: Edit the `body` text in the `send_email_alert()` function
- **Add attachments**: Extend the script to attach the CSV file to the email
- **Multiple recipients**: Change `RECIPIENT_EMAIL` to a comma-separated list

## Security Notes

- Never commit files containing passwords to version control
- Use environment variables for sensitive information in production
- Keep your app passwords secure and don't share them
- Regularly rotate your app passwords

## License

This script is provided as-is for personal and commercial use.

## Support

For issues related to:
- **PythonAnywhere**: Check their help documentation
- **Email setup**: Consult your email provider's SMTP documentation
- **Script modifications**: Review the inline comments in the code
