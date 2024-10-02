import requests
from bs4 import BeautifulSoup


def fetch_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_google_doc(doc_text):
    soup = BeautifulSoup(doc_text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    characters = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) == 3:
            x = cells[0].get_text(strip=True)
            char = cells[1].get_text(strip=True)
            y = cells[2].get_text(strip=True)
            characters.append((int(x), int(y), char))

    return characters


def create_grid(characters):
    if not characters:
        return []

    max_x = max(x for x, y, char in characters)
    max_y = max(y for x, y, char in characters)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in characters:
        grid[y][x] = char

    return grid


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def display_secret_message(url):
    doc_text = fetch_google_doc(url)
    characters = parse_google_doc(doc_text)
    grid = create_grid(characters)
    print_grid(grid)



# Example usage
url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
display_secret_message(url)