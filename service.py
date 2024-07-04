def compound_interest ( principal, rate, period ):

    def is_num(value):
        try:
            float(value)
        except ValueError:
            return False
        else:
            return True
        
    if not is_num(principal):
        return 'エラー：元本には数字を設定してください。'
    
    if not is_num(rate):
        return 'エラー：複利には数字を設定してください。'
    
    if not is_num(period):
        return 'エラー：期間には数字を設定してください。'

    else:
        i = 1
        principal = int (principal)
        rate = int (rate)
        period = int (period)
    
        while period + 1 > i:
            principal = principal + principal * rate / 100
            i = i + 1

        return principal
