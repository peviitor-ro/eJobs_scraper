from sitemap_extractor import get_urls_from_sitemap
from json_writer import write_to_json
from job_extractor import extract_all_jobs
from job_publisher import publish_all_jobs_in_directory
from clear_folder import delete_contents_of_folder

def main():
    directory_path = "FirmeNoi"

    urls = get_urls_from_sitemap()

    print("Extracting jobs...")
    company_jobs_dict = extract_all_jobs(urls)

    for company in company_jobs_dict.keys():
        write_to_json(company_jobs_dict)
        publish_all_jobs_in_directory(directory_path)

    # Delete the contents of the 'FirmeNoi' directory after extracting and publishing jobs
    delete_contents_of_folder(directory_path)

if __name__ == "__main__":
    main()
