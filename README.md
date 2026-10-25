# 🛡️ Python Cyber Security Toolkit: Password Strength & Hash Generator

A lightweight, command-line utility built in Python designed to evaluate password security against industry-standard criteria and securely generate cryptographic hashes. 

Created as part of an ongoing portfolio focused on foundational cybersecurity and automation.

---

## 🚀 Features

* **Comprehensive Strength Evaluation:** Checks passwords against robust security metrics:
  * Minimum length enforcement (12+ characters)
  * Presence of uppercase (`A-Z`) and lowercase (`a-z`) letters
  * Inclusion of numerical digits (`0-9`)
  * Inclusion of special characters / punctuation (`!@#$%^&*...`)
* **Actionable Feedback:** Aggregates all missing security requirements into a clean checklist rather than stopping at the first error.
* **Cryptographic Hashing:** Automatically generates a secure **SHA-256** cryptographic hash for strong passwords using Python's built-in `hashlib` module.
* **Interactive Loop:** Allows users to test multiple passwords continuously in a single session.

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.x
* **Built-in Modules Used:** 
  * `string` (for character set constants)
  * `hashlib` (for secure hashing operations)

No external third-party package installations (`pip install`) are required!

---

## ⚙️ How to Run

1. Clone or download this repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
2. Navigate into project directory
   cd Python-Password-Strength-checker-and-hasher

3.Run the script using python3
  python3 passwordstrengthchecker.py

## ⚖️ Ethical Disclaimer
This tool is created strictly for educational purposes, personal security auditing, and portfolio development.

## 💡 Example Usage

```text
Enter your password: MySecurePassword123!
Password is strong
Your password has been hashed using SHA-256: 3c242030d970f03229b8637651a51130d226a31c518a24c2c5462cf1b17a1f5a
Do you want to check another password? (y/n): n
Exiting the program.
