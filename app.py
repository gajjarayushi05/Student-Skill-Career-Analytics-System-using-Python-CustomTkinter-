import customtkinter as ctk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# APP SETTINGS

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

FILE = "student_data.csv"

BG = "#F6F8FC"
WHITE = "#FFFFFF"
PRIMARY = "#6C63FF"
BLUE = "#5B8DEF"
GREEN = "#52B788"
ORANGE = "#F4A261"
TEXT = "#263238"
MUTED = "#78909C"
LIGHT_PURPLE = "#EEEAFE"
LIGHT_BLUE = "#EAF1FF"
LIGHT_GREEN = "#E8F7F0"
LIGHT_ORANGE = "#FFF2E5"


# DATA

SUBJECTS = [
    "DS", "DBMS", "CN", "Java",
    "Python", "OS", "Statistics"
]

SKILLS = [
    "Communication",
    "Problem_Solving",
    "Coding_Skill",
    "Aptitude",
    "Project_Skill"
]

COLUMNS = [
    "Student_ID", "Name", "Semester",
    "DS", "DBMS", "CN", "Java", "Python", "OS", "Statistics",
    "Communication", "Problem_Solving",
    "Coding_Skill", "Aptitude", "Project_Skill"
]

try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=COLUMNS)


# CALCULATIONS

def calculate_scores(student):

    academic = np.mean([
        float(student[x]) for x in SUBJECTS
    ])

    technical = np.mean([
        float(student[x])
        for x in ["DS", "DBMS", "CN", "Java", "Python", "OS"]
    ])

    skill_scores = [
        float(student[x]) * 10
        for x in SKILLS
    ]

    skill = np.mean(skill_scores)

    readiness = (
        academic * 0.45
        + technical * 0.25
        + skill * 0.30
    )

    return (
        round(academic, 2),
        round(technical, 2),
        round(skill, 2),
        round(readiness, 2)
    )


# CAREER RECOMMENDATION

def generate_recommendation(student):

    python = float(student["Python"])
    ds = float(student["DS"])
    dbms = float(student["DBMS"])
    java = float(student["Java"])
    statistics = float(student["Statistics"])
    coding = float(student["Coding_Skill"]) * 10
    problem = float(student["Problem_Solving"]) * 10
    communication = float(student["Communication"]) * 10
    cn = float(student["CN"])
    os = float(student["OS"])

    careers = []

    score = (
        python * 0.35
        + coding * 0.30
        + problem * 0.20
        + ds * 0.15
    )

    careers.append(("Python Developer", round(score, 1)))

    score = (
        python * 0.25
        + statistics * 0.30
        + dbms * 0.20
        + problem * 0.15
        + coding * 0.10
    )

    careers.append(("Data Analyst", round(score, 1)))

    score = (
        ds * 0.30
        + coding * 0.25
        + problem * 0.25
        + java * 0.10
        + python * 0.10
    )

    careers.append(("Software Developer", round(score, 1)))

    score = (
        java * 0.30
        + dbms * 0.25
        + ds * 0.15
        + coding * 0.20
        + os * 0.10
    )

    careers.append(("Java / Backend Developer", round(score, 1)))

    score = (
        cn * 0.35
        + os * 0.25
        + dbms * 0.15
        + problem * 0.15
        + communication * 0.10
    )

    careers.append(("Network / System Engineer", round(score, 1)))

    careers.sort(
        key=lambda x: x[1],
        reverse=True
    )

    improvements = []

    values = {
        "Data Structures": ds,
        "DBMS": dbms,
        "Computer Networks": cn,
        "Java": java,
        "Python": python,
        "Operating Systems": os,
        "Statistics": statistics,
        "Communication": communication,
        "Problem Solving": problem,
        "Coding Skill": coding
    }

    for name, value in values.items():
        if value < 70:
            improvements.append(name)

    learning = []

    if python < 80:
        learning.append("Advanced Python")

    if ds < 80:
        learning.append("DSA & Problem Solving")

    if dbms < 80:
        learning.append("SQL & Database")

    if coding < 80:
        learning.append("Coding Practice")

    if statistics < 80:
        learning.append("Statistics & Data Analysis")

    if not learning:
        learning.append("Advanced Projects & Mock Interviews")

    interview = [
        "Practice technical interview questions",
        "Solve DSA coding problems",
        "Prepare SQL and DBMS questions",
        "Prepare your project explanation",
        "Practice HR communication"
    ]

    return (
        careers,
        improvements,
        learning,
        interview
    )


# MAIN APPLICATION

class StudentAnalyzer(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            "Student Skill & Interview Readiness Analyzer"
        )

        self.geometry("1280x780")
        self.minsize(1150, 700)

        self.configure(
            fg_color=BG
        )

        self.editing_id = None

        self.create_sidebar()
        self.create_main()

        self.show_dashboard()


    # SIDEBAR

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=230,
            corner_radius=0,
            fg_color=WHITE
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        ctk.CTkLabel(
            self.sidebar,
            text="🎓",
            font=("Arial", 38)
        ).pack(
            pady=(35, 0)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Student\nAnalytics",
            font=("Arial", 22, "bold"),
            text_color=PRIMARY
        ).pack(
            pady=(5, 35)
        )

        self.nav_button(
            "🏠   Dashboard",
            self.show_dashboard
        )

        self.nav_button(
            "👤   Student Profile",
            self.show_profile
        )

        self.nav_button(
            "🎯   Career Analysis",
            self.show_career
        )

        self.nav_button(
            "📊   Performance",
            self.show_performance
        )

        self.nav_button(
            "📁   Student Records",
            self.show_records
        )

        ctk.CTkLabel(
            self.sidebar,
            text=""
        ).pack(
            expand=True
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Python for Data Science\nMini Project",
            font=("Arial", 11),
            text_color=MUTED
        ).pack(
            pady=25
        )


    def nav_button(self, text, command):

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            command=command,
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color=LIGHT_PURPLE,
            text_color=TEXT,
            anchor="w",
            font=("Arial", 13, "bold")
        )

        button.pack(
            fill="x",
            padx=15,
            pady=5
        )


    # MAIN

    def create_main(self):

        self.main = ctk.CTkFrame(
            self,
            fg_color=BG,
            corner_radius=0
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )


    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()


    def header(self, title, subtitle):

        frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=35,
            pady=(25, 10)
        )

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Arial", 28, "bold"),
            text_color=TEXT
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            frame,
            text=subtitle,
            font=("Arial", 13),
            text_color=MUTED
        ).pack(
            anchor="w",
            pady=(5, 0)
        )


    # DASHBOARD

    def show_dashboard(self):

        self.clear_main()

        self.header(
            "Welcome to Student Analytics 👋",
            "Academic performance, skills and career readiness in one place."
        )

        stats = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        stats.pack(
            fill="x",
            padx=30,
            pady=15
        )

        self.dashboard_card(
            stats,
            "👥",
            "TOTAL STUDENTS",
            str(len(df)),
            PRIMARY,
            LIGHT_PURPLE
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        avg = 0

        if not df.empty:

            readiness_values = []

            for _, student in df.iterrows():

                scores = calculate_scores(student)

                readiness_values.append(
                    scores[3]
                )

            avg = round(
                np.mean(readiness_values),
                1
            )

        self.dashboard_card(
            stats,
            "🎯",
            "AVG READINESS",
            f"{avg}%",
            BLUE,
            LIGHT_BLUE
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        self.dashboard_card(
            stats,
            "📚",
            "ACADEMIC SCALE",
            "/100",
            GREEN,
            LIGHT_GREEN
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        self.dashboard_card(
            stats,
            "💻",
            "SKILL SCALE",
            "/10",
            ORANGE,
            LIGHT_ORANGE
        ).pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        card = ctk.CTkFrame(
            self.main,
            fg_color=WHITE,
            corner_radius=18
        )

        card.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=15
        )

        ctk.CTkLabel(
            card,
            text="Student Skill & Interview Readiness Analyzer",
            font=("Arial", 22, "bold"),
            text_color=TEXT
        ).pack(
            pady=(30, 10)
        )

        ctk.CTkLabel(
            card,
            text=(
                "Analyze subject marks, technical skills and "
                "personal skills to generate a personalized "
                "career and interview preparation report."
            ),
            font=("Arial", 14),
            text_color=MUTED,
            wraplength=800,
            justify="center"
        ).pack(
            pady=10
        )

        features = [
            ("📚", "Subject Marks", "Out of 100"),
            ("💻", "Skills", "Out of 10"),
            ("📊", "Analytics", "Automatic"),
            ("🎯", "Career Match", "Personalized"),
            ("⚠️", "Skill Gaps", "Detected"),
            ("🎤", "Interview", "Preparation")
        ]

        feature_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        feature_frame.pack(
            pady=30
        )

        for i, (icon, title, sub) in enumerate(features):

            item = ctk.CTkFrame(
                feature_frame,
                width=230,
                height=90,
                fg_color="#F8FAFF",
                corner_radius=12
            )

            item.grid(
                row=i // 3,
                column=i % 3,
                padx=8,
                pady=8
            )

            item.pack_propagate(False)

            ctk.CTkLabel(
                item,
                text=icon,
                font=("Arial", 24)
            ).pack(
                side="left",
                padx=12
            )

            text_frame = ctk.CTkFrame(
                item,
                fg_color="transparent"
            )

            text_frame.pack(
                side="left"
            )

            ctk.CTkLabel(
                text_frame,
                text=title,
                font=("Arial", 12, "bold"),
                text_color=TEXT
            ).pack(
                anchor="w"
            )

            ctk.CTkLabel(
                text_frame,
                text=sub,
                font=("Arial", 10),
                text_color=MUTED
            ).pack(
                anchor="w"
            )


    def dashboard_card(
        self,
        parent,
        icon,
        title,
        value,
        color,
        bg_color
    ):

        card = ctk.CTkFrame(
            parent,
            height=120,
            fg_color=WHITE,
            corner_radius=15
        )

        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=icon,
            font=("Arial", 25),
            text_color=color
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 0)
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 10, "bold"),
            text_color=MUTED
        ).pack(
            anchor="w",
            padx=18
        )

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 22, "bold"),
            text_color=color
        ).pack(
            anchor="w",
            padx=18
        )

        return card


    # PROFILE

    def show_profile(self):

        self.clear_main()

        self.header(
            "Student Profile 👤",
            "Academic marks are out of 100 and skills are out of 10."
        )

        scroll = ctk.CTkScrollableFrame(
            self.main,
            fg_color=WHITE,
            corner_radius=18
        )

        scroll.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=15
        )

        self.entries = {}

        fields = [
            ("Student ID", "Student_ID", "Example: 101"),
            ("Student Name", "Name", "Enter name"),
            ("Semester", "Semester", "Example: 5")
        ]

        row = 0

        for label, key, placeholder in fields:

            self.create_input(
                scroll,
                label,
                key,
                placeholder,
                row
            )

            row += 1

        ctk.CTkLabel(
            scroll,
            text="📚  ACADEMIC SUBJECT MARKS",
            font=("Arial", 17, "bold"),
            text_color=PRIMARY
        ).grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="w",
            padx=30,
            pady=(25, 15)
        )

        row += 1

        subject_labels = {
            "DS": "Data Structures",
            "DBMS": "DBMS",
            "CN": "Computer Networks",
            "Java": "Java",
            "Python": "Python",
            "OS": "Operating Systems",
            "Statistics": "Statistics"
        }

        for key, label in subject_labels.items():

            self.create_input(
                scroll,
                f"{label}  (/100)",
                key,
                "Enter marks 0 - 100",
                row
            )

            row += 1

        ctk.CTkLabel(
            scroll,
            text="💻  SKILLS",
            font=("Arial", 17, "bold"),
            text_color=GREEN
        ).grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="w",
            padx=30,
            pady=(25, 15)
        )

        row += 1

        skill_labels = {
            "Communication": "Communication",
            "Problem_Solving": "Problem Solving",
            "Coding_Skill": "Coding Skill",
            "Aptitude": "Aptitude",
            "Project_Skill": "Project Skill"
        }

        for key, label in skill_labels.items():

            self.create_input(
                scroll,
                f"{label}  (/10)",
                key,
                "Enter score 0 - 10",
                row
            )

            row += 1

        self.profile_button = ctk.CTkButton(
            scroll,
            text="➕  ADD STUDENT",
            width=350,
            height=48,
            corner_radius=12,
            fg_color=PRIMARY,
            hover_color="#584FD6",
            font=("Arial", 13, "bold"),
            command=self.add_student
        )

        self.profile_button.grid(
            row=row,
            column=1,
            pady=30
        )


    def create_input(
        self,
        parent,
        label,
        key,
        placeholder,
        row
    ):

        ctk.CTkLabel(
            parent,
            text=label,
            font=("Arial", 12, "bold"),
            text_color=TEXT
        ).grid(
            row=row,
            column=0,
            sticky="w",
            padx=30,
            pady=7
        )

        entry = ctk.CTkEntry(
            parent,
            width=350,
            height=38,
            corner_radius=9,
            placeholder_text=placeholder,
            fg_color="#F8FAFC",
            border_color="#DDE3EC",
            text_color=TEXT
        )

        entry.grid(
            row=row,
            column=1,
            padx=30,
            pady=7
        )

        self.entries[key] = entry


    # ADD / UPDATE / DELETE

    def add_student(self):
        self.save_student(update=False)


    def save_student(self, update=False):

        global df

        try:

            values = {}

            for key, entry in self.entries.items():

                value = entry.get().strip()

                if value == "":
                    raise ValueError(
                        f"Please enter {key}"
                    )

                values[key] = value

            student_id = int(
                values["Student_ID"]
            )

            if update:

                if self.editing_id is None:
                    raise ValueError(
                        "Select a student to update."
                    )

                if (
                    student_id != self.editing_id
                    and student_id in df["Student_ID"].astype(int).values
                ):
                    raise ValueError(
                        "Student ID already exists."
                    )

            else:

                if student_id in df["Student_ID"].astype(int).values:

                    messagebox.showerror(
                        "Duplicate ID",
                        "Student ID already exists."
                    )

                    return

            new_student = {
                "Student_ID": student_id,
                "Name": values["Name"],
                "Semester": int(values["Semester"])
            }

            if (
                new_student["Semester"] < 1
                or new_student["Semester"] > 8
            ):
                raise ValueError(
                    "Semester must be between 1 and 8."
                )

            for subject in SUBJECTS:

                mark = float(
                    values[subject]
                )

                if mark < 0 or mark > 100:

                    raise ValueError(
                        f"{subject} must be between 0 and 100."
                    )

                new_student[subject] = mark

            for skill in SKILLS:

                score = float(
                    values[skill]
                )

                if score < 0 or score > 10:

                    raise ValueError(
                        f"{skill} must be between 0 and 10."
                    )

                new_student[skill] = score

            if update:

                index = df.index[
                    df["Student_ID"].astype(int)
                    == self.editing_id
                ][0]

                for key, value in new_student.items():
                    df.at[index, key] = value

                messagebox.showinfo(
                    "Success",
                    "Student updated successfully."
                )

            else:

                df = pd.concat(
                    [
                        df,
                        pd.DataFrame([new_student])
                    ],
                    ignore_index=True
                )

                messagebox.showinfo(
                    "Success",
                    "Student added successfully."
                )

            df.to_csv(
                FILE,
                index=False
            )

            self.editing_id = None

            self.show_records()

        except ValueError as error:

            messagebox.showerror(
                "Invalid Data",
                str(error)
            )


    def load_student_for_edit(self, student_id):

        result = df[
            df["Student_ID"].astype(int)
            == int(student_id)
        ]

        if result.empty:

            messagebox.showwarning(
                "Not Found",
                "Student not found."
            )

            return

        student = result.iloc[0]

        self.editing_id = int(
            student["Student_ID"]
        )

        self.show_profile()

        for key, entry in self.entries.items():

            entry.delete(
                0,
                "end"
            )

            entry.insert(
                0,
                str(student[key])
            )

        self.profile_button.configure(
            text="✏️  UPDATE STUDENT",
            command=lambda: self.save_student(
                update=True
            )
        )


    def delete_student(self, student_id):

        global df

        if messagebox.askyesno(
            "Delete Student",
            f"Delete student ID {student_id}?"
        ):

            df = df[
                df["Student_ID"].astype(int)
                != int(student_id)
            ].reset_index(drop=True)

            df.to_csv(
                FILE,
                index=False
            )

            messagebox.showinfo(
                "Success",
                "Student deleted successfully."
            )

            self.show_records()


    # CAREER ANALYSIS

    def show_career(self):

        self.clear_main()

        self.header(
            "Career & Interview Analysis 🎯",
            "Personalized recommendation based on academic marks and skills."
        )

        top = ctk.CTkFrame(
            self.main,
            fg_color=WHITE,
            corner_radius=15
        )

        top.pack(
            fill="x",
            padx=35,
            pady=15
        )

        ctk.CTkLabel(
            top,
            text="Student ID",
            font=("Arial", 13, "bold"),
            text_color=TEXT
        ).pack(
            side="left",
            padx=20,
            pady=20
        )

        self.career_id = ctk.CTkEntry(
            top,
            width=220,
            height=38,
            placeholder_text="Enter Student ID"
        )

        self.career_id.pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            top,
            text="ANALYZE PROFILE",
            width=190,
            height=40,
            corner_radius=10,
            fg_color=PRIMARY,
            command=self.analyze_career
        ).pack(
            side="left",
            padx=15
        )

        self.result_frame = ctk.CTkScrollableFrame(
            self.main,
            fg_color="transparent"
        )

        self.result_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=5
        )


    def analyze_career(self):

        try:

            sid = int(
                self.career_id.get()
            )

            result = df[
                df["Student_ID"].astype(int)
                == sid
            ]

            if result.empty:

                messagebox.showwarning(
                    "Not Found",
                    "Student not found."
                )

                return

            student = result.iloc[0]

            academic, technical, skill, readiness = \
                calculate_scores(student)

            careers, improvements, learning, interview = \
                generate_recommendation(student)

            for widget in self.result_frame.winfo_children():
                widget.destroy()

            scores = ctk.CTkFrame(
                self.result_frame,
                fg_color="transparent"
            )

            scores.pack(
                fill="x",
                pady=10
            )

            self.score_card(
                scores,
                "ACADEMIC",
                f"{academic}%",
                PRIMARY
            ).pack(
                side="left",
                fill="both",
                expand=True,
                padx=5
            )

            self.score_card(
                scores,
                "TECHNICAL",
                f"{technical}%",
                BLUE
            ).pack(
                side="left",
                fill="both",
                expand=True,
                padx=5
            )

            self.score_card(
                scores,
                "SKILLS",
                f"{skill}%",
                GREEN
            ).pack(
                side="left",
                fill="both",
                expand=True,
                padx=5
            )

            self.score_card(
                scores,
                "INTERVIEW READY",
                f"{readiness}%",
                ORANGE
            ).pack(
                side="left",
                fill="both",
                expand=True,
                padx=5
            )

            ctk.CTkLabel(
                self.result_frame,
                text=f"Personalized Report — {student['Name']}",
                font=("Arial", 22, "bold"),
                text_color=TEXT
            ).pack(
                anchor="w",
                pady=(20, 10)
            )

            career_box = self.section(
                "💼  RECOMMENDED CAREER AREAS"
            )

            career_box.pack(
                fill="x",
                pady=7
            )

            for career, match in careers[:3]:

                row = ctk.CTkFrame(
                    career_box,
                    fg_color="#F8FAFF",
                    corner_radius=10
                )

                row.pack(
                    fill="x",
                    padx=15,
                    pady=5
                )

                ctk.CTkLabel(
                    row,
                    text=career,
                    font=("Arial", 14, "bold"),
                    text_color=TEXT
                ).pack(
                    side="left",
                    padx=15,
                    pady=12
                )

                ctk.CTkLabel(
                    row,
                    text=f"{match}% Match",
                    font=("Arial", 14, "bold"),
                    text_color=PRIMARY
                ).pack(
                    side="right",
                    padx=15
                )

            gap_box = self.section(
                "⚠️  SKILLS TO IMPROVE"
            )

            gap_box.pack(
                fill="x",
                pady=7
            )

            gap_text = (
                "  •  ".join(improvements)
                if improvements
                else
                "No major skill gaps detected."
            )

            ctk.CTkLabel(
                gap_box,
                text=gap_text,
                font=("Arial", 12),
                text_color=MUTED,
                wraplength=850
            ).pack(
                anchor="w",
                padx=20,
                pady=15
            )

            learning_box = self.section(
                "📚  RECOMMENDED LEARNING"
            )

            learning_box.pack(
                fill="x",
                pady=7
            )

            for item in learning:

                ctk.CTkLabel(
                    learning_box,
                    text=f"→  {item}",
                    font=("Arial", 12),
                    text_color=TEXT
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=4
                )

            interview_box = self.section(
                "🎤  INTERVIEW PREPARATION"
            )

            interview_box.pack(
                fill="x",
                pady=7
            )

            for item in interview:

                ctk.CTkLabel(
                    interview_box,
                    text=f"→  {item}",
                    font=("Arial", 12),
                    text_color=TEXT
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=4
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid Student ID."
            )


    def score_card(
        self,
        parent,
        title,
        value,
        color
    ):

        card = ctk.CTkFrame(
            parent,
            height=105,
            fg_color=WHITE,
            corner_radius=13
        )

        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 10, "bold"),
            text_color=MUTED
        ).pack(
            pady=(15, 3)
        )

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 22, "bold"),
            text_color=color
        ).pack()

        return card


    def section(self, title):

        box = ctk.CTkFrame(
            self.result_frame,
            fg_color=WHITE,
            corner_radius=13
        )

        ctk.CTkLabel(
            box,
            text=title,
            font=("Arial", 15, "bold"),
            text_color=PRIMARY
        ).pack(
            anchor="w",
            padx=20,
            pady=12
        )

        return box


    # PERFORMANCE

    def show_performance(self):

        self.clear_main()

        self.header(
            "Performance Analytics 📊",
            "Visualize academic performance of students."
        )

        if df.empty:

            ctk.CTkLabel(
                self.main,
                text="No student data available.",
                font=("Arial", 18),
                text_color=MUTED
            ).pack(
                pady=100
            )

            return

        ctk.CTkButton(
            self.main,
            text="📊  OPEN PERFORMANCE GRAPH",
            width=280,
            height=45,
            corner_radius=10,
            fg_color=PRIMARY,
            command=self.open_graph
        ).pack(
            pady=40
        )

        ctk.CTkLabel(
            self.main,
            text="Academic subjects are evaluated out of 100.",
            font=("Arial", 13),
            text_color=MUTED
        ).pack()


    def open_graph(self):

        averages = []

        for _, student in df.iterrows():

            averages.append(
                np.mean([
                    float(student[s])
                    for s in SUBJECTS
                ])
            )

        plt.figure(
            figsize=(11, 6)
        )

        plt.bar(
            df["Name"],
            averages
        )

        plt.title(
            "Student Academic Performance"
        )

        plt.xlabel(
            "Students"
        )

        plt.ylabel(
            "Average Marks / 100"
        )

        plt.xticks(
            rotation=45
        )

        plt.ylim(
            0,
            100
        )

        plt.tight_layout()

        plt.show()


    # RECORDS

    def show_records(self):

        self.clear_main()

        self.header(
            "Student Records 📁",
            "View, update or delete saved student data."
        )

        frame = ctk.CTkFrame(
            self.main,
            fg_color=WHITE,
            corner_radius=15
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=15
        )

        action_frame = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        action_frame.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

        columns = [
            "Student_ID",
            "Name",
            "Semester",
            "DS",
            "DBMS",
            "CN",
            "Java",
            "Python",
            "OS",
            "Statistics"
        ]

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        style = ttk.Style()

        style.theme_use(
            "clam"
        )

        style.configure(
            "Treeview",
            background=WHITE,
            foreground=TEXT,
            fieldbackground=WHITE,
            rowheight=32,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            background=PRIMARY,
            foreground=WHITE,
            font=("Arial", 10, "bold")
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=100
            )

        for _, row in df.iterrows():

            tree.insert(
                "",
                "end",
                values=[
                    row[column]
                    for column in columns
                ]
            )

        tree.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        def selected_id():

            selected = tree.selection()

            if not selected:

                messagebox.showwarning(
                    "Select Student",
                    "Please select a student record first."
                )

                return None

            values = tree.item(
                selected[0],
                "values"
            )

            return int(values[0])

        ctk.CTkButton(
            action_frame,
            text="➕ ADD STUDENT",
            width=150,
            height=40,
            fg_color=PRIMARY,
            command=self.show_profile
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            action_frame,
            text="✏️ UPDATE",
            width=150,
            height=40,
            fg_color=BLUE,
            command=lambda: self.update_selected(
                selected_id()
            )
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            action_frame,
            text="🗑️ DELETE",
            width=150,
            height=40,
            fg_color="#D9534F",
            hover_color="#B8403D",
            command=lambda: self.delete_selected(
                selected_id()
            )
        ).pack(
            side="left",
            padx=5
        )


    def update_selected(self, student_id):

        if student_id is not None:
            self.load_student_for_edit(
                student_id
            )

    def delete_selected(self, student_id):

        if student_id is not None:
            self.delete_student(
                student_id
            )


# START

app = StudentAnalyzer()

app.mainloop()