#Code for the project of student dashboard  and it also saves automatically  to csv file
import pandas as pd
import streamlit as st
import plotly.express as px
import json
import os

# ──────────────────────────────────────────
# PAGE SETUP
# ──────────────────────────────────────────
st.set_page_config(page_title="Student Dashboard", page_icon="🎓", layout="wide")
st.title("🎓 Student Dropout & Attendance Dashboard")
st.markdown("---")

# ──────────────────────────────────────────
# SAVE & LOAD FROM FILE (Permanent Storage)
# Data is saved in students.json file
# So data stays even after closing the app!
# ──────────────────────────────────────────
DATA_FILE = "students.json"

def load_data():
    # If file exists, load from it
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []   # if no file yet, start empty

def save_data(students):
    # Save to file every time data changes
    with open(DATA_FILE, "w") as f:
        json.dump(students, f)

# ──────────────────────────────────────────
# LOAD DATA INTO SESSION STATE
# ──────────────────────────────────────────
if 'students' not in st.session_state:
    st.session_state.students = load_data()  # load from file!

# ──────────────────────────────────────────
# STATUS FUNCTION
# ──────────────────────────────────────────
def check_status(att):
    if att < 50:
        return 'Dropped Out'
    elif att < 75:
        return 'At Risk'
    else:
        return 'Active'
# ──────────────────────────────────────────
# 4 TABS
# ──────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Add Student",
    "✏️ Edit Student",
    "🗑️ Delete Student",
    "📊 Dashboard"
])

# ══════════════════════════════════════════
# TAB 1 — ADD STUDENT
# ══════════════════════════════════════════
with tab1:
    st.subheader("➕ Add New Student")

    with st.form("add_form", clear_on_submit=True):
        c1, c2 = st.columns(2)

        with c1:
            name       = st.text_input("👤 Student Name")
            department = st.selectbox("📚 Department", ["AIDS", "CSE", "Mech", "ECE", "Civil"])
            year       = st.selectbox("📅 Year", [1, 2, 3, 4])

        with c2:
            attendance = st.number_input("📊 Attendance %",  min_value=0, max_value=100, value=0)
            marks      = st.number_input("📝 Marks (0-100)", min_value=0, max_value=100, value=0)

        add_btn = st.form_submit_button("✅ Add Student", use_container_width=True)

        if add_btn:
            if name.strip() == "":
                st.error("❌ Please enter student name!")
            else:
                existing = [s['Name'].lower() for s in st.session_state.students]
                if name.strip().lower() in existing:
                    st.error(f"❌ '{name}' already exists!")
                else:
                    st.session_state.students.append({
                        'Name':       name.strip(),
                        'Department': department,
                        'Year':       year,
                        'Attendance': attendance,
                        'Marks':      marks
                    })
                    save_data(st.session_state.students)  # 💾 save to file!
                    st.success(f"✅ {name} added and saved permanently!")

    if len(st.session_state.students) > 0:
        st.markdown("### 📋 Current Students")
        df_view = pd.DataFrame(st.session_state.students)
        df_view['Status'] = df_view['Attendance'].apply(check_status)
        st.dataframe(df_view, use_container_width=True, hide_index=True)
        st.info(f"💾 Total {len(st.session_state.students)} students saved in file.")
    else:
        st.info("📭 No students yet. Add your first student above!")

# ══════════════════════════════════════════
# TAB 2 — EDIT STUDENT
# ══════════════════════════════════════════
with tab2:
    st.subheader("✏️ Edit Student Details")

    if len(st.session_state.students) == 0:
        st.info("📭 No students to edit. Please add students first!")
    else:
        names_list = [s['Name'] for s in st.session_state.students]
        selected   = st.selectbox("🔎 Select student to edit:", names_list)

        idx     = next(i for i, s in enumerate(st.session_state.students) if s['Name'] == selected)
        student = st.session_state.students[idx]

        st.write(f"Editing: **{student['Name']}**")

        with st.form("edit_form"):
            c1, c2 = st.columns(2)

            with c1:
                new_name  = st.text_input("👤 Name",      value=student['Name'])
                new_dept  = st.selectbox("📚 Department", ["AIDS","CSE","Mech","ECE","Civil"],
                                          index=["AIDS","CSE","Mech","ECE","Civil"].index(student['Department']))
                new_year  = st.selectbox("📅 Year",       [1,2,3,4],
                                          index=[1,2,3,4].index(student['Year']))

            with c2:
                new_att   = st.number_input("📊 Attendance %",  min_value=0, max_value=100, value=student['Attendance'])
                new_marks = st.number_input("📝 Marks (0-100)", min_value=0, max_value=100, value=student['Marks'])

            save_btn = st.form_submit_button("💾 Save Changes", use_container_width=True)

            if save_btn:
                if new_name.strip() == "":
                    st.error("❌ Name cannot be empty!")
                else:
                    st.session_state.students[idx] = {
                        'Name':       new_name.strip(),
                        'Department': new_dept,
                        'Year':       new_year,
                        'Attendance': new_att,
                        'Marks':      new_marks
                    }
                    save_data(st.session_state.students)  # 💾 save to file!
                    st.success(f"✅ {new_name} updated and saved permanently!")
                    st.rerun()

# ══════════════════════════════════════════
# TAB 3 — DELETE STUDENT
# ══════════════════════════════════════════
with tab3:
    st.subheader("🗑️ Delete Student")

    if len(st.session_state.students) == 0:
        st.info("📭 No students to delete. Please add students first!")
    else:
        names_list     = [s['Name'] for s in st.session_state.students]
        del_name       = st.selectbox("Select student to delete:", names_list)
        student_to_del = next(s for s in st.session_state.students if s['Name'] == del_name)

        st.write(f"**Name:** {student_to_del['Name']}")
        st.write(f"**Department:** {student_to_del['Department']}")
        st.write(f"**Attendance:** {student_to_del['Attendance']}%")
        st.write(f"**Marks:** {student_to_del['Marks']}")

        st.warning(f"⚠️ Are you sure you want to delete **{del_name}**?")

        if st.button("🗑️ Yes, Delete", use_container_width=True):
            st.session_state.students = [
                s for s in st.session_state.students if s['Name'] != del_name
            ]
            save_data(st.session_state.students)  # 💾 save to file!
            st.success(f"✅ {del_name} deleted and saved permanently!")
            st.rerun()

# ══════════════════════════════════════════
# TAB 4 — DASHBOARD
# ══════════════════════════════════════════
with tab4:
    if len(st.session_state.students) == 0:
        st.info("📭 No students yet. Go to ➕ Add Student tab to add students!")
    else:
        df = pd.DataFrame(st.session_state.students)
        df['Status'] = df['Attendance'].apply(check_status)

        color_map = {
            'Active':      'green',
            'At Risk':     'orange',
            'Dropped Out': 'red'
        }

        total   = len(df)
        active  = len(df[df['Status'] == 'Active'])
        atrisk  = len(df[df['Status'] == 'At Risk'])
        dropped = len(df[df['Status'] == 'Dropped Out'])

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("👥 Total Students", total)
        c2.metric("✅ Active",          active)
        c3.metric("⚠️ At Risk",         atrisk)
        c4.metric("❌ Dropped Out",     dropped)

        st.markdown("---")

        st.subheader("📋 All Students")
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.markdown("---")

        st.subheader("📊 Status Breakdown")
        status_count = df['Status'].value_counts().reset_index()
        status_count.columns = ['Status', 'Count']
        fig1 = px.pie(status_count, names='Status', values='Count',
                      color='Status', color_discrete_map=color_map, hole=0.35)
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("---")

        st.subheader("📈 Attendance % of Each Student")
        fig2 = px.bar(df, x='Name', y='Attendance', color='Status',
                      color_discrete_map=color_map, text='Attendance')
        fig2.add_hline(y=75, line_dash="dash", line_color="red",
                       annotation_text="75% Minimum")
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("---")

        st.subheader("📝 Marks of Each Student")
        fig3 = px.bar(df, x='Name', y='Marks', color='Status',
                      color_discrete_map=color_map, text='Marks')
        fig3.add_hline(y=50, line_dash="dash", line_color="orange",
                       annotation_text="Pass Mark: 50")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("---")

        st.subheader("⚠️ Students Who Need Attention")
        need_help = df[df['Status'] != 'Active']
        if len(need_help) == 0:
            st.success("🎉 All students are Active!")
        else:
            st.warning(f"{len(need_help)} student(s) need attention!")
            st.dataframe(need_help, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("🎓 AIDS 2nd Semester Project | Made with Streamlit")