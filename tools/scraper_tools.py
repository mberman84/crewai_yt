import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

class ScraperTool():
  @tool("Scraper Tool")
  def scrape(url: str):
    "Useful tool to scrap a website content, use to learn more about a given url."

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        article = soup.find(id='insertArticle')
        
        if article:
            # Extract and print the text from the article
            text = (article.get_text(separator=' ', strip=True))
        else:
            print("Article with specified ID not found.")
        
        return text
    else:
        print("Failed to retrieve the webpage")
    
