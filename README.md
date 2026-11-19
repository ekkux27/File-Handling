# 🗂️ FileVault

A premium, dark-themed file manager built with [Streamlit](https://streamlit.io). FileVault gives a clean web interface to **create, read, update and delete** text files, with a glassmorphism look, gradient accents and smooth hover effects.

## ✨ Features

- **Dashboard**: total files, storage used, last-modified file and a recent-files list
- **Create**: make a new file; warns if the name already exists
- **Read**: preview a file with size and character stats, and download a copy
- **Update**: overwrite a file (editor pre-filled with its content) or append to it
- **Delete**: permanent removal behind a confirmation checkbox
- **Safe by design**: files live in a `workspace/` folder, and names containing slashes or `..` are rejected so nothing is written outside it

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or newer

### Installation

```bash
git clone https://github.com/<ekkux27>/<File-Handling>.git
cd <File-Handling>
pip install -r requirements.txt
```

### Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## 📁 Project Structure

```
.
├── app.py             # Streamlit application
├── requirements.txt   # Dependencies
├── workspace/         # Created automatically; stores your files
└── README.md
```

## 🛠️ How It Works

| Page      | What it does                                         |
|-----------|------------------------------------------------------|
| Dashboard | Shows stats and the 10 most recently modified files  |
| Create    | Writes a new UTF-8 text file into `workspace/`       |
| Read      | Displays file content and offers a download          |
| Update    | Overwrites or appends to an existing file            |
| Delete    | Removes a file after you confirm                     |

## ⚠️ Notes

- Only UTF-8 text files can be previewed or edited.
- Deleted files are removed permanently (no trash or undo).
- The `workspace/` folder is local to wherever the app runs; if you deploy it, files are stored on that server.

## 🗺️ Ideas for Next Steps

- Search and filter files
- Upload existing files
- Rename files
- Light/dark theme toggle

## 📄 License

Add a license of your choice (for example MIT) before sharing publicly.
