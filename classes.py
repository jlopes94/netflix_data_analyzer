from collections import Counter
from file_input import view_rows, view_fields, sub_fields, sub_rows, prof_fields, prof_rows


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
