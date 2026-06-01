# Functions
# Functions with Inputs
# fucntions with outputs

# def format_name(fname, lname):
#    formated_fname = fname.title()
#    formated_lname = lname.title()

#    return (f"{formated_fname} {formated_lname}")  

# print(format_name("michael", "jackson"))


# Multiple return values

def format_name(fname, lname):
    # Quick guard clause: check if either string is empty or just spaces
    if fname.strip() == "" or lname.strip() == "":
        return "You didn't provide valid inputs."
   
    formated_fname = fname.title()
    formated_lname = lname.title()

    return f"Result: {formated_fname} {formated_lname}"

# 1. Collect the inputs first
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")

# # 2. Pass the saved variables into the function and print
# output = format_name(first_name, last_name)
# print(output)