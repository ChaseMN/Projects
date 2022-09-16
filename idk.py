# Is it good practice to put a space before you start your comments?
#^ as in there
while True: 
    var = 1
    p = float(input('Amount to invest - '))
    cur = float(input('Current Price - '))
    print('Price to Break Even: ' + str(cur*1.004))
    print('1% Drop: ' + str(cur/1.01))
    var = float(input('Enter target sell price or 0 to restart - '))
    while var != 0:
        print(   'Gains: ' + str((p/cur*var) - (p*0.004))   )
        var = float(input('Enter target sell price or 0 to restart - '))