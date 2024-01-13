# Scraping 'a' tags from a list of links in csv file
from selenium import webdriver
import csv

# Replace 'your_file.csv' with the path to your CSV file containing links
file_path = 'your_file.csv'

# Create a WebDriver instance (make sure you have the appropriate webdriver installed and its path set)
driver = webdriver.Chrome()

# Open the CSV file
with open(file_path, 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Get the link from the current row
        link = row[0]

        # Navigate to the link
        driver.get(link)

        # Retrieve all anchor tags on the page
        anchor_tags = driver.find_elements_by_tag_name('a')

        # Print or process the anchor tags as needed
        for anchor_tag in anchor_tags:
            print(anchor_tag.get_attribute('href'))

# Close the WebDriver
driver.quit()

# TODO navigate to a lower level in a link
