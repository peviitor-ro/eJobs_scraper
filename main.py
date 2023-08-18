from sitemap_extractor import get_urls_from_sitemap
from json_writer import write_to_json
from job_extractor import extract_all_jobs
from job_publisher import publish_all_jobs_in_directory

def main():
    urls = get_urls_from_sitemap()
    company_jobs_dict = extract_all_jobs(urls)
    write_to_json(company_jobs_dict)
    publish_all_jobs_in_directory('FirmeNoi')

if __name__ == "__main__":
    main()
