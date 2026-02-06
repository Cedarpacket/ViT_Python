# ITP Week 1 Day 3 Exercise

usStates = ["Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"
]

# print the LENgth of us_states
print(len(usStates))
# print the comparison boolean of the LENgth of us_states to 50
print(len(usStates) == 50) # print(bool(len(usStates) == 50)) could have worked but its redundant
# create a variable my_state_index and assign the index value of the state you currently reside in
myStateIndex = usStates.index("California")
# print us_state with my_state_index to ACCESS your state!
print(usStates[myStateIndex])