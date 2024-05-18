from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#pip install <name-of-library>==<version>
#pip install requests
#pip install beautifulsoup4
#pip install selenium
#pip install lxml
#pip install selenium
#pip install Scrapy
#pip install -U selenium==4.11.2 #help to find appropriate selenium


#https://scrapinghub.github.io/xpath-playground/

#html Markup Syntax
#<h1 class='title'> Titanic(1997) </h1>
#Tag name Attribute: Attribute name/ Attribute value End tag

#TAGS
    #<head>
    #<body>
    #<header>
    #<article>
    #<p>: paragraph
    #<h1>, <h2>, <h3>: heading
    #<div>: divider
    #<nav>: navigational
    #<li>: list item
    #<a>: anchor
        #<a href = "...."> Text </a>
    #<button>
    #<table>
    #<td>: table data
    #<tr>: table row element
    #<ul>: unordered list
    #<iframe>

#XPath
    //tagName[contains(@AttributeName,"Value")]
    //tagName[
    /: select the children from the node set on the left side of this character
    //: specifies that matching node set should be located at any level within the document
     
    //tr/td --> get td inside tr
    
#Explicit Waits
        WebDriverWait(driver, 10).until(EC.presence_of)element_located(By.XPath,'value'))
   
#Order to find elements:
    #1. ID
    #2. Class name
    #3. Tag name, CSS Selector
    #4. Xpath
    
#Beautiful Soup
    #Steps before scraping a website
        #1.Fetch the pages
        #2.Page content
        #3.Create soup
            #soup.find(id = "specific_id")
            #soup.find('tag',class_ = "class_name")
            #soup.find_all("")
            
            #pagination : pages
    #Identify Java script : Go to setting, disable Java to see impact

#Selenium
    #website = ''
    #path = ''
    #driver = webdriver.Chrome(path)
    Headless Mode: running in background
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.headless = True
        options.add_argument('window-size=1920x1080')
        #driver.maximize_window() #maximize window
        #driver = webdriver.Chrome(path,options=options)
    
       
    driver.find_element_by_id()
    driver.find_elements_by_id() #multiple elements
    driver.find_element_by_class_name()
    driver.find_element_by_tag_name()
    driver.find_element_by_xpath('//tag[@AttrributeName="Value"]')
    driver.find_element_by_css_selector()
    driver.find_element_by_name()
    driver.find_element_by_link_text()
    find_element(By.ID, "id")
    find_element(By.NAME, "name")
    find_element(By.XPATH, "xpath")
    find_element(By.LINK_TEXT, "link text")
    find_element(By.PARTIAL_LINK_TEXT, "partial link text")
    find_element(By.TAG_NAME, "tag name")
    find_element(By.CLASS_NAME, "class name")
    find_element(By.CSS_SELECTOR, "css selector")
    
    all_matches_button = driver.find_element('xpath','//label[@analytics-event = "All matches"]')
    all_matches_button.click()

    Dropdowns
        dropdown = Select(driver.find_element_by_id('country'))
        dropdown.select_by_visible_text('Spain')
    Pagination
        paging = 
    
    
    Logins
    Waits
    
#SCRAPY
    conda install conda-forge scrapy==1.6 pylint autopep8 -y

#Selenium Webdriver
    #Console in Inspect
        $x('xPath')
    actual_url = driver.current_url
    assert actual_url== "" #verify matching or not
    logout_button_locator = driver.find_element(By.LINK_TEXT,'Log out')
    assert logout_button_locator.is_displayed()
    
    
    
    
    
    
    























 
            










        



 




