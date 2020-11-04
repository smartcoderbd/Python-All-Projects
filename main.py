import nltk
from newspaper import Article
url="https://www.thedailystar.net/country/news/flight-saudi-arabia-few-hours-still-waiting-covid-19-certificate-1967405"
article = Article(url)
article.download()
article.parse()
nltk.download("punkt")
article.nlp()
print(article.authors)
print(article.publish_date)
print(article.top_image)
print(article.summary)

