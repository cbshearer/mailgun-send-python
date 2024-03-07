import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## your configured mailgun domain
mg_domain = "mg.example.com"
## username is always API (https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)
mg_user = "api"
## API key (menu > API Security > Mailgun API Keys)
mg_pass = "EXAMPLE-KEY-DATA"
## address the message will be FROM
mg_from = "sender@example.com"
## address the message will be TO
mg_to = "recipient@example.com"

send_msg =  requests.post(
f"https://api.mailgun.net/v3/{mg_domain}/messages",
auth=(f"{mg_user}", f"{mg_pass}"),
data={"from": f"{mg_from}",
    "to": f"{mg_to}",
    "subject": "Hello there sir",
    "text": "Testing 1-2-3-4"},
    verify=False)

print(send_msg.status_code)
print(send_msg.text)
