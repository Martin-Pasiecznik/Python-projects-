## IMPORTANT: The code uses the library BeautifulSoup. Install with: pip install beautifulsoup4

from bs4 import BeautifulSoup

#HTML text between """ """ 
html_text = """
        ## Put your text in here!!!
"""

# Parse the html
soup = BeautifulSoup(html_text, 'html.parser')

# Extracts only the text, without the html
texto_sin_html = soup.get_text(separator=' ')

# print the result
print(texto_sin_html)
