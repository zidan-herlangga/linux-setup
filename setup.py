from Library import fungsi

def menu():
    fungsi.author()
    if fungsi.check_internet():
        while True:
            try:
                fungsi.author()
                print()
                print("1. Update System")
                print("2. Upgrade System")
                print("3. Download and Install Google Chrome")
                print("4. Download and Install Visual Studio Code")
                print("5. Exit")
                
                choice = input("\nMasukkan pilihan Anda: ")

                if choice == "1":
                    update_choice = input("[?] Apakah Anda ingin melakukan update (Y/n)? ")
                    fungsi.update(update_choice)
                elif choice == "2":
                    upgrade_choice = input("[?] Apakah Anda ingin melakukan upgrade (Y/n)? ")
                    fungsi.upgrade(upgrade_choice)
                elif choice == "3":
                    download_chrome_choice = input("[?] Apakah Anda ingin mendownload dan menginstall Google Chrome (Y/n)? ")
                    fungsi.download_chrome(download_chrome_choice)
                elif choice == "4":
                    download_vscode_choice = input("[?] Apakah Anda ingin mendownload dan menginstall Visual Studio Code (Y/n)? ")
                    fungsi.download_vscode(download_vscode_choice)
                elif choice == "5":
                    print("[!] Program selesai.")
                    break
                else:
                    print("[!] Pilihan tidak valid.")
            
            except KeyboardInterrupt:
                print("\n[!] Program selesai.")
                break
    

if __name__ == "__main__":
    menu()