import os
import face_detect
import face_capturing
import face_update
import face_recogntion


# Title bar
def title_bar():
    os.system('cls')

    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


# Main menu
def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                checkcamera()
                break
            elif choice == 2:
                capturefaces()
                break
            elif choice == 3:
                trainimages()
                break
            elif choice == 4:
                recognizefaces()
                break
                mainMenu()
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
    exit


def checkcamera():
    print("Please wait, starting camera")
    face_detect.detect_face()
    key = input("Enter any key to return main menu")
    mainMenu()


def capturefaces():
    face_capturing.capture_face()
    key = input("Enter any key to return main menu")
    mainMenu()


def trainimages():
    print("updating facelist....")
    face_update.update_facelist()
    key = input("Enter any key to return main menu")
    mainMenu()


def recognizefaces():
    print("Please wait, starting camera")
    face_recogntion.recognize_faces()
    key = input("Enter any key to return main menu")
    mainMenu()


mainMenu()
