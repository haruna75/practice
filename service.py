def compound_interest ( principal, rate, period ):

    if principal.isdigit() == False:
        print ('エラー：元本には数字を設定してください。')

    elif rate.isdigit() == False:
        print ('エラー：複利には数字を設定してください。')

    elif period.isdigit() == False:
        print ('エラー：期間には数字を設定してください。')

    else:
        i = 1
        principal = int (principal)
        rate = int (rate)
        period = int (period)
    
        while period + 1 > i:
            principal = principal + principal * rate / 100
            i = i + 1

        return principal
