import service

print ('複利計算を始めましょう！ただし、複利が発生するのは1年ごととします！')
principal_user = input ('元本を教えてください：')
rate_user = input ('複利が何％か教えてください：')
period_user = input ('何年分の計算をしますか？：')

result = service.compound_interest(principal_user, rate_user, period_user)
