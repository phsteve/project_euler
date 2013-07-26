# Find the difference between the sum of the squares of the first 100 natural
# numbers and the square of the sum

#(a + b + c)^2 - (a^2 + b^2 + c^2) = ab + ac + bc 
#==>
#(a + b + ... + z)^2 - (a^2 + b^2 + ... + z^2) = sum of the product of all pairs of nonequal numbers


total = 0
for i in range(1, 101):
    for j in range(1, 101):
        if i != j:
            total += i*j
print total

#answer = 25164150