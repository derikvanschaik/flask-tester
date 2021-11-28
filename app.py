from flask import Flask, request, render_template, url_for 
app = Flask(__name__)
# import functions from our 'in house' modules 
from parse_wiki import get_image_from_wiki
from api_calls import fetch_data, get_authors_and_quotes 

# routes 
@app.route("/", methods=['POST', 'GET'])    
def authors():
    authors, quotes = get_authors_and_quotes() 
    # return filtered authors by user search 
    if request.method == 'POST':
        user_search = request.form['author-search']
        filtered_authors = [author for author in authors if author.lower().startswith(user_search) ] 
        return render_template('authors.html',quotes=quotes,authors=filtered_authors)

    return render_template('authors.html', quotes=quotes,authors=authors)    

@app.route("/<author>")
def get_author(author=None): 
    print("calling author", author) 
    _, quotes = get_authors_and_quotes() 
    image_src = get_image_from_wiki(author)
    return render_template('author.html', quotes= quotes, author=author, image_src = image_src)  


if __name__ == '__main__': 
    app.run(debug=True)