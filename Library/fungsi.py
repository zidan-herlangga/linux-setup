import os
import socket
from time import sleep, localtime, strftime

os.system("clear" if os.name == "posix" else "")


named_tuple = localtime()
time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

path = "Download"
path_download = f"wget -P {path}"
path_move = f"cd {path}"

if os.name not in "posix":
    print("[!] Akses ditolak.")
    exit()

def author():
    print(f"""
[!] Setup Your Linux one Click

Author  :   Zidan Herlangga
Github  :   https://github.com/zidan-herlangga
Version :   1.0
Time    :   {time_string}
-----------------------------------------------""")

# Internet Check
def check_internet():
    try:
        socket.create_connection(("www.detik.com", 443))
        print("[!] Mohon tunggu, sedang mengecek koneksi internet..."), sleep(3)
        print("[!] Internet terhubung."), sleep(1), os.system("clear" if os.name == "posix" else "")
        return True
    
    except OSError:
        print("[!] Mohon tunggu, sedang mengecek koneksi internet..."), sleep(3)
        print("[!] Tidak dapat terhubung ke internet.")
        exit()

# Update Function
def update(oke):
    if oke == "y".lower():
        print("[!] Mohon tunggu..."), sleep(2)
        os.system("sudo apt-get update")
        print("[!] System telah di update."), sleep(2), os.system("clear" if os.name == "posix" else "")
    
    else:
        print("[!] System tidak di update.")
        pass

# Upgrade Function
def upgrade(oke):
    if oke == "y".lower():
        print("[!] Mohon tunggu..."), sleep(2)
        os.system("sudo apt-get upgrade")
        print("[!] System telah di upgrade."), sleep(2), os.system("clear" if os.name == "posix" else "")
    
    else:
        print("[!] System tidak di upgrade.")
        pass

# Chrome Download Function
def download_chrome(oke):
    if oke == "y".lower():
        print("[!] Mohon tunggu..."), sleep(2)
        os.system(f"{path_download} https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        print("[!] Package telah di download.")

        install = input("\n[?] Apakah ingin mengintall (Y/n)? ")
        if install == "y".lower():
            os.system(f"sudo dpkg -i {path}/google-chrome-stable_current_amd64.deb")
            print("[!] Package telah di install."), sleep(2), os.system("clear" if os.name == "posix" else "")
        else:
            print("[!] Package tidak di install."), sleep(2), os.system("clear" if os.name == "posix" else "")
            return

        if os.path.isfile("/usr/bin/google-chrome"):
            print("[!] Package sudah di install.")
        
    else:
        print("[!] Package tidak di download.")
        pass

# Visual Code Download Function
def download_vscode(oke):
    if oke == "Y" or oke == "y":
        print("[!] Mohon tunggu..."), sleep(2)
        os.system(f"{path_download} https://go.microsoft.com/fwlink/?LinkID=760868")
        os.system("mv index.html\?LinkID=760868 VSCode-Linux-x64-Installer.deb")
        print("[!] Package telah di download.")

        install = input("\n[?] Apakah ingin mengintall (Y/n)? ")
        if install == "y".lower():
            os.system(f"sudo dpkg -i {path}/VSCode-Linux-x64-Installer.deb")
        else:
            print("[!] Package tidak di install."), sleep(2), os.system("clear" if os.name == "posix" else "")
            return

        if os.path.isfile("/usr/bin/code"):
            print("[!] Package sudah di install.")
    
    else:
        print("[!] Package tidak di download."), sleep(2), os.system("clear" if os.name == "posix" else "")
        pass