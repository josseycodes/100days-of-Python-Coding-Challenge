from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage for URL mappings
url_mapping = {}
click_count = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    
    if long_url:
        # Generate a short URL
        short_url = generate_short_url(long_url)
        
        return render_template('shorten.html', long_url=long_url, short_url=short_url)
    else:
        return render_template('index.html', error='Please enter a valid URL.')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_mapping:
        # Increment click count
        click_count[short_url] = click_count.get(short_url, 0) + 1
        return redirect(url_mapping[short_url])
    else:
        return render_template('error.html', message='Short URL not found.')

@app.route('/stats/<short_url>')
def get_stats(short_url):
    if short_url in url_mapping:
        clicks = click_count.get(short_url, 0)
        return render_template('stats.html', short_url=short_url, clicks=clicks)
    else:
        return render_template('error.html', message='Short URL not found.')

def generate_short_url(long_url):
    # Simulating a simple hash function for generating short URLs
    short_url = hash(long_url) % (10**8)
    
    # Store the mapping in-memory
    url_mapping[str(short_url)] = long_url
    
    return short_url

if __name__ == '__main__':
    app.run(debug=True)
