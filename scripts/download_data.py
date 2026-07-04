import urllib.request
import os

url = "https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/netflix_titles.csv"
output_path = os.path.join(os.path.dirname(__file__), "..", "data", "netflix_titles.csv")
output_path = os.path.abspath(output_path)

print(f"Downloading dataset from {url}...")
urllib.request.urlretrieve(url, output_path)
print(f"Dataset successfully downloaded to {output_path}")
