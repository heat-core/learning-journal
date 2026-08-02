import unittest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from models import Base, Movie, User

class TestMovieRatingSystemModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    def test_create_movie(self):
        movie = Movie(title="Harry Potter and the Philosopher's Stone", release_year=2001)
        self.session.add(movie)
        self.session.commit()

        fetched_movie = self.session.execute(
            select(Movie).filter_by(title="Harry Potter and the Philosopher's Stone")).scalar_one()
        self.assertEqual(fetched_movie.release_year, 2001, "مدل Movie را به‌درستی پیاده‌سازی نکرده‌اید.")

    def test_create_user(self):
        user = User(name="Harry Potter", email="harry.potter@hogwarts.com")
        self.session.add(user)
        self.session.commit()

        fetched_user = self.session.query(User).filter_by(email="harry.potter@hogwarts.com").one()
        self.assertEqual(fetched_user.name, "Harry Potter", "مدل User را به‌درستی پیاده‌سازی نکرده‌اید.")



if __name__ == "__main__":
    unittest.main()
