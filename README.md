# 📬 Gmail Job Tracker

A Python script that connects to your Gmail account, searches for job application emails based on a subject line, and exports the results (date, sender, subject) to a CSV file.

---

## ✨ Features

- Authenticates using Gmail API (OAuth 2.0)
- Searches emails by **exact subject**
- Extracts `Date`, `From`, and `Subject`
- Exports results to `job_applications.csv`
- Simple to customize for other use cases

---

## 🛠 Requirements

- Python 3.7+
- Gmail account
- Google Cloud project with Gmail API enabled
- `credentials.json` file downloaded from Google Cloud Console

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/gmail-job-tracker.git
cd gmail-job-tracker
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. **Add your `credentials.json`** file from the [Google Cloud Console](https://console.cloud.google.com/).
2. **Run the script:**

```bash
python gmailreader.py
```

3. The script will:
   - Open a browser to authenticate your Google account
   - Fetch emails with a subject like `"job application"`
   - Save them to `job_applications.csv`

---

## 📂 Output Example

| Date       | From                        | Subject                         |
|------------|-----------------------------|----------------------------------|
| 2024-03-01 | recruiter@example.com       | Thank you for applying          |
| 2024-03-05 | hr@company.com              | Job Application Received        |

---

## 📝 Customization

To search for an **exact subject**, update this line in `gmailreader.py`:

```python
emails = search_emails(service, query='subject:"Your Exact Subject Here"')
```

---

## 🛡 Disclaimer

This script is for personal use only. If you're planning to share it, make sure you go through [Google's API Verification process](https://developers.google.com/identity/protocols/oauth2/verification) to avoid auth errors.

---

## 📄 License

MIT License
