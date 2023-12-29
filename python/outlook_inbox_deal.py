import win32com.client
def get_outlook_rule_email_count(folder_name):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6).Folders[str(folder_name)]  # 6 represents the Inbox folder
    items = inbox.items
    email_count=items.Count
    print(folder_name,email_count)
    return email_count
