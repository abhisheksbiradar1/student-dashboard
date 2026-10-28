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

## Installation and Setup

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m streamlit run "student dashboard.py"
   ```

5. Open the local URL displayed in the terminal.

## Attendance Status

- **Dropped Out:** Attendance below 50%.
- **At Risk:** Attendance from 50% to below 75%.
- **Active:** Attendance of 75% or above.

## Data Storage

Student records are stored locally in `students.json`. This file is excluded from Git using `.gitignore` so local student data is not intentionally committed to the repository.

## Future Improvements

- Add student search and filtering.
- Improve input validation and error handling.
- Add export options for student reports.
- Improve dashboard presentation and reporting.

## Author

Abhishek S Biradar
