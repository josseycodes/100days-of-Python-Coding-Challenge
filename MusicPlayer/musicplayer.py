import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def main():
    print("Simple Music Player")
    print("-------------------")
    
    file_path = input("Enter the path of the music file (e.g., /path/to/your/song.mp3): ")
    if not os.path.exists(file_path):
        print("Invalid file path!")
        return

    play_music(file_path)

    while True:
        print("\nOptions:")
        print("1. Pause")
        print("2. Unpause")
        print("3. Stop")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            pause_music()
        elif choice == '2':
            unpause_music()
        elif choice == '3':
            stop_music()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    pygame.quit()

if __name__ == "__main__":
    main()

