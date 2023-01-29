import requests
from bs4 import BeautifulSoup


 
def linkedin_scraper(webpage, page_number):
    results = []
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content,'html.parser')
    
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']
        results.append({'job_title': job_title, 'job_company': job_company, 'job_location': job_location, 'job_link': job_link})
    return results
    
    # if page_number < 25:
    #     page_number = page_number + 25
    #     linkedin_scraper(webpage, page_number)
    # else:
    #     print(results)

if __name__ == '__main__':
    print(linkedin_scraper('http://api.scraperapi.com?api_key=2b8b6e031d0f2382dff9abcd159cba20&url=https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={domain}&location={location}&geoId=115918471&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='.format(domain=r"App Development".replace(" ","%20"), location="Delhi".replace(" ","%20")), 0))