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
    
    def is_int(value):
        try:
            int(value)
        except ValueError:
            return False
        else:
            return True

    if not is_int(principal):
        return 'エラー：元本には整数を指定してください。'
    
    if not is_int(period):
        return 'エラー：期間には整数を指定してください。'
    
    principal = int (principal)
    rate = float (rate)
    period = int (period)

    if principal < 0:
        return 'エラー：元本にマイナスの数字を設定しないでください。'
    
    if rate < 0:
        return 'エラー：複利にマイナスの数字を設定しないでください。'
    
    if period < 0:
        return 'エラー：期間にマイナスの数字を設定しないでください。'

    i = 1
    while period + 1 > i:
        principal = principal + principal * rate / 100
        i = i + 1

    return principal
