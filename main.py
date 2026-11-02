from storage import (
    upload_file,
    list_files,
    download_file,
    delete_file,
    generate_url
)

while True:
    print("\n=== R2 STORAGE MANAGER ===")
    print("1. Upload file")
    print("2. List files")
    print("3. Download file")
    print("4. Delete file")
    print("5. Generate download URL")
    print("0. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        path = input("File path: ")
        upload_file(path)

    elif choice == "2":
        list_files()

    elif choice == "3":
        filename = input("Filename: ")
        download_file(filename)

    elif choice == "4":
        filename = input("Filename: ")
        delete_file(filename)

    elif choice == "5":
        filename = input("Filename: ")
        generate_url(filename)

    elif choice == "0":
        break

    else:
        print("Invalid choice")
