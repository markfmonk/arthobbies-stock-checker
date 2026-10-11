import urllib.request

URL = “https://arthobbies.com.mx”

def main():
print(“Checking ArtHobbies for Necromunda: Gangs of the Underhive”)
try:
request = urllib.request.Request(
URL,
headers={“User-Agent”: “Mozilla/5.0”}
)
with urllib.request.urlopen(request, timeout=20) as response:
page = response.read().decode(“utf-8”, errors=“ignore”)

    if "Gangs of the Underhive" in page:
        print("The product name appears on the homepage.")
        print("This does not yet confirm that it is in stock.")
    else:
        print("Product name not found on the homepage.")
except Exception as error:
    print("Could not check the website:", error)

if name == “main”:
main()
