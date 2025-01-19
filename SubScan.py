import requests
from colorama import Fore, Style, init

# Toggling colors
init(autoreset=True)

# Custom Colors
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
reset = Style.RESET_ALL

# Reading subdomains from file
def read_subdomains_from_file(file_path):
    subdomains = []
    try:
        with open(file_path, 'r') as file:
            subdomains = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"{red}File not found: {file_path}{reset}")
    return subdomains

# List of subdomains from file
subdomains = read_subdomains_from_file('subdomains.txt')  # Change file name if needed

if not subdomains:
    print(f"{red}No subdomains found in the file.{reset}")
    exit()

# Display tool information
print(f"""
{yellow}
    Coded By GHOST Lolzik
    Telegram : @WW6WW6WW6
    GitHub: https://github.com/GhostLolzik
    All rights reserved.
{reset}

            o  o   o  o
         |\\/ \\^/ \\/|  
         |,-------.|  
       ,-.(|)   (|),-. 
       \\_*._ ' '_.* _/  
        /-.--' .-`\\  
   ,--./    `---'    \\,--. 
   \\   |(  )     (  )|   /  
hjw \\  |         |  /  
`97  \\ | /|\\     /|\\ | /  
     /  \\-._     _,-/  \\  
    //| \\  `---'  // |\\\\  
   /,-.,-.\\       /,-.,-.\\  
  o   o   o      o   o    o  
""")

# Result lists
working_subdomains = []
not_working_subdomains = []

# Handle Ctrl + C interruption
try:
    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}", timeout=5)
            if response.status_code == 200:
                print(f"{green}{subdomain} - Found")
                working_subdomains.append(subdomain)
            else:
                print(f"{red}{subdomain} - No Found")
                not_working_subdomains.append(subdomain)
        except requests.exceptions.RequestException:
            print(f"{red}{subdomain} - No Found")
            not_working_subdomains.append(subdomain)

    # Display final statistics
    print("\n" + "="*30)
    print(f"{green}Found: {len(working_subdomains)}")
    print(f"{red}No Found: {len(not_working_subdomains)}")
    print("="*30)

    # Save the working subdomains (Found) to a file
    with open("found.txt", "w") as f:
        for subdomain in working_subdomains:
            f.write(subdomain + "\n")
    print(f"{green}Found subdomains have been saved to 'found.txt'.")

except KeyboardInterrupt:
    # Handling forced exit
    print(f"\n{yellow}Operation was interrupted. Exiting gracefully...{reset}")
