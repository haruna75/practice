import utils

print ('複利計算を始めましょう！ただし、複利が発生するのは1年ごととします！')
principal_user = input ('元本を教えてください：')
rate_user = input ('複利が何％か教えてください：')
period_user = input ('何年分の計算をしますか？：')

print ( '元本が' + principal_user + 'で、複利が' + rate_user + '%の時の、' + period_user + '年後の額を計算しますね！')

result = utils.compound_interest(principal_user, rate_user, period_user)
print ('答えは' + str(result) + 'ですね！')
