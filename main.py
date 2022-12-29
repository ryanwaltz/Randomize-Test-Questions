import random  # the only module we need


with open("/Users/ryanwaltz/Desktop/Desktop - MacBook Pro (3)/Randomize_tests/file.txt", "r") as file:
    lines = file.readlines()
"""
    Open the input file which should be in ".txt" form
    MUST be formatted so that the questions go without breaks from 1. to whatever you want
    Ex.
    1. Question
    choice
    choice
    choice
    choice
    2. Question
    
    Must have periods after numbers – can be adjusted but might trigger some bugs if not
"""
interim_lines = []
complete_lines = []
list_of_choices = ["a.", "b.", "c.", "d.",
                   "A.", "B.", "C.", "D.",
                   "A)", "B)", "C)", "D)",
                   ]

list_of_choices_reformat = ["1.", "2.", "3.", "4."]

"""
These list of common answer choice formatting helps the program not accidentally format answer choices twice.
Any answer choices without them will have their own answer choice (a., etc) added on to them.
This is especially helpful since some formatting from Google Docs or Word documents doesn't carry over to text documents.
This allows the user to have their choices formatted automatically instead of going over them manually.
"""
escape = 0
j = "1"
for i in lines:  # reading through lines
    if j in i:  # finds the number (1. in the first case)
        complete_lines.append(interim_lines)  # adds the lines as one entry in the complete_lines list
        interim_lines = []  # resets the interim_lines list
        j = str(int(j)+1)  # advances to the next number
    interim_lines.append(i)  # adds line to the interim_lines list
complete_lines.append(interim_lines)  # this is for the last question as there is no terminating sequence for it.

complete_lines.pop(0)  # this deletes the first entry of the list, which would simply be a newline character
complete_lines_randomized = []  # initializes the random list
while True:
    random_number = random.randint(0, len(complete_lines)-1)  # random entry in list
    complete_lines_randomized.append(complete_lines[random_number])  # adds the random entry to a new list
    complete_lines.pop(random_number)  # deletes the first entry from the original list
    if len(complete_lines) == 0:  # makes sure the list isn't zero so it can't throw errors.
        break

for i in complete_lines_randomized:
    if "." in i[0]:  # this if statement finds the period in the first line which usually comes immediately after the number
        indexer = i[0][0:5].index(".")  # this finds the value of the index of the .
        i[0] = (i[0])[indexer:]  # this resets the line to not include the number. Since the questions are going to be
                                 # randomized, we need new numbers
    for j in i[1:]:  # the subsequent lines of code focus on reformatting answer choices that may not have a value (a., b., etc.)
        if len(j) > 1:  # make sure the line isn't just a newline character
            for k in list_of_choices:
                if k in j:  # make sure there isn't already answer formatting
                    escape = 1  # if there is, don't execute the other code
            for l in list_of_choices_reformat:
                if l in j:
                    escape = 3  # reformatting time
    print(escape)
    if escape != 1:  # so there's no answer choice formatting / we need to replace the formatting
        try:
            i[4]  # make sure we didn't screw up - make sure there are 4 lines
        except IndexError:
            pass
        else:  # add the answer choice formatting to each line
            i[1] = i[1].replace("   ", "")
            i[2] = i[2].replace("   ", "")
            i[3] = i[3].replace("   ", "")
            i[4] = i[4].replace("   ", "")

            i[1] = "a. " + i[1][escape:]
            i[2] = "b. " + i[2][escape:]
            i[3] = "c. " + i[3][escape:]
            i[4] = "d. " + i[4][escape:]
            try:
                if len(i[5]) > 1:
                    i[5] = "e. " + i[5][escape:]  # sometimes (very rarely), there is a fifth choice
            except IndexError:
                pass

    escape = 0  # reset the value and get ready for the line.


"""
output assumes a file already exists to output to
"""

with open("/Users/ryanwaltz/Desktop/Desktop - MacBook Pro (3)/Randomize_tests/file_randomized.txt", "w") as file:
    for i in complete_lines_randomized:
        file.write(str(complete_lines_randomized.index(i)+1))  # write the number before each question
        for j in i:
            file.write(j)  # write the question and answer
