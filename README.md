# Swag Labs Login Automation Test

This project is an end-to-end automated functional test for mimicking a **e-commerce platform login** on [saucedemo.com](https://www.saucedemo.com), using **Python, Selenium WebDriver, Behave (BDD), and Allure Reports**.

---

## 📂 Project Structure
login_auto_test/
│
├── features/
│   ├── login.feature
│   ├── steps/
│   │   └── login_steps.py
│   └── environment.py
│
├── reports/
│    ├── data_behaviors.csv
|    └── data_suites.csv
├── requirements.txt
└── README.md

---

## 🛠️ Prerequisites

- Python 3.8+
- Google Chrome browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version
- Git

---

## 📦 Installation Guide

1. **Clone the Repository**
   - choose a directory in which you want to clone the repository
   - enter the command in the terminal: git clone https://github.com/your-username/newspaper_login_test.git
   - once cloning is done, go to specific directory: login_auto_test

2. Create & Activate Virtual Environment
   - create virtual environment by running this command in the terminal: python -m venv .venv
   - activate virtual environment by running this command in the terminal: .venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Install Allure Command Line Tool
   - Windows command (install via Scoop): scoop install allure
   - or manually download from: https://github.com/allure-framework/allure2/releases
   - Once downloaded, verify installation by running this command in the terminal: allure --version

---

## 🧪 Running the Test
1. Run Behave with Allure Formatter in the terminal
   - behave -f allure_behave.formatter:AllureFormatter -o reports/ features/

2. Generate and View Allure Report
   - allure serve reports/

---

## 📌 Additional Notes: 
1. individual reports (JSON File) per scenario will be automatically saved under the "reports" directory.
2. data_behaviors.csv and data_suites.csv are manually downloaded from the Allure Visual Report and transferred in the "reports" directory.
