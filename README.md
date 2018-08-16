# Mission_to_Mars

This web application scrapes various websites for data related to the Mission to Mars and displays the information in an HTML page.  

Data is scraped and collected from the websites below:

* [NASA Mars News Site](https://mars.nasa.gov/news/)
* [Featured Mars Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
* [Mars Weather Twitter Account](https://twitter.com/marswxreport?lang=en)
* [Mars Facts](http://space-facts.com/mars/)
* [High Resolutionm Images for each of Mars' hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

Application is built with:

* Requests/Splinter to navigate the sites  
* BeautifulSoup to find and parse out the necessary data
* MongoDB with Flask templating to create the HTML page
* PyMongo for CRUD applications for the database
* HTML/CSS and Bootstrap to structure the HTML template
