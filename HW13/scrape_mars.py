from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars = {}

    # Retrieve Latest News Article
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    listTextLabelElem = news_soup.find('div', class_='listTextLabel')
    mars["news_title"] = listTextLabelElem.find('a').get_text()
    mars["news_paragraph"] = listTextLabelElem.find('p').get_text()

    # Retrieve JPL Mars Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    time.sleep(2)

    # Find the more info button and click that
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    time.sleep(2)

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    # find the relative image url
    img_url_rel = img_soup.find('figure', class_='lede').find('img')['src']

    # Set featured_image
    mars.featured_image = f'https://www.jpl.nasa.gov{img_url_rel}'

    # Retrieve Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    weather_soup = BeautifulSoup(html, 'html.parser')

    # First, find a tweet with the data-name `Mars Weather`
    mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})

    # Set weather
    mars.weather = mars_weather_tweet.find('p', 'tweet-text').get_text()

    # Retrieve Mars Hemisphere Data
    # USGS
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # go to url and find item by css; collect items into driver element list
    browser.visit(usgs_url)
    items = browser.find_by_css('a.product-item h3')
    # time.sleep(1)

    hemisphere_image_urls = []
    for i in range(len(items)):
        data = {}
        browser.find_by_css('a.product-item h3')[i].click()
        #    time.sleep(1)
        img_url = browser.find_link_by_text('Sample').first
        data['url'] = img_url['href']
        data['title'] = browser.find_by_css('h2.title').text
        hemisphere_image_urls.append(data)
        browser.back()

    # Set hemispheres
    mars.hemispheres = hemisphere_image_urls

    

    df = pd.read_html('http://space-facts.com/mars/')[0]
    df.columns = ['description', 'value']
    df.set_index('description', inplace=True)

    table = df.to_html()
    table = table.replace('\n', '')

    mars['facts'] = table

    browser.quit()

    return mars
