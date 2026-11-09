# Chan-chan: to save people to their own special '.chan' file <3 (v1.0)
Reused parts from my older [python file system simulator](https://github.com/pnuggie/python-file-system-simulator) to make this.

## About ^_^

Chan-chan is a small Python command-line program that lets you create, view, search, edit, and delete character files using a custom `.chan` file extension. It started as a joke after accidentally typing .chan instead of -chan. I am a loser, you see. But I would *never* stoop to those losercore playlist levels of loserism. Nonetheless, please enjoy!

**Warning**: swearing. Haha

## Features!

- Create individual `.chan` character files!
- View all saved characters.
- Search for characters by name.
- Edit character names, ages and traits.
- Delete character files.
- Automatically load previously saved characters when the program starts.

## What Chan-chan needs to run...

- Python 3 (No external packages required!)

### How to run

- Download or clone this repository
- Make sure Python 3 is installed pls pls pls
- Run the Python file from your terminal:

```
python chanchan.py
```

Or `py` if it doesn't work for whatever reason.

- Follow the menu options!

## The `.chan` file format

Each character is stored in a separate `.chan` file. The files contain basic character information, currently consisting of:

- Name
- Age
- Traits
    - however these can kind of be whatever you want, its a long string anyway ¯\_(ツ)_/¯

The `.chan` extension is custom to this project, as the files are currently plain-text files rather than an *actual* file format. But it's pretty convincing, right?!

## Limitations in v1.0

This is an early version of the project, therefore it's ~~fucking shit~~ got a few issues, mostly regarding user error and developer tiredness. Here's a list:

- Character names are used as filenames, meaning duplicate names can overwrite existing character files.
- `.chan` files use a simple pipe-separated format (`name|age|traits`). Names and traits containing the `|` character can cause loading errors. Very basic I know.
- Chan-chan expects `.chan` files to follow its original formatting. Manually modifying files into an invalid format may prevent them from loading. But that's kind of on you.
- Character information is stored and loaded on a single line. Multi-line traits are not currently supported.
- `.chan` files are stored in the directory from which the program is run.

Future improvements will be attempts to fix these various issues.

## Here's some photos!

<img width="839" height="404" alt="image" src="https://github.com/user-attachments/assets/6cf1db08-f7a0-4158-9d18-51523f4ac1c8" />
What you see when you first open Chan-chan.

<img width="350" height="84" alt="image" src="https://github.com/user-attachments/assets/5cdb05e6-1843-48ee-81e2-cc43cccd3723" />
Change specific categories of the character file rather than the entire thing. This is an improvement from the original file sim.

<img width="443" height="460" alt="image" src="https://github.com/user-attachments/assets/e435f4ec-9843-43ca-8a22-da94248d6135" />
Add a character. Search up the character with same letters even if not the same case. It's cool.

<img width="323" height="118" alt="image" src="https://github.com/user-attachments/assets/04dcb141-53af-436f-8c3b-add161515572" />
The `.chan` file in action.

<img width="227" height="121" alt="image" src="https://github.com/user-attachments/assets/7b902390-df35-4e63-9c73-7f48b435274b" />
It remembers how many `.chan` files there are. This is due to `glob.glob("*.chan")` (glob will never not be funny) which returns a list of file paths with my custom extension.

<img width="421" height="87" alt="image" src="https://github.com/user-attachments/assets/223a3862-b737-4a21-a66b-403a4f905147" />
Little easter egg.
