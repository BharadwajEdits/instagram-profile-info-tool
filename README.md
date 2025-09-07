# Instagram Profile Info Tool

A simple Python tool to fetch **Instagram profile information** (username, full name, bio, followers, following, posts, profile picture, etc.).  
Supports **Windows, Linux, macOS, and Android (Termux)**.  

**By @TechBharadwaj**  
YouTube: [https://www.youtube.com/@TechBharadwaj](https://www.youtube.com/@TechBharadwaj)  
*Don't forget to subscribe! 🚀*

---

## 🚀 Why Login?

Instagram limits the data you can fetch from **public accounts** when you are not logged in.  

- **Without login:** it does't work If dont belive you can use a fake account, may hit rate limits.  
- **With login:** Access more reliable info and sometimes private account details (if you follow them).  
- **Important:** This tool does **not store your password**. It is used only temporarily for authentication with Instagram.  

---

## 📌 Prerequisites

- **Windows / Linux / macOS** → [Python 3.8+](https://www.python.org/downloads/)  
- **Android** → Install [Termux](https://f-droid.org/en/packages/com.termux/)  

---

## 🖥️ Installation & Use (Windows / Linux / macOS)

```bash
# 1. Clone the repo
git clone https://github.com/BharadwajEdits/instagram-profile-info-tool.git
cd instagram-profile-info-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the tool
python insta_tool.py
```

### Step 1: Login (Recommended)
When you run the tool, you will first be prompted to **login to Instagram**:

```
Enter your Instagram Username: yourusername
Enter your Instagram Password:
✅ Login successful!
```

### Step 2: Fetch Profile Info
Then, enter the **Instagram username you want to fetch info from**:

```
Enter Instagram Username to fetch info: instagram
```

---

## 📱 Installation & Use (Android / Termux)

```bash
# 1. Update Termux & install Python + Git
pkg update && pkg upgrade
pkg install python git -y

# 2. Clone repo
git clone https://github.com/BharadwajEdits/instagram-profile-info-tool.git
cd instagram-profile-info-tool

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the tool
python insta_tool.py
```

Follow the **login step** first, then enter the target Instagram username.

---

## ⚠️ Notes

- Works best with **public Instagram accounts**.  
- Private account info can only be fetched **if you follow them and login**.  
- If you see this error:

```
❌ Error: Could not fetch data. Maybe profile is private or Instagram blocked request.
```

→ Instagram may have **rate-limited** you. Wait a few minutes or login.  
- **No passwords are stored** by this tool.  
- **Do not tag personal IDs** in the repo or issues.  

---

## 📊 Example Output

```
--- Instagram Profile Info ---
Username: instagram
Full Name: Instagram
Bio: Discover what's new on Instagram 🔎✨
Followers: 694,405,312
Following: 233
Posts: 8,134
Profile Pic URL: https://instagram.fccj3-1.fna.fbcdn.net/v/t51.2885-19/281440578_1088265838702675_6233856337905829714_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.fccj3-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2QEVti5uXfCzQZYvPpzXPwKpMA-hG9WHeR1U8QV9n6Nh5XnOvPezE6JeW2YC33gBdqQ&_nc_ohc=fJowwsZqquoQ7kNvwGakcPi&_nc_gid=JUlv-KWOpAVcS3gnIQKp9g&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfYjR0ZpE5oAU9uHlmo6jkab5QRBWdr40JjOgOdxaz_uPg&oe=68C311D8&_nc_sid=8b3546
-------------------------------
```

---

Thank you for using this tool!  
**Subscribe to my YouTube channel:** [@TechBharadwaj](https://www.youtube.com/@TechBharadwaj) 🔔

