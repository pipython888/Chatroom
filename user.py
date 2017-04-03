import datetime


class User:
    def __init__(self, username, password, full_name='', email='', bio=''):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.bio = bio
        self.followers = set()
        self.following = set()
        self.time_joined = datetime.datetime.now().strftime("%B %d, %Y")

    def display_profile(self):
        """Displays a user's profile"""

        line = "=" * 40

        # Username
        print(self.username.center(40))
        print(line)

        # Full name and email
        if self.full_name:
            print(("Full name: %s" % self.full_name).center(40))

        if self.email:
            print(("Email: <%s>" % self.email).center(40))

        print(("Joined at: %s" % self.time_joined).center(40))

        print(line)

        # Bio
        if self.bio:
            bio_line = ""
            bio_lines = []
            for x in self.bio:
                bio_line += x
                if len(bio_line) == 30:
                    bio_lines.append(bio_line)
                    bio_line = ""
            del bio_line

            for bio_line in bio_lines:
                print(bio_line.center(40))

            del bio_lines
        else:
            print("No bio for this user".center(40))
        print(line)

        print()

        # Followers and Following
        print("Followers".center(40))
        print(line)
        for follower in self.followers:
            print(follower, end=" ")
        if self.followers:
            print()
        print(line)

        print()

        print("Following".center(40))
        print(line)
        for following in self.following:
            print(following, end=" ")
        if self.following:
            print()
        print(line)
