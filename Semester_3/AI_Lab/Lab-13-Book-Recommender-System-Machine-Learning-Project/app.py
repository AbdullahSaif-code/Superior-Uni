from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

popular = pickle.load(open('Models/popular.pkl','rb'))
piviot_table = pickle.load(open('Models/piviot_table.pkl','rb'))
books = pickle.load(open('Models/books.pkl','rb'))
similarity_scores = pickle.load(open('Models/similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular['Book-Title'].values),
                           author=list(popular['Book-Author'].values),
                           image=list(popular['Image-URL-M'].values),
                           votes=list(popular['num_ratings'].values),
                           rating=list(popular['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input', '').strip()
    # Try exact match first
    matches = piviot_table.index[piviot_table.index.str.lower() == user_input.lower()]
    if len(matches) == 0:
        # Try partial match
        matches = piviot_table.index[piviot_table.index.str.lower().str.contains(user_input.lower())]
    if len(matches) == 0:
        return render_template('recommend.html', data=[], error="No matching book found. Please try another title.")
    book_name = matches[0]
    index = np.where(piviot_table.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == piviot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data)

@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('q', '').lower()
    suggestions = []
    if query:
        # Use books DataFrame for partial matching
        matches = books[books['Book-Title'].str.lower().str.contains(query, na=False)]
        suggestions = matches['Book-Title'].drop_duplicates().head(10).tolist()
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)