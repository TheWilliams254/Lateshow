from app import create_app
from app.models import db, Episode, Guest, Appearance
import random

app = create_app()

with app.app_context():
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()
    db.session.commit()

    print("Cleared existing data")

    data = [
        (1999, "actor", "1/11/99", "Acting", "Michael J. Fox"),
        (1999, "Comedian", "1/12/99", "Comedy", "Sandra Bernhard"),
        (1999, "television actress", "1/13/99", "Acting", "Tracey Ullman"),
        (1999, "film actress", "1/14/99", "Acting", "Gillian Anderson"),
        (1999, "actor", "1/18/99", "Acting", "David Alan Grier"),
        (1999, "actor", "1/19/99", "Acting", "William Baldwin"),
        (1999, "Singer-lyricist", "1/20/99", "Musician", "Michael Stipe"),
        (1999, "model", "1/21/99", "Media", "Carmen Electra"),
        (1999, "actor", "1/25/99", "Acting", "Matthew Lillard"),
        (1999, "stand-up comedian", "1/26/99", "Comedy", "David Cross"),
        (1999, "actress", "1/27/99", "Acting", "Yasmine Bleeth"),
        (1999, "actor", "1/28/99", "Acting", "D. L. Hughley"),
        (1999, "television actress", "10/18/99", "Acting", "Rebecca Gayheart"),
        (1999, "Comedian", "10/19/99", "Comedy", "Steven Wright"),
        (1999, "actress", "10/20/99", "Acting", "Amy Brenneman"),
        (1999, "actress", "10/21/99", "Acting", "Melissa Gilbert"),
        (1999, "actress", "10/25/99", "Acting", "Cathy Moriarty"),
        (1999, "comedian", "10/26/99", "Comedy", "Louie Anderson"),
        (1999, "actress", "10/27/99", "Acting", "Sarah Michelle Gellar"),
        (1999, "Singer-songwriter", "10/28/99", "Musician", "Melanie C"),
        (1999, "actor", "10/4/99", "Acting", "Greg Proops"),
        (1999, "television personality", "10/5/99", "Media", "Maury Povich"),
        (1999, "actress", "10/6/99", "Acting", "Brooke Shields"),
        (1999, "Comic", "10/7/99", "Comedy", "Molly Shannon"),
        (1999, "actor", "11/1/99", "Acting", "Chris O'Donnell"),
        (1999, "actress", "11/15/99", "Acting", "Christina Ricci"),
        (1999, "Singer-songwriter", "11/16/99", "Musician", "Tori Amos"),
        (1999, "actress", "11/17/99", "Acting", "Yasmine Bleeth"),
        (1999, "comedian", "11/18/99", "Comedy", "Bill Maher"),
        (1999, "actress", "11/2/99", "Acting", "Jennifer Love Hewitt"),
        (1999, "rock band", "11/29/99", "Musician", "Goo Goo Dolls"),
        (1999, "musician", "11/3/99", "Musician", "Dave Grohl"),
        (1999, "Film actor", "11/30/99", "Acting", "Stephen Rea"),
        (1999, "Model", "11/4/99", "Media", "Roshumba Williams"),
        (1999, "television actress", "11/8/99", "Acting", "Kellie Martin"),
        (1999, "actress", "11/9/99", "Acting", "Kathy Griffin"),
        (1999, "actress", "12/1/99", "Acting", "Laura San Giacomo"),
        (1999, "journalist", "12/13/99", "Media", "Joan Lunden"),
        (1999, "actress", "12/14/99", "Acting", "Shannen Doherty"),
        (1999, "comedian", "12/16/99", "Comedy", "George Carlin"),
        (1999, "actor", "12/2/99", "Acting", "Michael Boatman"),
        (1999, "actor", "12/20/99", "Acting", "David Boreanaz"),
        (1999, "singer-songwriter", "12/21/99", "Musician", "Jewel"),
        (1999, "actor", "12/6/99", "Acting", "Paul Rudd"),
        (1999, "us senator", "12/7/99", "Politician", "Senator Bob Dole"),
        (1999, "actor", "12/9/99", "Acting", "Rob Schneider"),
        (1999, "comedian", "2/1/99", "Comedy", "George Carlin"),
        (1999, "actress", "2/10/99", "Acting", "Pamela Anderson, Natalie Raitano, Molly Culver"),
        (1999, "film actor", "2/11/99", "Acting", "Daniel Stern"),
    ]

    guest_cache = {}
    episode_id = 1
    guest_id = 1

    for year, occupation, show_date, group, guest_names in data:
        if guest_names == "NA":
            continue

        episode = Episode(id=episode_id, show_date=show_date, year=year, group=group)
        db.session.add(episode)
        db.session.commit()

        for name in [n.strip() for n in guest_names.split(",")]:
            if name not in guest_cache:
                guest = Guest(id=guest_id, name=name, occupation=occupation)
                db.session.add(guest)
                db.session.commit()
                guest_cache[name] = guest
                guest_id += 1
            else:
                guest = guest_cache[name]

            appearance = Appearance(rating=random.randint(3, 5), guest_id=guest.id, episode_id=episode.id)
            db.session.add(appearance)

        db.session.commit()
        episode_id += 1

    print("Sample seed completed successfully!")
