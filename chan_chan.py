import time
from time import sleep
import glob # LMAO
from pathlib import Path # another new thing im adding. i dont want to mess with os, so google said this should work...

# repurposed from my file simulator thingamajig

# saving the files SEPERATELY!!!!!!!! 
def savefiles():
    for f in files:
        filename = f["name"] + ".chan"

        with open(filename, "w") as file:
            file.write(
                f["name"] + "|" +
                str(f["age"]) + "|" +
                f["traits"] + "\n"
            )

# loading the files and making them accessable in variables
def loadfiles():
    chanfiles = glob.glob("*.chan")

    if not chanfiles:
        print("no .chan file found yet, you should make one!")
        return

    for filename in chanfiles:
        with open(filename, "r") as file:
            name, age, traits = file.readline().strip().split("|")

            savedfile = {
                "name": name,
                "age": int(age),
                "traits": traits
            }

            files.append(savedfile)

# main program

print(r""" 


░█████╗░██╗░░██╗░█████╗░███╗░░██╗░░░░░░░█████╗░██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗██║░░██║██╔══██╗████╗░██║░░░░░░██╔══██╗██║░░██║██╔══██╗████╗░██║
██║░░╚═╝███████║███████║██╔██╗██║█████╗██║░░╚═╝███████║███████║██╔██╗██║
██║░░██╗██╔══██║██╔══██║██║╚████║╚════╝██║░░██╗██╔══██║██╔══██║██║╚████║
╚█████╔╝██║░░██║██║░░██║██║░╚███║░░░░░░╚█████╔╝██║░░██║██║░░██║██║░╚███║
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

""") # required

files = []
loadfiles()
    
while True: # nice menu huh
    print("Chan-chan: to save your characters to their own special '.chan' file <3 (v1.0)")
    print()
    print("loading Chan-chan...")
    sleep(2)

    print("total files:", len(files))

        
    print("""        1. add new .chan file 
        2. view all .chan files
        3. search for a .chan file
        4. delete a .chan file
        5. rewrite a .chan file
        6. exit
        7. info""") # 8 spaces after 1.

    try:
        choice = int(input("choose 1-7: "))
        print()
    except ValueError:
        print("invalid input, please enter a number 1-7")
        continue

    if choice == 1: # asks for all the content info whatever needed
        name = input("character name: ")
        age = int(input("character age: "))
        traits = input("character traits: ")

        if name.lower() == "chan-chan":
            print("Chan-chan is honoured! but you should try someone else :) ")
            continue

        file = { #organises it nicely with the variables
            "name": name, # key for the files name
            "age": age,
            "traits": traits
        }

        files.append(file) # appends it to my file (below)
        savefiles() #saves :D
        print(".chan file added!") # confirmation
        print()

    elif choice == 2:
        if len(files) == 0:
            print("no .chan files yet. :( you should make one!")
            print()
        else:
            for f in files: # go through all files and print them all cause we want them all
                print("character name:", f["name"])
                print()

    elif choice == 3:
        filename = input("enter character name to search: ")

        found = False

        for f in files:  # below, the .lower() makes it so anything like Hello and hello can both appear as a search result
            if f["name"].lower() == filename.lower(): # the 'name' is a key/variable, as seen above. should match
                print("\n--- file opened ---")
                print("name:", f["name"])
                print("age:", f["age"]) 
                print("traits", f["traits"]) # e.g name: 'file (f)' 'name of the file' 
                print()
                found = True
                break

        if not found:
            print(".chan file not found. :(")
            print()

    elif choice == 4:
        filename = input("enter character to delete: ")

        found = False

        for f in files:
            if f["name"].lower() == filename.lower(): # is what user entered same as the found file wanted

                confirm = input("are you sure? y/n: ")

                if confirm.lower() != "y":
                    print("deletion cancelled")
                    print()
                    found = True
                    break

                filename = f["name"] + ".chan"

                files.remove(f)
                Path(filename).unlink()

                print("file deleted successfully.")
                print()
                found = True
                break

        if not found:
            print("file not found. :(")
            print()

    elif choice == 5:
        filename = input("enter character to edit details of: ")
    
        found = False
    
        for f in files:
            if f["name"].lower() == filename.lower():

                found = True

                print("current content:", f["name"], f["age"], f["traits"])
            
                changeitem = input("what do you want to change? (name, age, traits): ").lower()

                if changeitem == "name":
                    oldfilename = f["name"] + ".chan"

                    if newname.lower() == f["name"].lower():
                        print("that's already their name! this might cause a problem with files if you force it.")

                    f["name"] = input("new name: ")
                    savefiles()

                    Path(oldfilename).unlink() # delete og after replacement. this save is important.

                elif changeitem == "age":
                    try:
                        f["age"] = int(input("new age: "))
                    except ValueError:
                        print("age must be a number!")
                        break
                elif changeitem == "traits":
                    f["traits"] = input("new traits: ")

                else:
                    print("invalid category!")
                    break

                savefiles() # yeah its redundant shut up it might be important
                print("file updated!")
                print()
                print("now its:", f["name"], f["age"], f["traits"])

                break # i dont even need an else here, waow

        if not found:
            print("file not found. :(")
            print()

    elif choice == 6:
        savefiles() # final backup
        print("bye bye!! Chan-chan and the others are waiting for you!")
        sleep(2)
        break

    elif choice == 7:
        print("hello!! welcome to Chan-chan's info section!")
        sleep(1)
        print()
        print("Chan-chan can save character files for you, including their precious information! although, Chan-chan has a few limitations.\nfor example, Chan-chan sucks at working around human errors >.<")
        sleep(1)
        print()
        print("you search for things by name, in .chan files. for example:\nif i want Chan-chan's info, i'm going to choose option 3, search cHan-ChAn (any case!), and it will retrieve Chan-chan's info for me!")
        sleep(1)
        print()
        print("the characters are saved in their own '.chan' files! how kawaii!~ ne? you can even make one for Chan-chan, and put whatever you like!")
        sleep(1)
        print()
        print("if you want to manipulate them without the help of Chan-chan, Chan-chan will be a little sad...\nbut yes, you can find your beloved's .chan file in your file explorer! it's just a cuter text file, after all.")
        sleep(1)
        print()
        print("traits can be anything you want! they dont have to necessarily be traits, but they make more sense.\nyou can have long winded explanations of lore, or a short one word trait.")
        sleep(1)
        print()
        print("Chan-chan has no gender, as Chan-chan doesn't give a shit.")

    else:
        print("invalid choice, please select 1-5")
        print()