import requests
from bs4 import BeautifulSoup

def get_html_page_text(url):
    try:
        # Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find specific text elements (headings, paragraphs, spans)
        text_elements = []
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'span']):
            text_elements.append(tag.get_text(strip=True))

        # Join them into one big string
        all_text = ' '.join(text_elements)

        return all_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def scrape_stripe_treasury_marketing_policy(url):
    try:
        # Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from specific elements (headings, paragraphs)
        extracted_text = ""
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li']):
            extracted_text += tag.get_text(strip=True) + '\n'

        return extracted_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None