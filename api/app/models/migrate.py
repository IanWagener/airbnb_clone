# This script creates all tables from each model defined before: User, State, City, Place, PlaceBook, Amenity, PlaceAmenities

from base import database
from user import User
from state import State
from city import City
from place import Place
from place_book import PlaceBook
from amenity import Amenity
from place_amenity import PlaceAmenities

database.connect()

database.create_tables([User, State, City, Place, PlaceBook, Amenity, PlaceAmenities], safe=True)

test_record=User(email='foo', password='bar', first_name='foo',last_name='bar')
test_record.save()
