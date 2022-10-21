""" Converts abbreviated trigonomic equations to the all cosine and sine operands equivalent"""

# The quick character input will allow for users to punch in
# special characters to their calculator, as keywords for the
# trig functions (ie. cos, sin, csc) to make the program more  
# use friendly
quick_char_dict = {
    "a": "sin",
    "b": "cos", 
    "c": "tan",
    "d": "csc",
    "e": "sec",
    "f": "cot"
}

# Display how program works
text = """ Please input the trig equation with the trig functions
either abbreviated or translated through the quick character translation 
as seen below. Note however that when inputting the equation, please enter
the operands and operators in order, even if the logical equation would
be incorrect. Also if there are fractions in the equation, please put them around ()
"""
print(text)
for i in quick_char_dict.items():
    print(i)

# Get trig equation from user
trig_equation = input("\nEnter the Trig Equation: ")
trig_equation = trig_equation.lower().replace(" ", "")
trig_equation = trig_equation.replace("**", "^")

# Put equation into the split form to be translated from
equation = list()

# (Recursive function)
def split_down(equation: list, half: str) -> equation:
    #Split
    skip_until = 0
    for i, j in enumerate(half):
        if i < skip_until:
            continue
        elif j == "(":
            end = half.find(")")
            new_element = half[i + 1:end]
            new_element = new_element.partition("/")
            equation.append(list(new_element))
            skip_until = end
        elif j in ["*", "/", "+", "-"]:
            half = list(half.partition(j))
            break
    else:
        if half.find("(") != -1:
            return
        else:
            equation.append(half)
            return

    print(F"half[0]: {half[0]}\nhalf[1]:{half[1]}\nhalf[2]:{half[2]}")
    if half[0].find("(") == -1:
        equation.append(half[0])
    equation.append(half[1])
    
    split_down(equation, half[2])

# Function call
split_down(equation, trig_equation)


# Translation for any quick character transition
def quick_char_trans(equation):
    for i, j in enumerate(equation):
        if type(j) == list:
            quick_char_trans(j)
        elif j in quick_char_dict:
            equation[i] = quick_char_dict[j]

quick_char_trans(equation)
# Single Function Translations
trig_id = {
    #Sin 
    "csc": ["1", "/", "sin"],
    "sec": ["1", "/", "cos"],
    "cot": ["cos", "/", "sin"],
    "tan": ["sin", "/", "cos"],
    "csc^2": ["1", "/", "sin^2"],
    "sec^2": ["1", "/", "cos^2"],
    "tan^2": ["sin^2", "/", "cos^2"]
    
}

def translate(equation):
    for i, j in enumerate(equation):
        if type(j) == list:
            translate(j)
        elif j in trig_id.keys():
            equation[i] = trig_id[j]
            
translate(equation)
print(equation)
