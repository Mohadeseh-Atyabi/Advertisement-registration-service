import requests


def send_simple_message(email, subject, description):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa3a4d0761a7f4658ae7f284b52f5e065.mailgun.org/messages",
        auth=("api", "a907e11b0fc8f520c37e03307dc30a2c-48c092ba-c915a7dd"),
        data={"from": "Mohadeseh Atyabi <atyabi2000@gmail.com>",
              "to": [email, email],
              "subject": subject,
              "text": description})

