def compound_interest ( principal, rate, period ):

    if principal.isdigit() == False:
        print ('エラーです')

    elif rate.isdigit() == False:
        print ('エラーです')

    elif period.isdigit() == False:
        print ('エラーです')

    else:
        i = 1
        principal = int (principal)
        rate = int (rate)
        period = int (period)
    
        while period + 1 > i:
            principal = principal + principal * rate / 100
            i = i + 1

        return principal
