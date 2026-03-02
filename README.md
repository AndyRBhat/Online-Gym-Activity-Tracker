# 🏋️‍♂️ Full-Stack Gym Tracker & Session Timer
**Technologies:** Python, Flask, SQLite, JavaScript (jQuery), AJAX

## 📝 Project Overview
This project is a web application designed to help exercisers track their workouts in real-time and save their progress. I developed this to solve the problem where workout data disappears once a browser is closed. I ensured that every exercise, whether it’s cycling or push-ups, is recorded into a permanent database.
---

## 🛠 Technical Skills & Tooling
Through this project, I learnt the following:

### **Back-End Development**
* **Python 3:** Used for server-side logic, data processing, and database communication.
* **Flask Framework:** Utilized to build a lightweight web server, manage URL routing, and handle HTTP requests (GET/POST).
* **RESTful Logic:** Structured the backend to handle different data modes (signup, login, add, show).

### **Database Architecture**
* **SQLite3:** Integrated a relational database to move from temporary memory to permanent data storage.
* **Relational Schema Design:** Engineered a database with multiple tables, using primary and foreign keys to link exercise logs to unique user accounts.
* **SQL Queries:** Wrote custom SQL statements for CRUD (Create, Read, Update, Delete) operations, including `INSERT` and filtered `SELECT` queries.


### **Front-End & Integration**
* **JavaScript & jQuery:** Developed client-side scripts to manage the UI state, timer logic, and real-time DOM updates.
* **AJAX (Asynchronous JavaScript):** Implemented API calls to allow for a flawless user experience, enabling database interaction without page refreshes.
* **Jinja2 Templating:** Used Flask's template engine to add server-side data and static assets (CSS/Audio/GIFs) into the HTML.

### **Development Workflow**
* **Version Control:** Managed the project lifecycle using **Git** and **GitHub Desktop**
* **Environment Management:** Utilized Python virtual environments (`venv`) to maintain clean dependencies.
* **VS Code Integration:** Configured a local development environment within Visual Studio, utilizing integrated terminals and debugging tools.

---

## 🚀 How to Run Locally
1. **Clone the repo:** `git clone [Your Repo Link]`
2. **Setup Virtual Env:** `python -m venv venv`
3. **Activate & Install:** * Windows: `.\venv\Scripts\activate`
   * Run: `pip install flask`
4. **Launch:** Run `python timer.py` and navigate to `http://127.0.0.1:5000`

---

🔮 Future Improvements
[ ] Encrypt/Dectrypt password and user ID: While I was troubleshooting I realized user ID and Password data is sent in plain text in GET. I will implement it when I learn about encryption

[ ] Data Analytics and visualization: By adding date to the database while inserting I would like to create a graph of daily activity time. Also recently in Science we learnt about Glycolysis. So I would like to add calories burned to specific exercise.


👨‍💻 Author
Andy(Aniruddha) R Bhat Aspiring Programmer & Robotics Engineer | Class of 2028