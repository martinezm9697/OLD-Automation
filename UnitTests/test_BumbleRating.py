from unittest import TestCase

from Bumble import BumbleRating as Brate
from Bumble.BumbleBio import BumbleBio


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up the session')
        sampleBio = BumbleBio(
            [],
            "name",
            "age",
            False,
            ["badge 1", "badge 2"],
            "height",
            "occupation",
            "school",
            "exercise",
            "education",
            "drinking",
            "smoking",
            "gender",
            "intentions",
            "family_plans",
            "star_sign",
            "politics",
            "religion",
            "about_me",
            ["section 1", "section 2"],
            ["location 1", "location 2"]
        )
        cls.sampleBio = sampleBio

        dealbreakerBio = BumbleBio(
            [],
            "Sarah",
            "21",
            False,
            ["badge 1", "badge 2"],
            "",
            "",
            "",
            "",
            "",
            "Often",
            "Often",
            "Trans",
            "",
            "",
            "",
            "Conservative",
            "",
            "add me. Ig: @sarahIG25874521",
            ["here for a good time not a long time", "never"],
            [""]
        )
        cls.dealbreakerBio = dealbreakerBio

        goodBio = BumbleBio(
            [],
            "Ashley",
            "30",
            True,
            ["badge 1", "badge 2"],
            "5' 2",
            "Artist",
            "Texas Tech",
            "Active",
            "Bachelors",
            "Socially",
            "never",
            "Female",
            "Casual",
            "Wants Kids",
            "Virgo",
            "Moderate",
            "Nonw",
            "Video games, anime, and cats",
            ["i like going t they gym", "i hate eating fast food"],
            ["Houston, TX", "California", "New York"]
        )
        cls.goodBio = goodBio

    def test_bio_has_dealbreaker(self):
        assert (Brate.bio_has_dealbreaker(self.sampleBio)).__eq__(False)
        assert (Brate.bio_has_dealbreaker(self.dealbreakerBio)).__eq__(True)

    def test_rate_bio(self):
        assert (Brate.sum_bio_ratings(self.goodBio) > 1)
        assert (Brate.sum_bio_ratings(self.dealbreakerBio).__eq__(0))
        assert (Brate.sum_bio_ratings(self.sampleBio) > 0)
