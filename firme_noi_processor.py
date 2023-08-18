import os
import json
from bs4 import BeautifulSoup
from utils import *

def extract_and_publish_jobs(company, company_data, api_key='Grasum_Key'):
    # Extract jobs from company data
    final_jobs = company_data['Jobs']

    # Publish jobs and logo
    for version in [1, 4]:
        publish(version, company, final_jobs, api_key)

    publish_logo(company, company_data['Logo'])

if __name__ == "__main__":
    directory = 'FirmeNoi'
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                company_data = json.load(file)

            company_name = company_data['Company']
            extract_and_publish_jobs(company_name, company_data)
