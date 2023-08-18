from job_checker import check_for_jobs_and_extract_company

def extract_all_jobs(urls):
    company_jobs = {}
    for url in urls:
        jobs_for_url = check_for_jobs_and_extract_company(url)
        if not jobs_for_url:
            continue
        company_name = jobs_for_url[0]["company"]
        if company_name in company_jobs:
            company_jobs[company_name]['Jobs'].extend(jobs_for_url)
        else:
            company_jobs[company_name] = {
                'Company': company_name,
                'Logo': jobs_for_url[0]['job_logo'],
                'Jobs': jobs_for_url
            }
    return company_jobs

