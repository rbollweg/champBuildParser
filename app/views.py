__author__ = 'The Gibs'


from flask import render_template, flash, redirect
from app import app, models, parser, db
from .forms import SearchForm
import datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        flash("Parse requested for %s" % form.url_to_search)
        url_search = form.url_to_search._value()
        get_match = parser.spider(url_search)
        match = models.Match(url=get_match.match_url, date_play = datetime.datetime.now())
        db.session.add(match)
        for get_build in get_match.match_data:
            build = models.Build(champ_name = get_build.champName, match = match)
            db.session.add(build)
            for get_step in get_build.stepList:
                step = models.Step(time = get_step.time, build = build)
                db.session.add(step)
                for get_item in get_step.items:
                    item = models.Item(item = get_item.item_number, is_sold=get_item.is_sold, step=step)
                    db.session.add(item)
        db.session.commit()
        return redirect('/index')
    matches = models.Match.query.all()
    return render_template("index.html",
                           title='Home',
                           matches=matches,
                           form = form)

@app.route('/query/<game_id>')
def get_game(game_id):
    match = models.Match.query.get(game_id)
    return render_template("detail.html",
                           title='Match ' + game_id +' results',
                           match=match)

@app.route('/search', methods=['GET', 'POST'])
def search():

    return render_template('search.html',
                           title='Searching',
                           form=form)


