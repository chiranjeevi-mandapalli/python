# str.format(*args) it can take n number of parameters
# f string literal to do format
# {position:format_specification}
# types of format specification:
# 1) alignment
#         right >
#         left <
#         center ^
# 2) presntation
#         .f --> fixed point notation
#         .e--> exponent notation
import math

# compared to format ,f"" is faster
a,b,c = 10,20,30
s ="{} {} {}".format(a,b,c) # by default each place holder takes the values 0, 1 2 if we want can chnages the place holder place
print(s)
s ="{2} {0} {1}".format(a,b,c) #  chamging the place holder places explictly
print(s)
s ="{2:>5} {0:>4} {1:>3}".format(a,b,c) #  in the place holders we can specify the specification also
# he i have specified to align to right by 5 places so white spaces will be there
print(s)
s ="{2:$>5} {0:*>4} {1:&>3}".format(a,b,c) # in this case i have spacified whats need to be filled in the white space
print(s)

s ="{2:$<5} {0:*<4} {1:&<3}".format(a,b,c)
print(s)

s ="{2:$^5} {0:*^4} {1:&^3}".format(a,b,c)
print(s)

s ="{:.4f}".format(math.pi) # here im specifing the precision up to 4 decimals
print(s)
s ="{:.4f}".format(math.pi) # here im specifing the precision up to 4 decimals
print(s)

val = 57600000000000000000000
s = "{:e}".format(val)
print(s)

s = "{:.3e}".format(val) # here im specifying the precision
print(s)

# similarly we can use f"" to do the same
s = f"{a} {b}"
print(s)

s = f"{b} {a} {c}"
print(s)

s = f"{a:*>4} {b:*>4}"
print(s)


