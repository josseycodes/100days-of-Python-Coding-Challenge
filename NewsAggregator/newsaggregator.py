from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('news.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                source TEXT,
                category TEXT,
                content TEXT)''')
conn.commit()

# API endpoint to fetch news articles
@app.route('/get_articles', methods=['GET'])
def get_articles():
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    article_list = []
    for article in articles:
        article_dict = {
            'id': article[0],
            'title': article[1],
            'source': article[2],
            'category': article[3],
            'content': article[4]
        }
        article_list.append(article_dict)
    return jsonify(article_list)

# API endpoint to search for articles
@app.route('/search', methods=['GET'])
def search_articles():
    query = request.args.get('query')
    cursor.execute('SELECT * FROM articles WHERE title LIKE ?', ('%' + query + '%',))
    search_results = cursor.fetchall()
    return jsonify(search_results)

# API endpoint to bookmark git articles
@app.route('/bookmark/<int:article_id>', methods=['POST'])
def bookmark_article(article_id):
    # Implement logic to store bookmarked articles
    return jsonify({'message': 'Article bookmarked successfully'})

# API endpoint to get personalized recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Implement logic to generate personalized recommendations
    recommendations = []  # Replace with actual recommendations
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
