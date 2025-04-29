# 🏖 kumCTF

**kumCTF** is a beginner-friendly Capture The Flag (CTF) tool designed to help new learners practice basic pentesting and cybersecurity techniques.


## 🎯 ## Features

### Main Modules:
- **Information Gathering**
  - Tools: `whois`, `nslookup`, `dig`, `ping`
- **Scanning**
  - Tools: `rustscan`, `netdiscover`, `nmap (detailed)`, `nmap (service version scan)`
- **Privilege Escalation**
  - Provides examples for obtaining basic and reverse shells.
  - **Note:** Full privilege escalation involves more advanced techniques using tools like `linpeas` and `linenum`. However, kumCTF does not download external scripts (e.g., via wget) to maintain simplicity and focus on the basics.
- **Password Cracking**
  - Tools: `john`, `hashcat`
  - **Note:** Only MD5 hashes are targeted to keep it simple and educational for beginners.

Here is the main menu of kumCTF, showcasing the available modules:

![kumCTF Main Menu](https://github.com/tunakum/kumCTF/blob/b8947bb89110dd0ced9ae658414925af81b580a5/kumCTFmainmenu.png)

## 🛠 Used Technologies

### Python Libraries
- `rich` — For colorful CLI interfaces, tables, and styled outputs.
- **pyfiglet** — For generating ASCII art in the welcome screen.
- **subprocess** — For executing external system commands (e.g., nmap, ping).
- **os** — For system operations like clearing the terminal.
- **re** — For handling input validations with regular expressions.

### External Tools (System Commands)
- **nmap** — Network scanning and service detection.
- **rustscan** — Fast port scanning.
- **netdiscover** — Network discovery to find live hosts.
- **whois**, **nslookup**, **dig**, **ping** — Information gathering and DNS querying tools.
- **john**, **hashcat** — Password cracking tools (focused on MD5 hashes).

> Note: External tools must be installed separately on your system.


## ⚠ Disclaimer

This tool is intended **for educational and ethical hacking purposes only**.  
It must **NOT** be used for illegal or unauthorized activities.

Always ensure you have **explicit permission** before testing or interacting with any system or network.

By using **kumCTF**, you agree that you are solely responsible for your actions.
---

## 📦 Requirements

- Python 3.x
- Install dependencies using:

```bash
git clone https://github.com/tunakum/kumCTF.git
cd kumCTF
pip install -r requirements.txt
python3 main.py
