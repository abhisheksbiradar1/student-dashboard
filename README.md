# Student Dropout & Attendance Dashboard

A Python-based web application built with Streamlit to manage student records, monitor attendance and marks, and visualize academic performance through interactive dashboards.

## Features

- **Add Students:** Record student names, departments, academic years, attendance, and marks.
- **Edit Student Records:** Update existing student information.
- **Delete Student Records:** Remove student records when required.
- **Attendance Monitoring:** Categorize students based on attendance percentage.
- **Academic Performance:** Visualize student marks and attendance using interactive charts.
- **Status Summary:** Display total students and status-wise counts.
- **Students Requiring Attention:** Identify students who may need academic support.
- **Persistent Local Storage:** Save student records in a JSON file so they can be loaded again when the application restarts.

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- JSON for local data storage

## Project Structure

```text
student-dropout-attendance-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── students.json          # Generated locally when records are saved
```

The `students.json` file may not exist until the application saves its first student record. It should not be committed if it contains real or private student information.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-dropout-attendance-dashboard
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of this repository.

If you already have the project on your laptop, open its folder instead of cloning it again.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If you use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can interact with the dashboard.

## Attendance Status Rules

- Attendance below 50%: Dropped Out (current project classification)
- Attendance from 50% to below 75%: At Risk
- Attendance of 75% or above: Active

These are project-defined categories, not proof that a student has actually dropped out.

## Data Storage

Student records are stored locally in `students.json`. This is suitable for a small demonstration project. The current storage approach is not designed for concurrent users or production deployment.

Use synthetic or anonymized student information when testing or demonstrating the application.

## Future Improvements

- Add search, filtering, and sorting.
- Improve input validation and duplicate-record handling.
- Add CSV import and export.
- Add confirmation before deleting records.
- Improve error handling and data validation.
- Add automated tests.
- Consider a database for more reliable storage.
- Deploy the dashboard online.

## Author

**Abhishek S Biradar**

AI & Data Science Engineering Student

