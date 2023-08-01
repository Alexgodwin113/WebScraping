import time

from bs4 import BeautifulSoup
import requests

print("Which location you are familiar to work from?")
location = input('>')
print(f'filtering out {location}')


def find_jobs():
    html_text = requests.get('https://appointments.thetimes.co.uk/jobs/?Keywords=python#browsing').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_="lister__details cf js-clickable")
    for index, job in enumerate(jobs):
        job_location = job.find('li', class_="lister__meta-item lister__meta-item--location").text
        if location in job_location:
            company = job.find('li', class_="lister__meta-item lister__meta-item--recruiter").text
            salary = job.find('li', class_="lister__meta-item lister__meta-item--salary").text
            job_name = job.find('h3', class_="lister__header").text
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Job Name : {job_name.strip()} \n")
                f.write(f"Company Name: {company.strip()} \n")
                f.write(f"Salary : {salary.strip()} \n")
                f.write(" ")

            print(f'File Saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
