

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
```


```python
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
```


```python
news_url = "https://mars.nasa.gov/news/"
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
weather_url = "https://twitter.com/marswxreport?lang=en"
facts_url = "http://space-facts.com/mars/)"
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
```


```python
#Mars News
```


```python
news_response = requests.get(news_url)
```


```python
soup = bs(news_response.text, 'html.parser')
#print(soup.prettify())
```


```python
news_title = soup.find('div', class_="content_title").text.strip()
print(news_title)
```

    NASA Invests in Visionary Technology
    


```python
news_para = soup.find('div', class_='rollover_description_inner').text.strip()
print(news_para)
```

    NASA is investing in technology concepts, including several from JPL, that may one day be used for future space exploration missions.
    


```python
#Mars Featured Image from JPL website using Splinter
```


```python
browser.visit(jpl_url)
browser.find_by_id('full_image').click()
featured_image_url = browser.find_by_css('.fancybox-image').first['src']
print(featured_image_url)
```

    https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA15254_ip.jpg
    


```python
#Mars Featured Image from JPL website using Beautiful Soup
```


```python
browser.visit(jpl_url)
html = browser.html
soup = bs(html, 'html.parser')
result = soup.find('ul', class_='articles')
image = result.find_all('li')
for i in image:
    url = i.find('a')['data-fancybox-href']
featured_image_url = 'http://jpl.nasa.gov' + url
print(featured_image_url)
```

    http://jpl.nasa.gov/spaceimages/images/largesize/PIA22362_hires.jpg
    


```python
#Mars Weather
```


```python
weather_response = requests.get(weather_url)
soup = bs(weather_response.text, 'html.parser')
```


```python
weather_tweet = soup.find('p', class_='tweet-text').text.strip()
print(weather_tweet)
```

    Sol 2042 (May 05, 2018), Sunny, high -7C/19F, low -72C/-97F, pressure at 7.30 hPa, daylight 05:23-17:20
    


```python
#Mars Facts
```


```python
tables = pd.read_html(facts_url)
tables
```




    [                      0                              1
     0  Equatorial Diameter:                       6,792 km
     1       Polar Diameter:                       6,752 km
     2                 Mass:  6.42 x 10^23 kg (10.7% Earth)
     3                Moons:            2 (Phobos & Deimos)
     4       Orbit Distance:       227,943,824 km (1.52 AU)
     5         Orbit Period:           687 days (1.9 years)
     6  Surface Temperature:                  -153 to 20 °C
     7         First Record:              2nd millennium BC
     8          Recorded By:           Egyptian astronomers]




```python
facts_df = tables[0]
facts_df.columns = ['Parameters','Values']
facts_df.set_index('Parameters', inplace=True)
facts_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Values</th>
    </tr>
    <tr>
      <th>Parameters</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Equatorial Diameter:</th>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>Polar Diameter:</th>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>Mass:</th>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>Moons:</th>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>Orbit Distance:</th>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>Orbit Period:</th>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>Surface Temperature:</th>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>First Record:</th>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>Recorded By:</th>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
facts_table = facts_df.to_html()
facts_table = facts_table.replace('\n', ' ')
print(facts_table)
```

    <table border="1" class="dataframe">   <thead>     <tr style="text-align: right;">       <th></th>       <th>Values</th>     </tr>     <tr>       <th>Parameters</th>       <th></th>     </tr>   </thead>   <tbody>     <tr>       <th>Equatorial Diameter:</th>       <td>6,792 km</td>     </tr>     <tr>       <th>Polar Diameter:</th>       <td>6,752 km</td>     </tr>     <tr>       <th>Mass:</th>       <td>6.42 x 10^23 kg (10.7% Earth)</td>     </tr>     <tr>       <th>Moons:</th>       <td>2 (Phobos &amp; Deimos)</td>     </tr>     <tr>       <th>Orbit Distance:</th>       <td>227,943,824 km (1.52 AU)</td>     </tr>     <tr>       <th>Orbit Period:</th>       <td>687 days (1.9 years)</td>     </tr>     <tr>       <th>Surface Temperature:</th>       <td>-153 to 20 °C</td>     </tr>     <tr>       <th>First Record:</th>       <td>2nd millennium BC</td>     </tr>     <tr>       <th>Recorded By:</th>       <td>Egyptian astronomers</td>     </tr>   </tbody> </table>
    


```python
#USGS Astrogeology Site
```


```python
browser.visit(usgs_url)
html = browser.html
soup = bs(html, 'html.parser')
print(soup.prettify())
```

    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
     <head>
      <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" rel="stylesheet" type="text/css"/>
      <script async="" src="https://ssl.google-analytics.com/ga.js" type="text/javascript">
      </script>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js" type="text/javascript">
      </script>
      <title>
       Astropedia Search Results | USGS Astrogeology Science Center
      </title>
      <meta content="USGS Astrogeology Science Center Astropedia search results." name="description"/>
      <meta content="USGS,Astrogeology Science Center,Cartography,Geology,Space,Geological Survey,Mapping" name="keywords"/>
      <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
      <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
      <meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport"/>
      <meta content="x61hXXVj7wtfBSNOPnTftajMsZ5yB2W-qRoyr7GtOKM" name="google-site-verification"/>
      <!--<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Open+Sans:400italic,400,bold"/>-->
      <link href="/css/main.css" media="screen" rel="stylesheet"/>
      <link href="/css/print.css" media="print" rel="stylesheet"/>
      <!--[if lt IE 9]>
    			<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    			<script src="/js/respond.min.js"></script>
    			<link rel="stylesheet" type="text/css" href="/css/ie.css"/>
                            <script>
                              document.createElement('header');
                              document.createElement('nav');
                              document.createElement('section');
                              document.createElement('article');
                              document.createElement('aside');
                              document.createElement('footer');
                              document.createElement('hgroup');
                            </script>
                      <![endif]-->
      <link href="/favicon.ico" rel="icon" type="image/x-ico"/>
     </head>
     <body id="results">
      <header>
       <h1>
        Astrogeology Science Center
       </h1>
       <a href="http://www.usgs.gov">
        <img alt="USGS: Science for a Changing World" class="logo" height="70" src="/images/usgs_logo_main_2x.png" width="180"/>
       </a>
      </header>
      <div class="wrapper">
       <nav>
        <a href="#" id="nav-toggle" title="Navigation Menu">
         Menu
        </a>
        <ul class="dropdown dropdown-horizontal" id="yw0">
         <li>
          <a href="/">
           Home
          </a>
         </li>
         <li>
          <a href="/about">
           About
          </a>
          <ul>
           <li>
            <a href="/about/careers">
             Careers
            </a>
           </li>
           <li>
            <a href="/contact">
             Contact
            </a>
           </li>
           <li>
            <a href="/about/events">
             Events
            </a>
           </li>
           <li>
            <a href="/site/glossary">
             Glossary
            </a>
           </li>
           <li>
            <a href="/about/mission">
             Mission
            </a>
           </li>
           <li>
            <a href="/news">
             News
            </a>
           </li>
           <li>
            <a href="/people">
             People
            </a>
           </li>
           <li>
            <a href="/about/using-our-images">
             Using Our Images
            </a>
           </li>
           <li>
            <a href="/about/visitors">
             Visitors
            </a>
           </li>
          </ul>
         </li>
         <li>
          <a href="/facilities">
           Labs / Facilities
          </a>
          <ul>
           <li>
            <a href="/facilities/flynn-creek-crater-sample-collection">
             Flynn Creek Crater Sample Collection
            </a>
           </li>
           <li>
            <a href="http://www.moon-cal.org">
             Lunar Calibration Project
            </a>
           </li>
           <li>
            <a href="/facilities/meteor-crater-sample-collection">
             Meteor Crater Sample Collection
            </a>
           </li>
           <li>
            <a href="/facilities/mrctr">
             MRCTR GIS Lab
            </a>
           </li>
           <li>
            <a href="/facilities/cartography-and-imaging-sciences-node-of-nasa-planetary-data-system">
             PDS Cartography and Imaging Sciences Node
            </a>
           </li>
           <li>
            <a href="/pds/annex">
             PDS IMG Annex
            </a>
           </li>
           <li>
            <a href="/facilities/photogrammetry-guest-facility">
             Photogrammetry Guest Facility
            </a>
           </li>
           <li>
            <a href="/rpif">
             Regional Planetary Information Facility (RPIF)
            </a>
           </li>
          </ul>
         </li>
         <li>
          <a href="/maps">
           Maps / Products
          </a>
          <ul>
           <li>
            <a href="/search">
             Product Search
            </a>
           </li>
           <li>
            <a href="http://planetarynames.wr.usgs.gov">
             Gazetteer of Planetary Nomenclature
            </a>
           </li>
           <li>
            <a href="http://planetarymapping.wr.usgs.gov">
             Geologic Mapping Program
            </a>
           </li>
           <li>
            <a href="http://pilot.wr.usgs.gov">
             Planetary Image Locator Tool (PILOT)
            </a>
           </li>
           <li>
            <a href="/search/planetary-index">
             Planetary Map Index
            </a>
           </li>
          </ul>
         </li>
         <li>
          <a href="/geology">
           Missions / Research
          </a>
          <ul>
           <li>
            <a href="/geology/mars-dunes">
             Mars Dunes
            </a>
           </li>
           <li>
            <a href="/geology/mars-ice">
             Mars Ice
            </a>
           </li>
           <li>
            <a href="/missions">
             Mission Support
            </a>
           </li>
           <li>
            <a href="/solar-system">
             Solar System
            </a>
           </li>
           <li>
            <a href="/groups">
             Working Groups
            </a>
           </li>
          </ul>
         </li>
         <li>
          <a href="/tools">
           Tools
          </a>
          <ul>
           <li>
            <a href="http://planetarynames.wr.usgs.gov">
             Gazetteer of Planetary Nomenclature
            </a>
           </li>
           <li>
            <a href="http://isis.astrogeology.usgs.gov">
             Integrated Software for Imagers and Spectrometers (ISIS)
            </a>
           </li>
           <li>
            <a href="http://astrogeology.usgs.gov/tools/map-a-planet-2">
             Map a Planet 2
            </a>
           </li>
           <li>
            <a href="http://pilot.wr.usgs.gov">
             Planetary Image Locator Tool (PILOT)
            </a>
           </li>
           <li>
            <a href="http://astrocloud.wr.usgs.gov/">
             Projection on the Web (POW)
            </a>
           </li>
          </ul>
         </li>
        </ul>
        <form action="/search/results" class="search" id="search" method="get">
         <input title="Search Astropedia" type="submit" value=""/>
         <input name="q" placeholder="Search" type="text"/>
         <input name="__ncforminfo" type="hidden" value="IkwEzEPZK6Eoy1HChkI6m9FuSC1ggBXyZoWQ6--o3hcoA4vsFMMQMOA0Zz0-OUOOJxGMChzxA9amyYHVCFWbMYEK8mTjTT6jMJvoSLOKIjk="/>
        </form>
       </nav>
       <div class="container">
        <form action="/search/results" class="bar widget block" id="search-bar">
         <input name="q" type="hidden" value="hemisphere-enhanced"/>
         <input name="target" type="hidden" value="Mars"/>
         <input name="__ncforminfo" type="hidden" value="IkwEzEPZK6Eoy1HChkI6m9FuSC1ggBXyZoWQ6--o3hdp5r0MV2Kw9w_uFM95BArapDnoC17ZDRSG5Av03ahb8PpuNb36mjojoXX5Go3QBfSpwE_pJMhZ6g=="/>
        </form>
        <div class="full-content">
         <section class="block" id="results-accordian">
          <div class="result-list" data-section="product" id="product-section">
           <div class="accordian">
            <h2>
             Products
            </h2>
            <span class="count">
             4 Results
            </span>
            <span class="collapse">
             Collapse
            </span>
           </div>
           <div class="collapsible results">
            <div class="item">
             <a class="itemLink product-item" href="/search/map/Mars/Viking/cerberus_enhanced">
              <img alt="Cerberus Hemisphere Enhanced thumbnail" class="thumb" src="/cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png"/>
             </a>
             <div class="description">
              <a class="itemLink product-item" href="/search/map/Mars/Viking/cerberus_enhanced">
               <h3>
                Cerberus Hemisphere Enhanced
               </h3>
              </a>
              <span class="subtitle" style="float:left">
               image/tiff 21 MB
              </span>
              <span class="pubDate" style="float:right">
              </span>
              <br/>
              <p>
               Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…
              </p>
             </div>
             <!-- end description -->
            </div>
            <div class="item">
             <a class="itemLink product-item" href="/search/map/Mars/Viking/schiaparelli_enhanced">
              <img alt="Schiaparelli Hemisphere Enhanced thumbnail" class="thumb" src="/cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png"/>
             </a>
             <div class="description">
              <a class="itemLink product-item" href="/search/map/Mars/Viking/schiaparelli_enhanced">
               <h3>
                Schiaparelli Hemisphere Enhanced
               </h3>
              </a>
              <span class="subtitle" style="float:left">
               image/tiff 35 MB
              </span>
              <span class="pubDate" style="float:right">
              </span>
              <br/>
              <p>
               Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…
              </p>
             </div>
             <!-- end description -->
            </div>
            <div class="item">
             <a class="itemLink product-item" href="/search/map/Mars/Viking/syrtis_major_enhanced">
              <img alt="Syrtis Major Hemisphere Enhanced thumbnail" class="thumb" src="/cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png"/>
             </a>
             <div class="description">
              <a class="itemLink product-item" href="/search/map/Mars/Viking/syrtis_major_enhanced">
               <h3>
                Syrtis Major Hemisphere Enhanced
               </h3>
              </a>
              <span class="subtitle" style="float:left">
               image/tiff 25 MB
              </span>
              <span class="pubDate" style="float:right">
              </span>
              <br/>
              <p>
               Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…
              </p>
             </div>
             <!-- end description -->
            </div>
            <div class="item">
             <a class="itemLink product-item" href="/search/map/Mars/Viking/valles_marineris_enhanced">
              <img alt="Valles Marineris Hemisphere Enhanced thumbnail" class="thumb" src="/cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png"/>
             </a>
             <div class="description">
              <a class="itemLink product-item" href="/search/map/Mars/Viking/valles_marineris_enhanced">
               <h3>
                Valles Marineris Hemisphere Enhanced
               </h3>
              </a>
              <span class="subtitle" style="float:left">
               image/tiff 27 MB
              </span>
              <span class="pubDate" style="float:right">
              </span>
              <br/>
              <p>
               Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…
              </p>
             </div>
             <!-- end description -->
            </div>
            <script>
             addBases=[];;if(typeof resetLayerSwitcher==="function"){resetLayerSwitcher(false)};var productTotal = 4;
            </script>
           </div>
           <!-- end this-section -->
          </div>
         </section>
        </div>
       </div>
       <div class="icons projects black scroll-wrapper">
        <div class="scroll">
         <a class="icon" href="http://isis.astrogeology.usgs.gov" title="Integrated Software for Imagers and Spectrometers">
          <img alt="ISIS Logo" height="112" src="/images/logos/isis_2x.jpg" width="112"/>
          <span class="label">
           ISIS
          </span>
         </a>
         <a class="icon" href="http://planetarynames.wr.usgs.gov" title="Gazetteer of Planetary Nomenclature">
          <img alt="Nomenclature Logo" height="112" src="/images/logos/nomenclature_2x.jpg" width="112"/>
          <span class="label">
           Planetary Nomenclature
          </span>
         </a>
         <a class="icon" href="http://astrogeology.usgs.gov/tools/map" title="Map a Planet 2">
          <img alt="Map-a-Planet Logo" height="112" src="/images/logos/map_a_planet_2x.jpg" width="112"/>
          <span class="label">
           Map a Planet 2
          </span>
         </a>
         <a class="icon" href="/facilities/imaging-node-of-nasa-planetary-data-system-pds" title="PDS Imaging Node">
          <img alt="PDS Logo" height="112" src="/images/pds_logo-black-web.png"/>
          <span class="label">
           PDS Imaging Node
          </span>
         </a>
         <!--
    						<a title="Astropedia Search" href="/search" class="icon">
    							<img alt="Astropedia Logo" height="112" width="112" src="/images/logos/astropedia_2x.jpg"/>
    							<span class="label">Astropedia</span>
    						</a>
    -->
         <a class="icon" href="/rpif" title="Regional Planetary Image Facility">
          <img alt="RPIF Logo" height="112" src="/images/logos/rpif_2x.jpg" width="112"/>
          <span class="label">
           RPIF
          </span>
         </a>
         <a class="icon" href="/facilities/photogrammetry-guest-facility" title="Photogrammetry Guest Facility">
          <img alt="Photogrammetry Guest Faciltiy Logo" height="112" src="/images/logos/photogrammetry_2x.jpg" width="112"/>
          <span class="label">
           Photogrammetry Guest Facility
          </span>
         </a>
         <a class="icon" href="http://pilot.wr.usgs.gov" title="Planetary Image Locator Tool">
          <img alt="Pilot Logo" height="112" src="/images/logos/pilot_2x.jpg" width="112"/>
          <span class="label">
           PILOT
          </span>
         </a>
         <a class="icon" href="/facilities/mrctr" title="Mapping, Remote-sensing, Cartography, Technology and Research GIS Lab">
          <img alt="MRCTR GIS Lab Logo" height="112" src="/images/logos/mrctr_2x.jpg" width="112"/>
          <span class="label">
           MRCTR GIS Lab
          </span>
         </a>
        </div>
       </div>
       <footer>
        <div class="left">
         <a href="http://astrogeology.usgs.gov">
          Home
         </a>
         |
         <a href="http://astrogeology.usgs.gov/contact">
          Contact
         </a>
         |
         <a href="http://astrogeology.usgs.gov/about/events">
          Events
         </a>
         |
         <a href="http://astrogeology.usgs.gov/news">
          News
         </a>
        </div>
        <div class="right">
         <a href="http://www.doi.gov">
          U.S. Department of Interior
         </a>
         |
         <a href="http://www.usgs.gov">
          U.S. Geological Survey
         </a>
         |
         <a href="http://www.usa.gov">
          USA.gov
         </a>
        </div>
       </footer>
      </div>
      <!--
    		<div class="credit">
    			<small>Background Credits: NASA/USGS</small>
    		</div>
    -->
      <div class="page-background" style="
    			background:url('/images/backgrounds/mars.jpg');
    			filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(
    				src='/images/backgrounds/mars.jpg', sizingMethod='scale');
    		">
      </div>
      <script type="text/javascript">
       var baseUrl = "";
    
    
    var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-27613186-1']);_gaq.push(['_trackPageview']);(function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);})();
      </script>
      <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js" type="text/javascript">
      </script>
      <script src="/js/general.js" type="text/javascript">
      </script>
     </body>
    </html>
    


```python
results = soup.find('div', class_='result-list')                   
items = results.find_all('div', class_='item')                        
titles_urls = []

for item in items:                                              
    titles = item.find('div', class_='description')
    img_title = titles.a.text                                                
    img_title = img_title.replace(' Enhanced', '')
    browser.click_link_by_partial_text(img_title)                           
    
    html = browser.html                                                 
    soup = bs(html, 'html.parser')                                 
    
    linkss = soup.find('div', class_='downloads')
    links = linkss.find('ul')
    link = links.find('li')  
    img_url = link.a['href']
    
    titles_urls.append({'img_title': img_title, 'img_url': img_url})  
    
    browser.click_link_by_partial_text('Back')  
```


```python
print(titles_urls)
```

    [{'img_title': 'Cerberus Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'img_title': 'Schiaparelli Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'img_title': 'Syrtis Major Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'img_title': 'Valles Marineris Hemisphere', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]
    
