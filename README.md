# 🏦 Bank Management System  

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)  
[![Streamlit](https://img.shields.io/badge/streamlit-1.20%2B-ff4b4b.svg)](https://streamlit.io/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)  
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/Neeraj-Singh97/Bank-Management-system/issues)  

A simple **Bank Management System** built with **Python** (backend) and **Streamlit** (UI).  
This project provides basic account operations like creating, updating, deleting accounts, handling deposits/withdrawals, and maintaining transaction history.  

## 🚀 Features  

- ➕ Create new bank accounts (with Aadhaar & address)  
- 💰 Deposit and withdraw money (with transaction tracking)  
- 🔍 View account details and full transaction history  
- ✏️ Update account information (name, email, PIN)  
- ❌ Delete accounts securely  
- 📋 List all accounts (account no, holder name, PIN)  


## 🛠️ Installation & Setup  
-1.Installation Python 
-2.Need for Vscode
-3.All required minimum Package and library.

### 2. Create Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate   # On Windows
source myenv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r Requirements.txt
```

### 4. Run Application

```bash
streamlit run Bank-Management/app.py
```

## 📖 Usage

From the **main menu**, you can:

* **Create Account** → Generate a new account with details.
* **Deposit / Withdraw** → Manage balance with account no. & PIN.
* **Show Details** → View account profile & transactions.
* **Update Info** → Change name, email, or PIN.
* **Delete Account** → Remove account permanently.
* **List Accounts** → View all active accounts.


## 📂 Project Structure

```
Bank-Management-system/
│
├── Bank-Management/
│   ├── app.py        # Streamlit UI
│   ├── hello.py      # Backend logic
│   └── data.json     # Data storage (auto-generated)
│
├── Requirements.txt  # Dependencies
└── README.md         # Documentation
```

## ⚠️ Notes

* All data is stored in `data.json` locally.
* **Do not use real Aadhaar numbers or PINs** – only for demo.
* Use latest Streamlit version for best results.
**if i Need to Use to another database eaisly used to connect it**
  Database like:-SQL,MySQL,MngoDB,Excel.Etc


## 💡 Troubleshooting

* **Missing packages?**

  ```bash
  pip install -r Requirements.txt
  ```

* **File not found?** → Check your current working directory.

* **Streamlit errors?**

  ```bash
  pip install --upgrade streamlit
  ```

## ✨ Contributing

Contributions are welcome!

* Fork the repo
* Create a new branch
* Commit your changes
* Submit a Pull Request 🚀


## 📜 License

This project is licensed under the [MIT License](LICENSE).


👨‍💻 Author
Neeraj Singh
Software Engineer | Data Science & AI Enthusiast
📧 Email: [your-email@example.com]
🔗 GitHub: https://github.com/Neeraj-Singh97
💼 LinkedIn: https://www.linkedin.com/in/your-profile
📱+91 - 7505637648


