# sitemap_extractor.py
import requests
from bs4 import BeautifulSoup

companies_sitemap_url = {
    'https://www.ejobs.ro/sitemaps-new/companies.xml',
    'https://www.ejobs.ro/sitemaps-new/companies-latest.xml'
}

def get_urls_from_sitemap():
    urls = []
    for url in companies_sitemap_url:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Skip if the root is sitemapindex
        if soup.find("sitemapindex"):
            continue

        # Get all URL entries, typically wrapped in <url> tags in sitemaps
        for entry in soup.find_all("url"):
            loc_tag = entry.find("loc")  # <loc> tag typically contains the actual URL
            if loc_tag:
                urls.append(loc_tag.text)
    
    return urls

