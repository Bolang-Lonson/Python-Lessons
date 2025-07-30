import requests
from bs4 import BeautifulSoup

def fetch(url: str) -> BeautifulSoup:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(str(e))

    return BeautifulSoup(response.content, 'html.parser')


def extractTable(soup: BeautifulSoup) -> list:
    # Find the first (and only) table
    table = soup.find("table")

    # Extract table data
    data = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"])
        row_data = [cell.get_text(strip=True) for cell in cells]
        if row_data:
            data.append(row_data)

    return data[1:]

def displayGraphic(url: str) -> None:
    lines = extractTable(fetch(url))
    # Putting all y coords in their own list
    yCoords = [int(cell[2]) for cell in lines]

    # Getting height of display grid and knowing how many horizontal lines to print
    dispHeight = max(yCoords)

    for y in range(dispHeight, -1, -1):
        line = [pixel for pixel in lines if int(pixel[2]) == y] #   Getting all pixels that belong to line y
        orderedLine = sorted(line, key=lambda x: int(x[0])) #   Ordering the sublists for the line y in ascending order of x coords
        for i in range(len(orderedLine)):
            print(orderedLine[i][1], end='')

            if (i + 1) % 4 == 0:
                print(end=' ')

        print('\n')


displayGraphic('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')