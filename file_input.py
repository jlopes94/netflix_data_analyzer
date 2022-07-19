import csv

# handles the files downloaded from netflix and makes them into readable data

#
# SUBSCRIPTION HISTORY ####################################
sub_fields = []
sub_rows = []

with open("./user_data/SubscriptionHistory.csv", 'r', encoding='UTF-8') as csvfile:
    sub_csv = csv.reader(csvfile)
    # for getting next line
    sub_fields = next(sub_csv)

    # extracting each data row one by one
    for sub_row in sub_csv:
        sub_rows.append(sub_row)

# SUBSCRIPTION HISTORY ####################################
#
#
# PROFILE INFORMATION ####################################

prof_fields = []
prof_rows = []

with open("./user_data/Profiles.csv", 'r', encoding='UTF-8') as csvfile:
    prof_csv = csv.reader(csvfile)
    # for getting next line
    prof_fields = next(prof_csv)

    # extracting each data row one by one
    for prof_row in prof_csv:
        prof_rows.append(prof_row)


# PROFILE INFORMATION ####################################
#
#
# VIEWING ACTIVITY ####################################

view_fields = []
view_rows = []

with open("./user_data/ViewingActivity.csv", 'r', encoding='UTF-8') as csvfile:
    view_csv = csv.reader(csvfile)
    # for getting next line
    view_fields = next(view_csv)

    # extracting each data row one by one
    for view_row in view_csv:
        view_rows.append(view_row)

# VIEWING ACTIVITY ####################################
#
