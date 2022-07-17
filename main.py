import re
from collections import Counter
from file_input import view_rows, view_fields, sub_fields, sub_rows, prof_fields, prof_rows
import secrets

#  this is a placeholder for personal netflix data analytics

#  netflix profile names | i should probably assign IDs up here then loop and add class instances later
net_profiles = []  # list for parsing
accounts = {}  # dictionary with names and IDs

# add profile names to list
for i in prof_rows:
    net_profiles.append(i[0])

#  move class to a new file when done with all methods
#  TODO: change allshows to a return statement for displaying,
#   timewatched(total), timewatched(specific show),  most autoplayed, timewatched(all accounts)
class NetflixProfile:

    def __init__(self, prof_name, id):
        self.id = id
        self.shows_watched = {}  # dictionary for all shows and number of episodes
        self.name = prof_name
        print(self.name, "ID:", self.id)
        #  loops through view activity and gets all shows
        for show in view_rows:
            temp_string = show[4]
            # for cleaning the input to only show the show's name and not the season or episode
            if show[0] == prof_name:
                atpos = temp_string.find("Epi")
                if atpos > 0:
                    temp_string = temp_string[:atpos - 2]
                atpos = temp_string.find("Season")
                if atpos > 0:
                    temp_string = temp_string[:atpos - 2]
                temp_string = temp_string.split(':')  # so many shows have colons in their season formatting...  why?
                # appends shows to an object's dictionary
                self.shows_watched[temp_string[0]] = self.shows_watched.get(temp_string[0], 0) + 1

    def __str__(self):
        return self.id

    # add number input in the future for most_common
    def allshows(self):
        k = Counter(self.shows_watched)
        high = k.most_common(5)

        # change this to a return statement for displaying
        for i in high:
            print(i[0], " :", i[1], " ")
        print("\n")

    def timewatched(self, show):
        # uses input to find a show and return the amount of time watched
        if show in self.shows_watched:
            print()


# assigned random number ID to each account and assigns them in a dictionary for later use
for h in net_profiles:
    name_id = str(secrets.randbelow(100000000))
    name_id = NetflixProfile(str(h), name_id)
    accounts[str(name_id)] = accounts.get(str(name_id), h)
    NetflixProfile.allshows(name_id)

# show account dictionary setup for reference {ID: Name}
print(accounts)
