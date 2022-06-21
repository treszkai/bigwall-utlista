import csv
import sys

from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://utlista.bigwall.hu")
route_elements = r.html.find(".route_row")
routes = [
    {
        "ID": el.attrs["data-number"],
        "French grade": el.attrs["data-french-grade"],
        "Title": el.attrs["data-title"].strip(),
    }
    for el in sorted(route_elements, key=lambda x: x.attrs["data-number"])
]

if not routes:
    print('Hoppa, egy utat se talaltam a valaszban, lehuztak a rolot vagy mi a fasz van')
    sys.exit(1)

writer = csv.DictWriter(sys.stdout, fieldnames=['ID', 'Title', 'French grade'], lineterminator='\n')
writer.writeheader()
for route in routes:
    writer.writerow(route)
