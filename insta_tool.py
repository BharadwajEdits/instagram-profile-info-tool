# Instagram Profile Info Tool
# By @TechBharadwaj YT : https://www.youtube.com/@TechBharadwaj

import instaloader
import getpass

BANNER = """
======================================
   Instagram Profile Info Tool
   By @TechBharadwaj YT
   https://www.youtube.com/@TechBharadwaj
======================================
"""

print(BANNER)

# Initialize Instaloader
L = instaloader.Instaloader()

# Login first (needed even for public accounts now)
your_user = input("Enter your Instagram Username: ")
your_pass = getpass.getpass("Enter your Instagram Password: ")

try:
    L.login(your_user, your_pass)
    print("✅ Login successful!\n")
except Exception as e:
    print("❌ Login failed:", e)
    exit()

# Ask for target username
target_user = input("Enter Instagram Username to fetch info: ")

try:
    profile = instaloader.Profile.from_username(L.context, target_user)

    print("\n--- Instagram Profile Info ---")
    print("Username:", profile.username)
    print("Full Name:", profile.full_name)
    print("Bio:", profile.biography)
    print("Followers:", profile.followers)
    print("Following:", profile.followees)
    print("Posts:", profile.mediacount)
    print("Profile Pic URL:", profile.profile_pic_url)
    print("-------------------------------")

except Exception as e:
    print("❌ Error:", e)
