# AI-Assisted Selenium Automation Framework PoC

## Objective

This project demonstrates a Proof of Concept (PoC) for AI-assisted test automation using:

- AI-generated manual test cases
- JSON-based locator mapping
- Selenium with Python
- Reusable helper framework
- Screenshot capture
- Word execution reporting

The goal is to reduce repetitive automation scripting effort and improve maintainability using reusable automation assets.

---

# Framework Architecture

AI_Automation_POC/
│
├── drivers/
│   └── chromedriver.exe
│
├── helpers/
│   ├── locator_helper.py
│   ├── screenshot_helper.py
│   └── report_helper.py
│
├── locators/
│   └── locators.json
│
├── tests/
│   └── test_login_logout.py
│
├── test_cases/
│   └── SauceDemo_Login_Logout_TestCase.xlsx
│
├── screenshots/
│
├── reports/
│
├── requirements.txt
│
└── README.md

---

# Technologies Used

* Python
* Selenium WebDriver
* PyTest
* python-docx
* JSON locator mapping

---

# AI Usage in This PoC

## AI-assisted activities:

* Manual test case generation
* Selenium Python script generation
* Reusable automation framework generation
* Locator abstraction design

## Human-assisted activities:

* Initial locator identification
* Framework setup
* Execution validation

---

# Features

* Reusable locator mapping
* Helper-based automation framework
* Screenshot capture after key actions
* Word execution report generation
* Structured framework design
* AI-friendly automation architecture

---

# Sample Flow Automated

SauceDemo Login and Logout Flow:

1. Launch application
2. Enter username
3. Enter password
4. Click login
5. Validate successful login
6. Open menu
7. Click logout
8. Validate logout

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Execution

Navigate to the tests folder:

```bash
cd tests
```

Run the automation script:

```bash
python test_login_logout.py
```

---

# Execution Output

After successful execution:

## Screenshots

Saved inside:

```text
screenshots/
```

## Word Execution Report

Saved inside:

```text
reports/
```

---

# Future Enhancements

* Dynamic test case execution
* AI-based locator generation
* Self-healing locators
* HTML reporting
* CI/CD integration
* PyTest framework integration
* Multi-browser execution

---

# Disclaimer

This project uses SauceDemo as a public demo application for learning and demonstration purposes only.

No confidential or proprietary application data is included.

---

# Author

Belinda Smith