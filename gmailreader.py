import os.path
import csv
from datetime import datetime
import re
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Gmail API scope for read-only access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def clean_and_parse_date(date_raw: str):
    if not date_raw:
        return ''
    
    # Remove content in parentheses (e.g., (PDT), (UTC))
    cleaned = re.sub(r'\s*\(.*?\)\s*', '', date_raw).strip()

    try:
        return datetime.strptime(cleaned, "%a, %d %b %Y %H:%M:%S %z")
    except ValueError as e:
        print(f"Date parsing failed for: {cleaned}\nError: {e}")
        return None

def search_emails(service, query="subject:Thank you for Applying to Amazon"):
    results = service.users().messages().list(userId='me', q=query, maxResults=50).execute()
    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
        headers = msg_data['payload']['headers']
        
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '(No Sender)')
        date_raw = next((h['value'] for h in headers if h['name'] == 'Date'), '')
        
        # Clean and parse date
        date = clean_and_parse_date(date_raw)

        # Append email data, checking if the date is valid
        emails.append({
            'Date': date.strftime('%Y-%m-%d') if date else 'Invalid Date',
            'From': sender,
            'Subject': subject
        })

    return emails

def save_to_csv(emails, filename='job_applications.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'From', 'Subject'])
        writer.writeheader()
        writer.writerows(emails)
    print(f'Saved {len(emails)} emails to {filename}')

if __name__ == '__main__':
    service = authenticate_gmail()
    # Default query is 'job application', but you can change it
    emails = search_emails(service, query='job application')  
    save_to_csv(emails)
