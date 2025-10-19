📚 Book Price Alert Web Scraper

A Python web scraper that monitors book prices from Books to Scrape
 and sends email alerts when a book’s price falls below a specified threshold.

🧠 Features

Scrapes book titles, prices, and availability using BeautifulSoup

Sends automatic email alerts when prices drop below a threshold

Saves all scraped data into a CSV file for analysis

Simple and readable Python code, with placeholders for email credentials

⚙️ Technologies Used

Python 3

Requests

BeautifulSoup4

smtplib (for email automation)

CSV module

🚀 How to Run

Clone this repository:

git clone https://github.com/s338moha/python-webscraping-assignment.git
cd python-webscraping-assignment


Install required packages:

pip install requests beautifulsoup4


Open book_price_scraper.py and update email credentials:

FROM_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password_here"
TO_EMAIL = "recipient_email@gmail.com"


⚠️ Use an App Password from Gmail, not your regular password.
Learn how: https://myaccount.google.com/apppasswords

Run the scraper:

python book_price_scraper.py


Check your inbox for alerts and view the generated CSV file:

books.csv

📊 Example CSV Output
Title,Price,Availability
A Light in the Attic,51.77,In stock
Tipping the Velvet,53.74,In stock
Soumission,50.10,In stock

📨 Example Email Alert
Subject: Price Alert 🚨

'It's Only the Himalayas' is now £19.99 (In stock)
'The Requiem Red' is now £17.45 (In stock)

🧾 Notes

Educational project for learning web scraping and email automation.

Only scrapes publicly available data from BooksToScrape.

Do not include your real email password in the repository. Use your own Gmail App Password.
