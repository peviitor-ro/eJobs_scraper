import os
import json

def write_to_json(company_jobs_data):
    directory = 'FirmeNoi'
    if not os.path.exists(directory):
        os.makedirs(directory)

    for company, company_data in company_jobs_data.items():
        safe_name = company.replace("'", "")
        filename = os.path.join(directory, f"{safe_name}.json")

        existing_jobs = []
        # Check if company's JSON file already exists
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as existing_file:
                existing_data = json.load(existing_file)
                existing_jobs = existing_data.get('Jobs', [])
        
        new_jobs = company_data["Jobs"]
        
        # Only append new jobs with IDs not found in the existing file
        filtered_new_jobs = [job for job in new_jobs if not any(ej.get("id") == job.get("id") for ej in existing_jobs)]
        
        # Combine the existing jobs with the filtered new jobs
        all_jobs = existing_jobs + filtered_new_jobs

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({
                "Company": company,
                "Logo": company_data.get('Logo', 'Default Logo URL'),
                "Jobs": all_jobs
            }, file, ensure_ascii=False, indent=4)
        
        print(f"Created or updated JSON file for {company}")

    return f"Processed {len(company_jobs_data)} companies. JSON files have been updated in the '{directory}' folder."

