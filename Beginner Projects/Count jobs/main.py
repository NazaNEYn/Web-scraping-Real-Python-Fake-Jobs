import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_data(tag=None,class_name=None):
    #  css selector
    if class_name is not None:
        selector = f".{class_name}"
        elements = soup.select(selector)
        
    # tag selector
    elif tag is not None:
         elements = soup.find_all(tag)
         
    # if user dont provide anything
    else:
        return []
    
    return [element.get_text(strip=True) for element in elements]


response = requests.get("https://realpython.github.io/fake-jobs/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

job_title = fetch_data(tag="h2")
companies = fetch_data(class_name="company")
locations = fetch_data(class_name="location")

jobs = []
for title, company, location in zip(job_title,companies,locations):
    jobs.append({
        "Job Title": title,
        "Company": company,
        "Location": location,        
    })
    
df = pd.DataFrame(jobs)
df.to_json("jobs.json", orient="records", indent=4)



def filter_list(data_list,prompt):
    keyword = input(prompt).title()
    filtered = [item for item in data_list if keyword in item]
    return filtered


filtered_job = filter_list(job_title, "Search for a job keyword:\n")
print(filtered_job)
print("-----------------")
print(f"There are {len(filtered_job)} companies that match '{filtered_job}'.")

filtered_company = filter_list(companies, "Search for a company keyword:\n")
print(filtered_company)
print("-----------------")
print(f"There are {len(filtered_company)} companies that match '{filtered_company}'.")


filtered_location = filter_list(locations, "Search for a location keyword:\n")
print(filtered_location)
print("-----------------")
print(f"There are {len(filtered_location)} companies that match '{filtered_location}'.")



