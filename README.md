
# Task Manager

## Description

Task Manager is a simple GUI-based application built using Python and Tkinter. It allows users to add, edit, delete, view, and save tasks. Tasks include details such as title, category, due date, and priority. The application also saves tasks in a JSON file to maintain persistence.

## Features

- Add new tasks with title, category, details, due date, and priority.
- Edit existing tasks.
- Delete selected tasks.
- View all tasks in a list.
- Save tasks to a JSON file for persistence.
- Load tasks from the JSON file when the application starts.

## Prerequisites

Ensure you have Python installed on your system. You can check by running:

```sh
python --version
```

If Python is not installed, download and install it from [Python's official website](https://www.python.org/downloads/).

## Installation

1. Clone the repository:

```sh
git clone https://github.com/vinaythanay/task-manager.git
```

2. Navigate to the project directory:

```sh
cd task-manager
```

3. Install required dependencies (if any):

```sh
pip install tkinter
```

(Tkinter is included in standard Python installations, but install it if necessary.)

## Usage

1. Run the application:

```sh
python task_manager.py
```

2. Use the interface to add, edit, delete, and view tasks.
3. Click **Save** to store tasks in `tasks.json`.

## File Structure

```
📂 task-manager
 ┣ 📜 task_manager.py   # Main Python script
 ┣ 📜 tasks.json        # JSON file for storing tasks
 ┗ 📜 README.md         # Project documentation
```

## Deployment

To push this project to GitHub, follow these steps:

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/vinaythanay/task-manager.git
git push -u origin main
```


## Author

This project was created and maintained by Vinay Kumar.
