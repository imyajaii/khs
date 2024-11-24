import instaloader

KHS_ACCOUNT = "hs_kim_95"

# Create instaloader
inst = instaloader.Instaloader()

# Load profile
profile_name = KHS_ACCOUNT
profile = instaloader.Profile.from_username(inst.context,profile_name)

# Print profile information
print(f"Username: {profile.username}")
print(f"Followers: {profile.followers}")
print(f"Followees: {profile.followees}")
print(f"Post-count: {profile.mediacount}")

for post in profile.get_post():
    print(f"post: {post.caption}, like: {post.likes}, comments: {post.comments}")