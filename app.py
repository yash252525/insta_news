from flask import Flask,render_template,request
import requests
from config import NEWS_API_KEY
app= Flask(__name__)


#homepage
@app.route("/")
def index():
    query=request.args.get("query","latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles',[])
    filetered_articles = [article for article in articles if "Yahoo" not in article["source"]["name"] and 'removed' not in article["title"].lower()]

    return render_template('index.html', articles=filetered_articles,query=query)
    




if __name__ in "__main__":
    app.run(debug=True)





