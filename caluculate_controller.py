from flask import Flask, render_template, request
import caluculate_service

app = Flask(__name__)

@app.route('/caluculate')
def caluculate_query():
    principal_user = request.args.get('principal')
    rate_user = request.args.get('rate')
    period_user = request.args.get('period')

    result = caluculate_service.compound_interest(principal_user, rate_user, period_user)

    return render_template ('index.html', principal=principal_user, rate=rate_user, period=period_user, result=result)

if __name__ == '__main__':
    app.run(debug=True)
