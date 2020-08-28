from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pcsale.db'
app.secret_key = "fj2ofjaslfjsdalfjofjasfas"

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    search = dealSearch(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()
    if not results:
        flash('Nothing found')
        return redirect('/')
    else:
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/dealsDB')
def live_update():
    with open('top_bapcs_subreddit_posts.csv') as file:
        reader = csv.DictReader(file)
        items = []
        total = {'title': 'score':, 'id': , 'subreddit': , 'url': , 'num_counts':, 'created':}
        for row in reader:
            items.append(dict(row))
            total['title'] = row['title']
            total['score'] += int(row['score'])
            total['subreddit'] += int(row['subreddit'])
            total['url'] += int(row['url'])
            total['url'] += int(row['num_counts'])
            total['url'] += int(row['created'])
    return render_template('index.html', items=items, total=total)

@app.route('/')
def home():
    return '<h1 align="center" style="margin-top:200px;">Home</h1>'

if __name__ == '__main__':
    app.run(host='5000')