import re
from collections import defaultdict

log_data = """
2023-05-10 10:15:30 User123 Login
2023-05-10 10:17:45 User123 ViewItem:Item456
2023-05-10 10:20:10 User123 AddToCart:Item456
2023-05-10 10:25:20 User123 Logout
2023-05-10 11:15:30 User456 Login
2023-05-10 11:17:45 User456 ViewItem:Item789
2023-05-10 11:20:10 User456 AddToCart:Item789
2023-05-10 11:25:20 User456 Logout
2023-05-10 12:15:30 User789 Login
2023-05-10 12:17:45 User789 ViewItem:Item123
2023-05-10 12:25:20 User789 Logout
2023-05-10 13:15:30 User101112 Login
2023-05-10 13:17:45 User101112 ViewItem:Item456
2023-05-10 13:20:10 User101112 AddToCart:Item456
2023-05-10 13:25:20 User101112 Logout
2023-05-10 14:15:30 User131415 Login
2023-05-10 14:17:45 User131415 ViewItem:Item789
2023-05-10 14:25:20 User131415 Logout
2023-05-11 10:15:30 User123 Login
2023-05-11 10:17:45 User123 ViewItem:Item111
2023-05-11 10:20:10 User123 AddToCart:Item111
2023-05-11 10:25:20 User123 Logout
2023-05-12 10:15:30 User123 Login
2023-05-12 10:17:45 User123 ViewItem:Item111
2023-05-12 10:20:10 User123 AddToCart:Item111
2023-05-12 10:25:20 User123 Logout
User999 ViewItem:Item456
User999 AddToCart:Item456
"""

viewed_items = defaultdict(set)
added_items = defaultdict(set)

lines = log_data.split("\n")
for line in lines:
    match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (User\d+) (ViewItem|AddToCart):(Item\d+)", line)
    if match:
        date, user, action, item = match.groups()
        if action == "ViewItem":
            viewed_items[user].add(item)
        elif action == "AddToCart":
            added_items[user].add(item)

for user in viewed_items.keys():
    common_items = viewed_items[user].intersection(added_items[user])
    if common_items:
        print(f"User {user} viewed and added the following items to Cart: {', '.join(sorted(common_items))}")