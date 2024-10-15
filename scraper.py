import requests
from bs4 import BeautifulSoup

# Fetch webpage content
url = 'https://www.geo.tv/'  # Replace with the target URL
response = requests.get(url)
content = response.text

# Parse HTML content
soup = BeautifulSoup(content, 'html.parser')
headlines = soup.find_all('h1')  # Modify as needed

# Create or overwrite the HTML file to display the data
with open('index.html', 'w') as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraped Data</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Scraped Data</h1>
    <ul>
    ''')
    
    # Write the scraped headlines into the HTML file
    for headline in headlines:
        f.write(f'<li>{headline.text.strip()}</li>\n')
    
    f.write('''
    </ul>
</body>
</html>
''')

print("Data written to index.html")
