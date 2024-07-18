
# Python MongoDB Weather Scraper

This project is a Python application that scrapes weather data from the [Government of Canada's weather page](https://www.weather.gc.ca/canada_e.html) and loads the data into a MongoDB database. 
The project uses the `requests` library to fetch the web page, `BeautifulSoup` for parsing the HTML, and `PyMongo` for interacting with MongoDB.

 **Script Overview**:
   - The script fetches the weather data from the specified URL.
   - It parses the HTML to extract the weather data table.
   - The extracted data is then loaded into the MongoDB database.
   - Each document in the MongoDB collection includes a `last_modified` field containing the UTC timestamp of when the data was inserted.

![image](https://github.com/user-attachments/assets/c8aea3fb-0cf3-4fad-b0c1-84a022bb44f6)
