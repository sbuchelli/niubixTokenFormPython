from flask import Flask, request , redirect

__author__ = 'Sergio Buchelli <sbuchelli@hellozum.com>'
__source__ = ''

app = Flask(__name__)

@app.route('/getTokenForm',methods=['POST'])
def getTokenForm():
    purchaseNumber = request.args.get('purchase','')
    amount = request.args.get('amount','')
    zumToken = request.args.get('zumToken','')
    transactionToken = request.form['transactionToken']
    
    utm_source =  request.args.get('utm_source','')
    utm_medium =  request.args.get('utm_medium','')
    utm_campaign =  request.args.get('utm_campaign','')
    utm_content =  request.args.get('utm_content','')
    
    print("purchase ",purchaseNumber)
    print("amount ",amount)
    print("transactionToken ",transactionToken)
    
    url="https://<dominio a cambiar>/#/gracias/"+purchaseNumber+"/"+amount+"/"+transactionToken+"/"+zumToken+"?utm_source="+utm_source+"&utm_medium="+utm_medium+"&utm_campaign="+utm_campaign+"&utm_content="+utm_content
    print("url ",url)
    
    #print("response ",response)
    #response = jsonify()
    #response.status_code = 201
    #response.headers['location'] = url
    #response.autocorrect_location_header = False
    return redirect(url,code=302)

    
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=7000)
