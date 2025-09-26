from flask import Blueprint
from datetime import datetime

from init import db
from models.user import User
from models.organiser import Organiser
from models.venue import Venue
from models.event import Event
from models.show import Show
from models.booking import Booking

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created.")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped.")

@db_commands.cli.command("seed")
# ========== Seed Users ==========
def seed_users_table():
    users = [User(
        first_name = "Bobby",
        last_name = "Mac Manus",
        email = "bobby@email.com",
        phone_number = "0424111222"
    ), User(
        first_name = "Susie",
        last_name = "Tinsdale",
        email = "susie@email.com",
        phone_number = "0232666777"
    ), User(
        first_name = "Josie",
        last_name = "Roberts",
        email = "josie@email.com",
        phone_number = "0232444333"
    ), User(
        first_name = "Lottie",
        last_name = "Timins",
        email = "lottie@email.com",
        phone_number = "0424555688"
    )]

    db.session.add_all(users)
    db.session.commit()

# ========== Seed Organisers ==========
def seed_organisers_table():
    organisers = [Organiser(
        full_name = "Johnnie Marks",
        email = "johnnie@email.com",
        phone_number = "0232333456"
    ), Organiser(
        full_name = "Georgia Pierce-allen",
        email = "georgia@email.com",
        phone_number = "08889765432"
    )]

    db.session.add_all(organisers)
    db.session.commit()

# ========== Seed Venues ==========
def seed_venues_table():
    venues = [Venue(
        name = "Rod Laver Arena",
        location = "200 Batman Ave, Melbourne VIC 3004"
    ), Venue(
        name = "Hordern Pavilion",
        location = "1 Driver Ave, Moore Park NSW 2021"
    )]

    db.session.add_all(venues)
    db.session.commit()

# ========== Seed Events ==========
def seed_events_table():
    events = [Event(
        title = "Linkin Park: From Zero World Tour",
        description = """The band will perform both new hits like “The Emptiness Machine” and “Heavy Is The Crown” alongside iconic anthems spanning their 20+ year career. Following the release of “Heavy Is The Crown”, the official League of Legends World Championship Anthem and their first collaboration with Riot Games, Linkin Park reasserted their position as one of rock’s defining voices. The song’s hard-hitting rhythm and anthemic energy embody the bold, renewed spirit of the band, resonating with fans across the globe and paving the way for From Zero.

Linkin Park made their triumphant return to the spotlight with "The Emptiness Machine," which surged to #1 on both the Billboard Alternative and Mainstream Rock Airplay charts, marking their 13th and 11th chart-toppers on these lists, respectively. The song also debuted at #4 on the UK Singles Chart, achieving the band’s highest UK chart position in their 24-year career.

With over 54 million monthly listeners on Spotify and accolades from Billboard, The New York Times, and The Los Angeles Times on their recent singles, Linkin Park’s comeback has proven they are more influential than ever. Their timeless appeal, and their latest music has struck a powerful chord, propelling them to the forefront of rock music once again.""",
        organiser_id = organisers[0].organiser_id
    ), Event(
        title = "Halsey: For My Last Trick",
        description = """Diamond-certified and GRAMMY®Award-nominated artist Halsey continues the celebration for the 10th anniversary of her triple platinum certified full-length debut album, BADLANDS, with the announcement of her Back to Badlands Tour

The new tour announce arrives on the heels of Halsey wrapping her “FOR MY LAST TRICK,” tour, which was the best selling tour of her career, with Variety branding the tour as “one of the most ambitious pop tours of the year.”

When BADLANDS was first released on August 28, 2015, it catapulted Halsey into music history. Since its release the album has sold over 3 Million albums-adjusted in the US, and has accumulated over 9 Billion on-demand streams worldwide. It is one of the only albums in music history to have every song, RIAA certified gold, platinum or multi-platinum. As well as multiple certifications in other countries including the UK, and Australia.""",
        organiser_id = organisers[1].organiser_id
    )]

    db.session.add_all(events)
    db.session.commit()

# ========== Seed Shows ==========
def seed_shows_table():
    shows = [Show(
        duration = 2.25,
        date_time = datetime.strptime("8-3-2026 7:00PM", "%d-%m-%Y %I:%M%p"),
        event_id = events[0].event_id,
        venue_id = venues[0].venue_id
    ), Show(
        duration = 2.25,
        date_time = datetime.strptime("9-3-2026 7:00PM", "%d-%m-%Y %I:%M%p"),
        event_id = events[0].event_id,
        venue_id = venues[0].venue_id
    ), Show(
        duration = 2.25,
        date_time = datetime.strptime("11-3-2026 7:00PM", "%d-%m-%Y %I:%M%p"),
        event_id = events[0].event_id,
        venue_id = venues[1].venue_id
    ), Show(
        duration = 2.5,
        date_time = datetime.strptime("13-2-2026 7:00PM", "%d-%m-%Y %I:%M%p"),
        event_id = events[1].event_id,
        venue_id = venues[1].venue_id
    ), Show(
        duration = 2.5,
        date_time = datetime.strptime("14-2-2026 7:00PM", "%d-%m-%Y %I:%M%p"),
        event_id = events[1].event_id,
        venue_id = venues[1].venue_id
    )]

    db.session.add_all(shows)
    db.session.commit()

# ========== Seed Bookings ==========
def seed_bookings_table():
    bookings = [Booking(), Booking(), Booking(), Booking()]

    db.session.add_all(bookings)
    db.session.commit()