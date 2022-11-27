from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                         '=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobsList = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for jobs in jobsList:
    published_date = jobs.find('span', class_='sim_posted').span.text
    if 'few' in published_date :
        print(f"The published date: {published_date} :")
        companyName = jobs.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = jobs.find('span', class_='srp-skills').text.replace(" ", "")
        print(f"company name:{companyName}. Required skills: {skills}")
    print(jobs)
