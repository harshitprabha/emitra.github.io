import smtplib
from flask import Flask,render_template,request
   
def mail(msg):
	val='emitrabot@gmail.com'
	key='Hjharwal@333'
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(val, key)
	s.sendmail(val,'cscnimera@gmail.com',msg)
	s.quit()
	print('done')

app = Flask(__name__)

@app.route('/send', methods =["GET", "POST"])
def send():
    if request.method == 'POST':
        n=request.form.get('name')
        e=request.form.get('email')
        s=request.form.get('subject')
        m=request.form.get('message')
        msg=str([n,e,s,m])
        mail(msg)
        return 'Request Submitted'
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pricing.html')
def p():
    return render_template('pricing.html')

@app.route('/contact.html')
def c():
    return render_template('contact.html')

@app.route('/Rscit.html')
def r():
    return render_template('Rscit.html')
    
if __name__ == '__main__' :
        app.run(debug=True)
