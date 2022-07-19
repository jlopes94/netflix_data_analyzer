import re
from classes import NetflixProfile
from file_input import view_rows, view_fields, sub_fields, sub_rows, prof_fields, prof_rows
import secrets

#  this is a placeholder for personal netflix data analytics

#  netflix profile names | i should probably assign IDs up here then loop and add class instances later
net_profiles = []  # list for parsing
accounts = {}  # dictionary with names and IDs

# add profile names to list
for i in prof_rows:
    net_profiles.append(i[0])

#  finish all class methods
#  TODO: change allshows to a return statement for displaying,
#   timewatched(total), timewatched(specific show),  most autoplayed, timewatched(all accounts)


# assigned random number ID to each account and assigns them in a dictionary for later use
for h in net_profiles:
    name_id = str(secrets.randbelow(100000000))
    name_id = NetflixProfile(str(h), name_id)
    accounts[str(name_id)] = accounts.get(str(name_id), h)
    NetflixProfile.allshows(name_id)

# show account dictionary setup for reference {ID: Name}
print(accounts)
