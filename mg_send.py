import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mg_domain = "mg.example.com"        ## your configured mailgun domain
mg_user = "api"                     ## username is always API (https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)
mg_pass = "EXAMPLE-KEY-DATA"        ## API key (menu > API Security > Mailgun API Keys)

mg_sender = "sender@example.com"
mg_recipient = "recipient@example.com"
mg_subject = "test subject"
mg_message = "this is a test body!"

send_url = f"https://api.mailgun.net/v3/{mg_domain}/messages"
send_data = {"from": mg_sender, "to": mg_recipient, "subject": mg_subject, "text": mg_message}
send_msg =  requests.post(send_url, auth=(mg_user, mg_pass), data={"from": mg_sender, "to": mg_recipient, "subject": mg_subject, "text": mg_message}, verify=False)

print(send_msg.status_code)
print(send_msg.text)
