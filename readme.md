# eJobs Scraper

The `eJobs Scraper` is a web scraping tool designed to extract job listings from the eJobs.ro platform. It processes these listings and publishes them to a specified endpoint. The tool also ensures that outdated job listings for specific companies are deleted before new ones are added.

## Features

- Extract job listings from eJobs.ro.
- Process job data, such as company name, job title, and logo.
- Extract sitemaps to aid in web scraping.
- Write extracted data to JSON format.
- Automatically clean outdated data for specific companies before updating.
- Publish the processed data to an API.

## Getting Started

### Prerequisites

- Python 3.x

### Setup

1. Clone the repository:

git clone [repository-link]
cd [repository-directory]

### Usage

Run the main script to start the scraping process:

python main.py

This will extract the jobs, process the data, and publish it to the specified API.

### Structure

main.py: The primary entry point of the application.

job_checker.py: Contains functions to check for jobs and extract company details from URLs.

job_extractor.py: Processes URLs and extracts job information.

job_publisher.py: Publishes processed job data.

sitemap_extractor.py: Extracts sitemaps to streamline the web scraping process.

json_writer.py: Writes extracted data into a JSON format.

job_processor.py: Processes and refines the job data after extraction.

firme_noi_processor.py: Handles specific processing for 'firme noi' or new companies.
