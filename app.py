# app.py
from flask import request, jsonify
from app import create_app
from app.models import db, Episode, Guest, Appearance

app = create_app()


@app.route('/')
def index():
    return '<h1>Your API is running!</h1>'

@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return [
        {
            "id": e.id,
            "date": e.show_date,
            "number": e.id 
        } for e in episodes
    ]


@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)

    if not episode:
        return {"error": "Episode not found"}, 404

    return {
        "id": episode.id,
        "date": episode.show_date,
        "number": episode.id,
        "appearances": [
            {
                "id": appearance.id,
                "rating": appearance.rating,
                "episode_id": appearance.episode_id,
                "guest_id": appearance.guest_id,
                "guest": {
                    "id": appearance.guest.id,
                    "name": appearance.guest.name,
                    "occupation": appearance.guest.occupation
                }
            } for appearance in episode.appearances
        ]
    }



@app.route('/guests')
def get_guests():
    guests = Guest.query.all()
    return {
        "guests": [
            {
                "id": g.id,
                "name": g.name,
                "occupation": g.occupation
            } for g in guests
        ]
    }


@app.route('/appearances', methods=['POST'])
def add_appearance():
    data = request.get_json()

    try:
        rating = data['rating']
        episode_id = data['episode_id']
        guest_id = data['guest_id']

        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        if not episode or not guest:
            return jsonify({"errors": ["Episode or Guest not found"]}), 404

        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)

        db.session.add(appearance)
        db.session.commit()

        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": guest.id,
            "episode_id": episode.id,
            "episode": {
                "id": episode.id,
                "date": episode.show_date,
                "number": episode.id 
            },
            "guest": {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
        }), 201

    except KeyError:
        return jsonify({"errors": ["Missing required fields"]}), 400
    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400
    except Exception as e:
        return jsonify({"errors": ["Server error"]}), 500



if __name__ == '__main__':
    app.run(debug=True)