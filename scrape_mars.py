# -*- coding: utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    mars_data = {}
    
    news_url = "https://mars.nasa.gov/news/"
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    weather_url = "https://twitter.com/marswxreport?lang=en"
    facts_url = "http://space-facts.com/mars/)"
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"    

    
    #Mars News
    news_response = requests.get(news_url)
    soup = bs(news_response.text, 'html.parser')
    news_title = soup.find('div', class_="content_title").text.strip()
    mars_data["news_title"] = news_title
    news_para = soup.find('div', class_='rollover_description_inner').text.strip()
    mars_data["news_para"] = news_para
     
    
    #Mars Featured Image from JPL website
    browser.visit(jpl_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    result = soup.find('ul', class_='articles')
    image = result.find_all('li')
    for i in image:
        url = i.find('a')['data-fancybox-href']
        featured_image_url = 'http://jpl.nasa.gov' + url
    mars_data["featured_image_url"] = featured_image_url 

    #Mars Weather
    weather_response = requests.get(weather_url)
    soup = bs(weather_response.text, 'html.parser')
    weather_tweet = soup.find('p', class_='tweet-text').text.strip()
    mars_data["weather"] = weather_tweet
     
    #Mars Facts
    tables = pd.read_html(facts_url)
    facts_df = tables[0]
    facts_df.columns = ['Parameters','Values']
    facts_df.set_index('Parameters', inplace=True) 
    facts_table = facts_df.to_html()
    facts_table = facts_table.replace('\n', ' ')
    mars_data["facts"] = facts_table
     

    #USGS Astrogeology Site
    browser.visit(usgs_url)
    time.sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find('div', class_='result-list')                   
    items = results.find_all('div', class_='item')                        
    titles_urls = []
    for item in items:                                              
        titles = item.find('div', class_='description')
        img_title = titles.a.text                                                
        img_title = img_title.replace(' Enhanced', '')
        browser.click_link_by_partial_text(img_title)                           
    
        time.sleep(2)
        html = browser.html                                                 
        soup = bs(html, 'html.parser')                                 
        linkss = soup.find('div', class_='downloads')
        links = linkss.find('ul')
        link = links.find('li')  
        img_url = link.a['href']
        titles_urls.append({'img_title': img_title, 'img_url': img_url})  
        browser.click_link_by_partial_text('Back')
        mars_data["high_res_images"] = titles_urls
         

    return mars_data