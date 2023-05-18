import requests
from bs4 import BeautifulSoup

# Function to scrape the webpage
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the desired information from the webpage
    # Modify this part according to the specific data you want to scrape
    
    # Example: Extract all the links on the webpage
    links = soup.find_all('a')
    links_data = [link['href'] for link in links]
    
    # Example: Extract all the headings on the webpage
    headings = soup.find_all(['h1', 'h2', 'h3'])
    headings_data = [heading.text.strip() for heading in headings]
    
    # Save the scraped data to a text file
    with open(f"{url.split('//')[1]}.txt", "w") as file:
        file.write("Links:\n")
        file.write("\n".join(links_data))
        file.write("\n\nHeadings:\n")
        file.write("\n".join(headings_data))

# Get the website URL from the user
website_url = input("Enter the website URL: ")

# Scrape the webpage
scrape_website(website_url)
