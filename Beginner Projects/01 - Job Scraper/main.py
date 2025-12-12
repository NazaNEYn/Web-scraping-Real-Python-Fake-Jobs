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
    

saving_file_input = input("Do you want to save the results as 'json' or 'csv' format?\nType 'j' for json and 'c' for csv?\n").lower()

df = pd.DataFrame(jobs)

while True:
    if saving_file_input == "j":
        df.to_json("jobs.json", orient="records",indent=4)
        print("Jobs saved as jobs.json")
        break
    elif saving_file_input == "c":
        df.to_csv("jobs.csv", index=False)
        print("Jobs saved as jobs.csv")
        break
    else:
        print("Invalid input. Try again!")

    
