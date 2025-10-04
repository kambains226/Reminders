📝 Task CLI with Firebase

A lightweight command-line task manager built in Python, designed to be used locally or remotely (via SSH).
It stores your to-dos in Firebase Firestore, so they sync automatically between your computer, phone, or any device running the CLI.

🚀 Features

Add, list, delete, and complete tasks directly from the terminal.

Colorful, clean CLI interface (using olorama).

Firebase Firestore integration for cloud storage & sync.

Can be accessed remotely with SSH + Tailscale.

🧩 How It Works

When you create a task, it’s stored both locally (in memory) and in Firebase Firestore.

Each task includes:

{
  "task": "Finish Firebase CLI",
  "done": false,
  "created_at": "2025-10-04T14:00:00",
  "due": "2025-10-04 21:30"
}

python main.py list
python main.py create "Buy groceries"
python main.py delete <task_name>
python main.py complete <task_name>
python main.py clear

⚙️ Setup
1️⃣ Clone the repo
git clone https://github.com/kambains226/Reminders.git
cd Reminders



2️⃣ Install Dependencies

pip install firebase-admin  colorama tabulate


🔑 Firebase Setup
1️⃣ Create a Firebase project

Go to Firebase Console -> Add Project
Enable Firestore Database 

2️⃣ Generate a Service Account Key

In your project:
Project Settings → Service Accounts → Generate New Private Key

Download the .json file and rename it (serviceAccount.json).

3️⃣ Add it to your project root
/project-folder
  ├── firebase.py
  ├── main.py
  ├── tasks.py
  ├── serviceAccount.json   ← 🔒 Your private key

  
