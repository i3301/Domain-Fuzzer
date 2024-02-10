import requests
from colorama import Fore

def print_banner():
    try:
        with open("banner.txt", 'r', encoding='utf-8') as file:
            banner_content = file.read()
            print(f"{banner_content}")
    except FileNotFoundError:
        print(f"Error: File 'banner.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_banner()

Base = input(f"{Fore.MAGENTA}[+]Enter Default Domain: ")

FILE_PATH = input(f"{Fore.MAGENTA}[+]Wordlist Path(No parentheses): ")

with open(FILE_PATH, "r") as file:
    wordlist = [line.strip() for line in file.readlines()]
    
def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{Fore.GREEN}[+]{url} -XSS Found")
     
print(f"{Fore.BLUE}[+]Working. . .")
        
for word in wordlist:
    url = Base + "/" + word
    make_request(url)
input("Press Enter To Exit. . .")