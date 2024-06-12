import win32com.client
import os
from datetime import datetime, timedelta

# Function to sanitize filenames
def sanitize_filename(filename):
    return "".join(c for c in filename if c.isalnum() or c in (' ', '_')).rstrip()

# Select the outlook email you want to backup
# Access the outlook from the device
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

# List available accounts/mailboxes
arr_mailbox = []
for account in mapi.Accounts:
    print(account.DisplayName)
    arr_mailbox.append(account)

# User input to select the mailbox
email_select = input("Please paste the email you would like to backup: ")

# Access the inbox folder
inbox = mapi.Folders(email_select).Folders("Inbox")
email_list = inbox.Items

# Make sure the backup directory exists
backup_dir = ''
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Iterate over email items and save them
for i, message in enumerate(email_list, start=1):
    subject_sanitized = sanitize_filename(message.Subject)
    filename = f'{i}_{subject_sanitized}.msg'
    full_path = os.path.join(backup_dir, filename)
    message.SaveAs(full_path, 3)
    print(f"Message {i} was saved successfully as {filename}")

print("All messages were saved successfully.")
