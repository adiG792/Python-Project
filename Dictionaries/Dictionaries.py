# a special structure to store key value pairs
monthConversions = {
    0: "January",
    1: "February",
    "Mar": "March",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid key"))  # if key is not matched we can give a default value
