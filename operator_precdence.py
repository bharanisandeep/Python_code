# division and multiplication have higher precedense than plus and minus
# Operator precedence is executed in BODMAS rule
#Bracket, Order, Division Multiplication, Addition and Subtraction
#Here Division and mul have equal precedence and addition and sub having equal precednce.
# If the expression that mixes the operations then they are executed from left to write


a = 12
b = 3

print(a + b / 3 - 4 * 12) # -35
print(a + (b / 3) - (4 * 12)) ## so here also ans is -35 that means above code is executed in this manner where
# higher precedence is given to mul and div

