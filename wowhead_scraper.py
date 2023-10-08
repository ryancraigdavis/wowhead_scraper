#!python3
# wowhead_scraper.py is a simple web scraper to check for the latest headlines
# on Wowhead.

import requests
import bs4

# URL of site we want to scrape


def quest_scrape():
    # url = "https://www.wowhead.com/wotlk"
    quest_data = []

    for quest_id in range(1, 10):
        quest_url = f"https://www.wowhead.com/wotlk/quest={quest_id}"
        raw_quest = requests.get(quest_url)  # Pull down the site.
        raw_quest.raise_for_status()  # Confirm site was pulled. Error if not
        soup = bs4.BeautifulSoup(raw_quest.text, "html.parser")

        for quest_main_content in soup.find_all(
            "div", class_="main-contents", id="main-contents"
        ):
            quest_content = quest_main_content.find("div", class_="text")
            print(quest_content)


if __name__ == "__main__":
    quest_scrape()
