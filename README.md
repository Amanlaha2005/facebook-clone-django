# Facebook Clone using Django 🧑‍💻📘

A mini Facebook-like social media web application built using **Django**.  
This project includes core social networking features such as posts, profiles, friend requests, notifications, and search.

---

## 🚀 Features

- 🔐 User Authentication (Login / Logout / Register)
- 🧑 User Profiles (Profile photo + bio)
- ✏️ Edit Profile
- 📝 Create Posts (Text + Image)
- ❤️ Like & 💬 Comment on Posts
- 🤝 Friend Request System (Send / Accept / Reject)
- 🔔 Notifications System
  - Unread badge
  - Mark as read
  - Delete notification
- 👥 Friends-only Feed
- 🔍 Search Users
- ⏱️ Time-ago display (e.g., "5 minutes ago")

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default Django DB)  
- **Authentication:** Django Auth System  

---

## 📂 Project Structure

FaceBookClone/
│
├── FaceBookClone/ # Project settings
├── accounts/ # Authentication & Profiles
├── posts/ # Posts, likes, comments
├── templates/ # HTML templates
├── static/ # CSS files
├── media/ # Uploaded images (ignored in Git)
├── manage.py
└── requirements.txt



---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Amanlaha2005/facebook-clone-django.git
cd facebook-clone-django

2️⃣ Create virtual environment
python -m venv env
env\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver


Open browser:

http://127.0.0.1:8000/