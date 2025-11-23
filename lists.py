# acronyms = []
# print(acronyms)

# acronyms
# IDK -> I don't know
# LOL -> Laughing out loud
# TBH -> To be honest
# BRB -> Be right back
# G2G -> Got to go
# TTYL -> Talk to you later
# IDC -> I don't care
# OMG -> Oh my god
# SMH -> Shaking my hand
# JK -> Just kidding
# ASAP -> As soon as possible
# FYI -> For your information
# LMK -> Let me know
# TMI -> Too much information

acronyms = ['LOL','IDK','TBH']
print(acronyms)

acronyms.append('IMO')
acronyms.append('ASAP')
print(acronyms)

acronyms.remove('LOL')
print(acronyms)

# acronyms.remove('idk') # will throw error saying idk is not in the list as it is case-sensitive.
# print(acronyms)

# acronyms.clear() # removes all elements in the list.
# print(acronyms)


# check if a given acronym is present in the list of acronyms.
if 'IDK' in acronyms:
    print('IDK is present in acronyms')
else:
    print('IDK is not present in acronyms')


# loop through all acronyms in the list and print them
for acronym in acronyms:
    print(acronym)