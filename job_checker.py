# job_checker.py
import requests
import re
from bs4 import BeautifulSoup
from utils import create_job, publish, publish_logo  # Assuming you have these functions in the utils module

def check_for_jobs_and_extract_company(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    job_elements = soup.find('main', class_='CDInner__Main').find_all('div', class_='JobCard')
    
    # If no jobs are found, return None immediately
    if not job_elements:
        return None

    # Extract company title once
    company_name_tag = soup.find('h1', class_='CDTCompanyAlias')
    if company_name_tag:
        company_title = company_name_tag.text.replace('S.R.L.', '').replace('SRL', '').replace(' ', '').replace('&', '').replace('-', '').strip()
        company_title = re.sub(r'[^a-zA-Z0-9 ]', '', company_title)
        company_title = re.sub(r'\s+', ' ', company_title).strip()
    else:
        company_title = "Unknown"

    jobs = []

    for job in job_elements:
        job_title_tag = job.find('h2')
        
        if job_title_tag:
            job_title = job_title_tag.text.strip()
            # Remove any non-ASCII characters from the job_title
            job_title = re.sub(r'[^\x00-\x7F]+', '', job_title)
            # Extracting job link from the <a> tag
            job_link_tag = job_title_tag.find('a', href=True)
            job_link = "https://www.ejobs.ro" + job_link_tag['href'] if job_link_tag else url
        else:
            job_title = "Unknown"
            job_link = url

        # Extracting job logo
        default_logo = "https://design.ejobs.ro/assets/img/colorPositiveOrange.07ea350f.png"
        job_logo_container = job.find('div', class_='JDCDetails__Logo')
        if job_logo_container:
            job_logo = job_logo_container.find('img', alt=True)
            if job_logo and job_logo.has_attr('src'):
                job_logo_url = job_logo['src'] if not job_logo['src'].startswith("data:image") else default_logo
            else:
                job_logo_url = default_logo
        else:
            job_logo_url = default_logo

        # Extracting city
        job_city_tag = job.find('span', class_='JCContentMiddle__Info')
        if job_city_tag:
            job_city = job_city_tag.text.replace('\u0219', 's').replace('\u0103', 'a')
            job_city = job_city.split('si alte')[0].split(',')[0].strip()
            job_city = job_city.replace('(', '').replace(')', '').strip()
        else:
            job_city = "Unknown"

        job_data = create_job(
            company=company_title,
            job_title=job_title,
            job_link=job_link,
            job_logo=job_logo_url,
            city=job_city,
            country='Romania'
        )
        jobs.append(job_data)

    # Publish the jobs and logo
    for version in [1]:
        publish(version, company_title, jobs, 'Grasum_Key')

    # Assuming you're using the logo of the first job as the company logo
    if jobs and 'job_logo' in jobs[0] and jobs[0]['job_logo'] != "No logo found":
        publish_logo(company_title, jobs[0]['job_logo'])

    return jobs
