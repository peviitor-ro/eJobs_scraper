import json
from sitemap_extractor import get_urls_from_sitemap
from job_checker import check_for_jobs_and_extract_company

def process_jobs():
    urls = get_urls_from_sitemap()
    
    company_jobs_dict = {}  # Dictionary to store company details and jobs for each company

    for url in urls:
        jobs_for_url = check_for_jobs_and_extract_company(url)

        # If no jobs are found, skip to the next URL
        if not jobs_for_url:
            continue

        # Assuming the company name and logo is consistently the same across all its job listings
        company_name = jobs_for_url[0]["company"]
        company_logo = jobs_for_url[0]["job_logo"]

        # Create or update the company entry
        if company_name not in company_jobs_dict:
            company_jobs_dict[company_name] = {
                "logo": company_logo,
                "jobs": []
            }
        
        # Accumulate jobs for each company
        for job in jobs_for_url:
            # Remove the redundant company and logo fields from the job
            del job["company"]
            del job["job_logo"]

            company_jobs_dict[company_name]["jobs"].append(job)

    return company_jobs_dict

