"""Program that will expand trigonometric equations into the sine and cosine form
    By: Keith Hendricks"""


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

# Single Function Translations
trig_id = {
    #Sin 
    "csc": ["1", "/", "sin"],
    "sec": ["1", "/", "cos"],
    "cot": ["cos", "/", "sin"],
    "tan": ["sin", "/", "cos"],
    "csc^2": ["1", "/", "sin^2"],
    "sec^2": ["1", "/", "cos^2"],
    "cot^2": ["cos^2", "/", "sin^2"],
    "tan^2": ["sin^2", "/", "cos^2"]
    
}

def introduction():
    """Displays how this program will work and how the user
       should use it"""
    text = """ Please input the trig equation with the trig functions either abbreviated or translated through 
        the quick character translation 
        as seen below. Note however that when inputting the equation, please enter the operands and operators 
        in order, even if the logical equation would
        be incorrect. Also if there are fractions in the 
        equation, please put them around ()."""
    print(text)
    for i in quick_char_dict.items():
        print(i)


def get_user_trig_equation():
    """ Gets the trig equation from the user and formats the
    raw input"""
    trig_equation = input("\nEnter the Trig Equation: ")
    trig_equation = trig_equation.lower().strip()
    trig_equation = trig_equation.replace("**", "^")
    return trig_equation


def format_equation(equation):
    """Takes an equation and formats it into a list by adding new lines between operands and operators, then using the splitlines str method to partition all of it out into a list to be simplified from. Then isolates any parenthesis in the equation into sublists into the equation list"""
    i = 0
    j = len(equation)
    while i < j:
        if equation[i] in ["*", "/", "+", "-", "(", ")"]:
            equation = (
                equation[:i] +
                f"\n{equation[i]}\n" +
                equation[i+1:]
                )
            # Adds two to the len of equation, as \n was added twice
            j += 2
            # Moves i back to the current equation[i] so it does not do this operation on equation[i] again and get stuck in a forever loop
            i += 1
        # Check for smushed ending of parenthesis and nested parenthesis
                
        # Move to next element in equation
        i += 1

    equation = equation.splitlines(False)
    equation = list(filter(lambda x: x != '', equation))
    
    # Isolate parenthesis
    elements_stack = []
    end = 0
    i = 0
    j = len(equation)
    while i < j:
        #Check for new parenthesis
        if equation[i] == "(":
            # Pushes a tuple containing ([start], start_index) onto stack
            elements_stack.append(
                (list(), i)
                )
        # Check for ending element and if for subarray
        elif equation[i] == ")" and len(elements_stack) > 1:
            start = elements_stack[-1][1] - elements_stack[-2][1]
            end = i
            elements_stack[-2][0][start:end] = [elements_stack[-1][0]]
            elements_stack.pop()
        elif equation[i] == ")" and len(elements_stack) == 1:
            end = i + 1
            # Get the length of the condensed element
            parenthesis_len = len(equation[elements_stack[0][1]:end])
            equation[elements_stack[0][1]:end] = [elements_stack[0][0]]
            # After modifying the container that is being looped over, i is reupdated to the position of the current condensed list that was replaced over the ith term that the ( started at
            i -= parenthesis_len - 1
            j -= parenthesis_len - 1
            elements_stack.pop()

        # If active stack, then push element between the curr parenthesis onto the latest new element in stack
        elif elements_stack:
            elements_stack[-1][0].append(equation[i])
        else:
            pass
        # Move to next element
        i += 1
    return equation
            
          

def quick_char_trans(equation):
    """Translation for any quick character transition"""
    for i, j in enumerate(equation):
        if type(j) == list:
            quick_char_trans(j)
        elif j in quick_char_dict:
            equation[i] = quick_char_dict[j]
            

def translate(equation):
    for i, j in enumerate(equation):
        if type(j) == list:
            translate(j)
        elif j in trig_id.keys():
            equation[i] = trig_id[j]
            
            
def main():
    introduction()
    equation = get_user_trig_equation()
    equation = format_equation(equation)
    quick_char_trans(equation)
    translate(equation)
    equation = [str(i) for i in equation]
    final_equation = " ".join(equation)
    print(final_equation)


if __name__ == "__main__":
    main()



