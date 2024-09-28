import re

txt = "today is 12/09/2023, 2023-09-12, and Sep 12, 2023 hello 1234"
date = re.findall(r"\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|[A-Za-z]{3,} \d{1,2}, \d{4})\b", txt)

for i in date:
    print(i)
