import os
import json
from firme_noi_processor import extract_and_publish_jobs

def publish_all_jobs_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                company_data = json.load(file)
            company_name = company_data['Company']
            extract_and_publish_jobs(company_name, company_data)
