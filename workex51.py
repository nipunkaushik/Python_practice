n = 1
average = 0
count = 0
newtotal = 0
total = None
while True:
    try:
        total = (raw_input("Enter a Number"))
        if total == 'done':
            break
        total = float(total)
    except:
        print "Invalid input"
        continue
    newtotal = total + total
    count = n
    average = newtotal / n
    n = n + 1
print newtotal, count, average
