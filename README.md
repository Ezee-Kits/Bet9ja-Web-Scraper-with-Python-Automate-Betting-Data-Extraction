Bet9ja Web Scraper with Python: Automate Betting Data Extraction

Welcome to the Bet9ja Web Scraper, a Python-based script designed to automate the process of extracting betting data from the Bet9ja website. This tool is perfect for sports betting enthusiasts, data analysts, and developers looking to gather real-time betting odds for soccer matches.

📋 Project Overview

This project leverages Selenium and BeautifulSoup to scrape soccer betting odds and match details from the Bet9ja website. The data includes match times, teams, and the associated odds (home, draw, away) for each game, which is then saved into a structured CSV file.

🚀 Features

Scrapes real-time soccer betting data from Bet9ja's daily bundle page.
Captures essential match information: match time, teams, and betting odds.
Saves data in CSV format for easy access and further analysis.
Handles page scrolling to load more data automatically.
Prevents duplicate entries by checking for and removing any repeated records.

🛠️ Installation and Setup

Prerequisites
Python 3.x
Selenium
BeautifulSoup
WebDriver for Selenium (e.g., ChromeDriver or GeckoDriver)

Installation Steps

Clone the Repository:

    git clone https://github.com/YourUsername/Bet9ja-Web-Scraper.git

Install the Required Libraries:

    pip install -r requirements.txt

Download the Appropriate WebDriver:

If you're using Chrome, download ChromeDriver and place it in your system PATH.
Modify the Saving Path (Optional):

In the script, update the saving_path_csv variable with your preferred directory to save the CSV file.

🕹️ Usage
Run the Script:
  python bet9ja_scraper.py

📁 Output

The output CSV file (BET9JA.csv) contains the following fields:

TIME: The match time.
HOME TEAM: The home team in the match.
AWAY TEAM: The away team in the match.
HOME ODD: Odds for the home team to win.
DRAW ODD: Odds for a draw.
AWAY ODD: Odds for the away team to win.
BOOKMAKER: The bookmaker name (Bet9ja).

🔧 Future Improvements

Additional Markets: Expand the scraper to extract data from other betting markets (e.g., over/under, handicap).
Error Handling: Improve robustness in case of website changes or scraping failures.
Multiple Bookmakers: Add support for scraping odds from other betting websites.

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Feel free to contribute by opening issues, suggesting improvements, or submitting pull requests. Your feedback is appreciated!
  
The script will automatically open a browser, navigate to Bet9ja's soccer betting page, scrape the data, and save it as BET9JA.csv in your specified directory.
