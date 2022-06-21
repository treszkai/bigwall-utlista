import csv
import sys

from requests_html import HTMLSession

grade_dict = {
    # French grade: UIAA grade
    '4a': 'IV',
    '4b': 'V−',
    '4c': 'V',
    '5a': 'V+',
    '5b': 'VI−',
    '5c': 'VI',
    '6a': 'VI+',
    '6a+': 'VII−',
    '6b': 'VII',
    '6b+': 'VII+',
    '6c': 'VIII−',
    '6c+': 'VIII−',
    '7a': 'VIII',
    '7a+': 'VIII+',
    '7b': 'VIII+/IX−',
    '7b+': 'IX−',
    '7c': 'IX',
    '7c+': 'IX+',
    '8a': 'IX+/X−',
    '8a+': 'X−',
    '8b': 'X',
    '8b+': 'X+',
    '8c': 'X+/XI−',
}

session = HTMLSession()
r = session.get("https://utlista.bigwall.hu")
route_elements = r.html.find(".route_row")
routes = [
    {
        "ID": el.attrs["data-number"],
        "Title": el.attrs["data-title"].strip(),
        "French grade": el.attrs["data-french-grade"],
        "UIAA grade": grade_dict[el.attrs["data-french-grade"]],
    }
    for el in sorted(route_elements, key=lambda x: x.attrs["data-number"])
]

if not routes:
    print('Hoppa, egy utat se talaltam a valaszban, lehuztak a rolot vagy mi a fasz van')
    sys.exit(1)

writer = csv.DictWriter(sys.stdout, fieldnames=['ID', 'Title', 'French grade', 'UIAA grade'], lineterminator='\n')
writer.writeheader()
for route in routes:
    writer.writerow(route)
