# 3 little pigletsaaa
# input 3 dig number_of_bricks report sum average and 
number_of_bricks = int(input("Enter three digits (each digit for one pig):"))
print ("with loop")
digits = [int(d) for d in str(number_of_bricks)]
print(digits)

print ("with division")
hundreds_digit = number_of_bricks // 100
tens_digit = (number_of_bricks % 100) // 10
ones_digit = number_of_bricks % 10
digits = [hundreds_digit, tens_digit, ones_digit]
print(digits)
print ("results :sum,per piglet, reminader , is it divide124d evenly ")
total = hundreds_digit + tens_digit + ones_digit
print ( total  , total // 3 , total % 3, not (total % 3))
