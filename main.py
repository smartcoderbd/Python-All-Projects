import nltk
from newspaper import Article
url="put-your-article-link"
article = Article(url)
article.download()
article.parse()
nltk.download("punkt")
article.nlp()
print(article.authors)
print(article.publish_date)
print(article.top_image)
print(article.summary)

