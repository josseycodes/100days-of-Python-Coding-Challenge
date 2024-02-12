import shutil
import os
import time
import schedule

def backup(source_dir, dest_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Copy files from source to destination
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, os.path.relpath(source_file, source_dir))
            shutil.copy2(source_file, dest_file)
    print("Backup completed successfully.")

def incremental_backup(source_dir, dest_dir):
    # TODO: Implement incremental backup logic
    print("Incremental backup is not yet implemented.")

def restore(source_dir, dest_dir):
    # Copy files from source to destination
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, os.path.relpath(source_file, source_dir))
            shutil.copy2(source_file, dest_file)
    print("Restore completed successfully.")

def schedule_backup(source_dir, dest_dir, interval):
    schedule.every(interval).hours.do(backup, source_dir, dest_dir)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    source_dir = input("Enter the source directory: ")
    dest_dir = input("Enter the destination directory: ")

    print("Choose an option:")
    print("1. Backup")
    print("2. Incremental Backup")
    print("3. Restore")
    print("4. Schedule Backup")

    choice = input("Enter your choice: ")

    if choice == "1":
        backup(source_dir, dest_dir)
    elif choice == "2":
        incremental_backup(source_dir, dest_dir)
    elif choice == "3":
        restore(source_dir, dest_dir)
    elif choice == "4":
        interval = int(input("Enter backup interval in hours: "))
        schedule_backup(source_dir, dest_dir, interval)
    else:
        print("Invalid choice.")
