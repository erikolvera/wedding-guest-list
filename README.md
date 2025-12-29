# Wedding Guest List 💍

A Python based Command Line Interface application to manage wedding guest lists. This tool allows users to maintain separate lists for the Groom and Bride, track the total count, and save data persistently to a JSON file.

## Features

* **Persistent Storage:** Automatically saves guest names to `guest_lists.json` so data isn't lost when the program closes.
* **Dual Lists:** Manages separate lists for the Groom and the Bride.
* **Batch Adding:** Add multiple guests in a row without navigating back to the main menu.
* **Smart Removal:** Case insensitive search to remove guests from either list easily.
* **Guest Analytics:** View specific lists or get a total count of all attending guests.

## Prerequisites

* **Python 3.10+**: This project uses `match`/`case` syntax, which requires Python version 3.10 or higher.

## Project Structure

To run this code, ensure your files are organized in the following directory structure. The `main.py` file relies on the `functions` package.

```text
wedding-guest-manager/
├── main.py
└── functions/
    ├── __init__.py      (Optional)
    ├── add_guest.py
    ├── remove_guest.py
    ├── view_guests.py
    ├── guest_count.py
    └── data.py
```
## Installation & Usage
1) Clone or download this repository  
2) Navigate to the root directory of the project in your terminal  
3) Run the application: `python main.py`
