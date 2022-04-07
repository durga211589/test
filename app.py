import pandas as pd

df = pd.DataFrame()
print(df)

import requests

res = requests.get('https://stackoverflow.com/questions/56658553/module-not-found-error-in-vs-code-despite-the-fact-that-i-installed-it')

print(res.status_code)