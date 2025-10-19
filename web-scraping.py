import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup
import csv

# Function to send email alerts
def send_email(subject, body, to_email, from_email, app_password):
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, app_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    

# URL to scrape
url = "http://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# Extract book data
products = soup.find_all("article", class_="product_pod")
data = []

for product in products:
    title = product.h3.a["title"]
    price_text = product.find("p", class_="price_color").text.strip()
    price = float(price_text.replace("£", ""))  
    availability = product.find("p", class_="instock availability").text.strip()
    data.append([title, price, availability])

# Set price alert threshold
PRICE_LIMIT = 20.0
alerts = []

for title, price, availability in data:
    if price < PRICE_LIMIT:
        alert_msg = f"'{title}' is now £{price} ({availability})"
        alerts.append(alert_msg)

# *** UPDATE THESE BEFORE RUNNING ***
FROM_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password_here"
TO_EMAIL = "recipient_email@gmail.com"

# Send alerts if any
if alerts:
    body = "\n".join(alerts)
    send_email("Price Alert 🚨", body, TO_EMAIL, FROM_EMAIL, APP_PASSWORD)
    print("Email sent with alerts!")
else:
    print("No deals found today.")

# Save scraped data to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability"])
    writer.writerows(data)