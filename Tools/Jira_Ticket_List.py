import requests
from bs4 import BeautifulSoup

# Define the URL of the JIRA kanban board you want to scrape
url = "https://travismathew.atlassian.net/jira/software/c/projects/CHS/boards/90"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'html.parser')

aria_labels = [element['aria-label'] for element in soup.find_all(attrs={'aria-label': True})]
print(aria_labels)

