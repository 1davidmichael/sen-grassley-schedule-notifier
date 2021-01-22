import boto3
import os
import requests
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
from datetime import date


def lambda_handler(event, context):

    response = requests.get("https://www.grassley.senate.gov/news/events")
    soup = BeautifulSoup(response.text, "html.parser")
    schedule_text = soup.find_all("div", class_="field-item even")[0]

    events = schedule_text.find_all("p")

    client = boto3.client("ses")
    today = date.today()

    SENDER = os.environ["SENDER"]
    RECIPIENT = os.environ["RECIPIENT"]

    CHARSET = "UTF-8"
    SUBJECT = f"Grassley Schedule { today.strftime('%m/%d/%Y') }"
    BODY_TEXT = "\n".join(str(event.text) for event in events)

    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [RECIPIENT],
            },
            Message={
                "Body": {
                    "Text": {
                        "Charset": CHARSET,
                        "Data": BODY_TEXT
                    }
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": SUBJECT
                }
            },
            Source=SENDER
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
