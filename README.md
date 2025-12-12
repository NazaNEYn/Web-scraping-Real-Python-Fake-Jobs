# Web Scraping Projects

## [BEGINNER PROJECT](https://github.com/NazaNEYn/Web-scraping-Real-Python-Fake-Jobs/tree/main/Beginner%20Projects)

1.  **[Job Scraper (basic)](https://github.com/NazaNEYn/Web-scraping-Real-Python-Fake-Jobs/tree/main/Beginner%20Projects/01%20-%20Job%20Scraper)**
    * **Scrape:** job title, company, location, job description (on detail page).
    * **Export to:** CSV, JSON.
    * **This teaches:**
        * ✔ `.find_all()`
        * ✔ CSS selectors

2.  **[Search by keyword (CLI)](https://github.com/NazaNEYn/Web-scraping-Real-Python-Fake-Jobs/tree/main/Beginner%20Projects/02%20-%20Job%20Scraper%20(Search%20by%20keyword))**
    * The script displays all jobs with "python" in the title.
    * **You learn:**
        * ✔ filtering
        * ✔ user input
        * ✔ basic CLI tools
    * **Output example:**
        ```
        ['Lauraton, AP']
        ```

3.  **[Count jobs](https://github.com/NazaNEYn/Web-scraping-Real-Python-Fake-Jobs/blob/main/Beginner%20Projects/Count%20jobs/main.py)**
    * **Generate:**
        ```
        Company A — 12 jobs
        Company B — 5 jobs
        Company C — 3 jobs
        ```
    * **Teaches:**
        * ✔ dictionaries
        * ✔ data grouping

---

## INTERMEDIATE PROJECTS

4.  **Jobs by Location Map**
    * Scrape all job locations → generate a frequency map.
    * **Example:**
        ```
        Remote: 35
        San Francisco: 3
        Berlin: 2
        Madrid: 1
        ```
    * **Optional:**
        * export as a bar chart (matplotlib)
        * save results to CSV

5.  **Build a Job Search CLI Tool**
    * Commands like:
        ```bash
        python jobfinder.py --location "Remote"
        python jobfinder.py --company "Acme"
        python jobfinder.py --keyword "software"
        ```
    * **Teaches:**
        * ✔ `argparse`
        * ✔ structured command-line tools
        * ✔ filtering data

6.  **Save full job descriptions**
    * Each job has a detail page.
    * Your script can follow the link and extract:
        * title
        * company
        * location
        * description
        * date posted
    * Store everything in a JSON file.
    * **This teaches:**
        * ✔ scraping multiple pages
        * ✔ link extraction
        * ✔ nested scraping (page → detail page)

---

## ADVANCED PROJECTS

7.  **Build a mini Job Recommendation Engine**
    * **Steps:**
        * Scrape all jobs
        * Vectorize job descriptions (TF-IDF)
        * User enters skills like "python, flask, sql"
        * Script returns best matching jobs
    * **Teaches:**
        * ✔ simple NLP
        * ✔ TF-IDF
        * ✔ cosine similarity

8.  **Build a Job Board Web App**
    * Using Flask or Django:
        * homepage shows all jobs
        * filter by company, location, keyword
        * job detail page shows full description
    * **You learn:**
        * ✔ backend routing
        * ✔ HTML templates
        * ✔ rendering scraped data into a UI

9.  **Build a SQLite Database**
    * **Tables:**
        * jobs
        * companies
        * locations
    * **Fields:**
        * title
        * company
        * location
        * description
        * apply link
    * Populate the database from the scraper.
    * **Teaches:**
        * ✔ SQL
        * ✔ databases
        * ✔ schema design

---

## PORTFOLIO-WORTHY PROJECTS

10. **Automated Job Analytics Dashboard**
    * Make a dashboard (Streamlit):
        * job count by company
        * job count by location
        * word cloud of job requirements
        * filter sidebar
    * Users can explore data in real time.

11. **Build a “Daily Fresh Jobs” Notifier**
    * Your script:
        * Scrapes the site daily
        * Detects new postings
        * Emails new jobs (using SMTP)
    * **Teaches:**
        * ✔ scheduling
        * ✔ notifications
        * ✔ tracking changes across runs

12. **Build a Resume Matcher**
    * User uploads resume text.
    * Script recommends jobs that best match skills.
    * **Teaches:**
        * ✔ NLP
        * ✔ similarity scoring
        * ✔ data parsing
