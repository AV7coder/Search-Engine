from flask import Flask,render_template, request
import wikipedia
from googlesearch import search
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def index():
    if  request.method == 'POST':
        mainResult = []
        search_text = request.form.get('user_search')
        result = wikipedia.summary(search_text, sentences=100)
        mainResult.append(result)
        for i in search(search_text, tld="co.in", num=1, stop=5, pause=1): 
            mainResult.append(i)   
        displayResult = {
            "1":mainResult[0],
            "2":mainResult[1],
            "3":mainResult[2],
            "4":mainResult[3],
            "5":mainResult[4],
            "6":mainResult[5]
        }
        return render_template("index.html",data=displayResult)
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)