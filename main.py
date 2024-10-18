import os
from groq import Groq
import requests
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True  # Enable debug mode

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

def fetch_articles(interests):
    url = f'https://newsapi.org/v2/everything?q={interests}&apiKey={NEWS_API_KEY}&pageSize=5&sortBy=relevancy'
    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        return articles
    except requests.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []

def summarize_article(article):
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following article in 12-15 sentences:\n\n{article['title']}\n\n{article['description']}"
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error summarizing article: {e}")
        return ""

def create_newsletter(articles):
    newsletter_content = ""
    for article in articles:
        title = article.get('title', '')
        url = article.get('url', '')
        summary = summarize_article(article)
        newsletter_content += f"Title: {title}\n\nSummary: {summary}\n\nRead more: {url}\n\n---\n\n"
    return newsletter_content

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_interests = request.form['interests']
        print(f"User interests: {user_interests}")
        articles = fetch_articles(user_interests)
        print(f"Number of articles fetched: {len(articles)}")
        if not articles:
            return render_template('index.html', newsletter="No relevant articles found.")
        newsletter = create_newsletter(articles)
        print(f"Generated newsletter: {newsletter[:100]}...")
        return render_template('index.html', newsletter=newsletter)
    return render_template('index.html', newsletter=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)