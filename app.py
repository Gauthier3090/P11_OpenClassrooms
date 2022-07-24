import json
from datetime import datetime


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


def sorted_competitions(comps):
    finished_competitions = []
    new_competitions = []
    for info in comps:
        info_date = datetime.strptime(info['date'], '%Y-%m-%d %H:%M:%S')
        if info_date < datetime.now():
            finished_competitions.append(info)
        else:
            new_competitions.append(info)

    return finished_competitions, new_competitions


def list_places_booked(competitions, clubs):
    places_booked = []
    for competition in competitions:
        for club in clubs:
            places_booked.append({'competition': competition['name'], 'booked': [0, club['name']]})
    return places_booked


def update_places(competition, club, places_booked, places_required):
    for item in places_booked:
        if item['competition'] == competition['name']:
            print(item)
            print(item['booked'][1], club['name'])
            print(item['booked'][0] + places_required <= 12)
            if item['booked'][1] == club['name']:
                if item['booked'][0] + places_required <= 12:
                    item['booked'][0] += places_required
                    break
                else:
                    raise ValueError("You can't book more than 12 places in a competition.")
    return places_booked
