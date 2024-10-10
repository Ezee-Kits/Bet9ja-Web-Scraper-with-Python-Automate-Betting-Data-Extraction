# Bet9ja Web Scraper with Python: Automate Betting Data Extraction

This Python script automates the extraction of soccer betting data from **Bet9ja**. It scrapes match times, team names, and betting odds (home, draw, away) from the Bet9ja website, providing a fast and efficient way to gather betting data for further analysis.

## 📌 Features

- **Automated Betting Data Scraping**: Extracts match times, teams, and odds from Bet9ja’s soccer section.
- **CSV Output**: Saves the data into a CSV file for easy access and analysis.
- **Efficient Scrolling**: Scrolls through the website to load and extract all match data.
- **Duplicate Removal**: Automatically detects and removes duplicate records to ensure clean datasets.

## 🚀 How It Works

The scraper visits the Bet9ja daily soccer betting page, extracts match details, and saves the data into a structured CSV format. It automatically scrolls through the available matches to capture all the required data.

### Key Steps:

1. **Browser Setup**: The script uses Selenium to initiate a browser session and navigate to the Bet9ja page.
2. **Scroll and Load**: Automatically scrolls through the page to load all the available soccer matches.
3. **Data Scraping**: Uses BeautifulSoup to extract match times, home/away teams, and betting odds.
4. **Data Storage**: Saves the extracted data in CSV format.
5. **Duplicate Handling**: Removes any duplicate records in the CSV file.

## 🛠️ Requirements

Before running the script, ensure the following packages are installed:

- **Python 3.x**
- **Selenium**
- **BeautifulSoup4**
- **pandas**
- **ChromeDriver** (or the appropriate driver for your browser)

Install the required packages using pip:
```bash
pip install selenium beautifulsoup4 pandas
```

## 🏃 How to Run the Script

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/Bet9ja-Web-Scraper.git
   ```

2. **Set up ChromeDriver**:  
   Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your browser. Ensure the ChromeDriver is in your system path.

3. **Run the Python Script**:
   ```bash
   python bet9ja_scraper.py
   ```

4. **View Results**:  
   The scraped data will be saved as `BET9JA.csv` in the specified directory.

## 📁 Output

The output CSV file (`BET9JA.csv`) contains the following fields:
- **TIME**: The match time.
- **HOME TEAM**: The home team in the match.
- **AWAY TEAM**: The away team in the match.
- **HOME ODD**: Odds for the home team to win.
- **DRAW ODD**: Odds for a draw.
- **AWAY ODD**: Odds for the away team to win.
- **BOOKMAKER**: The bookmaker name (Bet9ja).

## 🔧 Future Improvements

- **Expand to Other Sports**: Scrape data from other sports like basketball or tennis.
- **Error Handling**: Add more robust error handling for page load issues or website changes.
- **Enhance Efficiency**: Improve the script’s speed by optimizing scrolling and data extraction techniques.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing

Feel free to contribute by opening issues, suggesting improvements, or submitting pull requests. All feedback is welcome!
