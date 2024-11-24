import datetime
import instaloader

KHS_ACCOUNT = "hs_kim_95"


# Get current date
now = datetime.datetime.now()
format_now = now.strftime("%m/%d/%Y %H:%M:%S")

# Create instaloader
inst = instaloader.Instaloader()

# Load profile
profile_name = KHS_ACCOUNT
profile = instaloader.Profile.from_username(inst.context,profile_name)

# Print profile information
print(f"Current-datetime: {format_now}")
print(f"Username: {profile.username}")
print(f"Followers: {profile.followers}")
print(f"Followees: {profile.followees}")
print(f"Post-count: {profile.mediacount}")

for post in profile.get_post():
    print(f"post: {post.caption}, like: {post.likes}, comments: {post.comments}")