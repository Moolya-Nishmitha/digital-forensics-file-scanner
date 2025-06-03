# Digital Forensics File Scanner

A lightweight Python script to scan folders and flag suspicious files based on:

- File extensions like `.exe`, `.bat`, `.js`, `.vbs`
- Large files over 10MB
- Filenames containing keywords such as “password”, “secret”, or “malware”

---

## How to Run

1. Clone this repo or download the files.
2. Open a terminal and navigate to the project directory.
3. Run the script with:

```bash
python3 scanner.py
```
When prompted, enter the path of the folder you want to scan.

Example paths:

/Users/nish/Desktop/test-folder (Mac/Linux)

C:\Users\Nish\Desktop\test-folder (Windows)

Check the output for any flagged suspicious files.

What It Does
The script walks through the folder, checking each file’s:

Extension (flags risky types)

Size (flags anything bigger than 10MB)

Filename (looks for keywords)

If a file looks shady, it prints the path and why.

Why Use This?
Quick way to spot potentially harmful files.

Great for beginners learning Python and file operations.

A solid foundation for more advanced digital forensics tools.

About Me
honestly I am just playing around


