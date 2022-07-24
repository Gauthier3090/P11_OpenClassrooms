from app import load_competitions, load_clubs, update_places, list_places_booked, sorted_competitions
from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()
old_competitions, new_competitions = sorted_competitions(competitions)
places_booked = list_places_booked(competitions, clubs)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show-summary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template(
            'welcome.html',
            club=club,
            old_competitions=old_competitions,
            new_competitions=new_competitions
        )
    except IndexError:
        if request.form['email'] == '':
            flash("Please enter your email.", 'error')
        else:
            flash("No account related to this email.", 'error')
        return render_template('index.html'), 401


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchase-places', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]

    try:
        places_required = int(request.form['places'])

        if places_required > int(competition['numberOfPlaces']):
            flash('Not enough places available.', 'error')

        elif places_required > int(club['points']):
            flash("You don't have enough points.", 'error')

        elif places_required > 12:
            print(places_required > 12)
            flash("You can't book more than 12 places in a competition.", 'error')

        else:
            try:
                update_places(competition, club, places_booked, places_required)
                competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
                club['points'] = int(club['points']) - (places_required * 3)
                flash('Great-booking complete!', 'success')
                print(old_competitions, new_competitions)
                return render_template(
                    'welcome.html',
                    club=club,
                    old_competitions=old_competitions,
                    new_competitions=new_competitions
                )

            except ValueError as error_message:
                flash(error_message.__str__(), 'error')

    except ValueError:
        flash('Please enter a number between 0 and 12.', 'error')

    return render_template('booking.html', club=club, competition=competition), 400


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
