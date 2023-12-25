from unittest import TestCase

from Bumble.BumbleBio import BumbleBio
from Bumble import BumbleRating as Brate


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up the session')
        sampleBio = BumbleBio(
            [],
            "Amy",
            "55",
            False,
            ["badge 1", "badge 2"],
            "5' 7",
            "Artist",
            "",
            "Sometimes",
            "",
            "Never",
            "Never",
            "Woman",
            "Something Casual",
            "",
            "",
            "Moderate",
            "Christian",
            "",
            [""],
            ["Houston", "Singapore, NM", "Paris, Tx"]
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
            "Trans Woman",
            "",
            "",
            "",
            "Conservative",
            "",
            "add me. Ig: @sarahIG25874521",
            ["here for a good time not a long time", "never", "I am a trans woman"],
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
            "Industrial Engineer",
            "Texas Tech University",
            "Active",
            "Undergraduate",
            "Socially",
            "Never",
            "Woman",
            "",
            "",
            "",
            "Moderate",
            "Spiritual",
            "Video games, anime, and cats",
            ["I like going to the gym", "i hate eating fast food", "I like playing overwatch"],
            ["Houston", "LA, CA", "Mexico"]
        )
        cls.goodBio = goodBio

    def test_rate_bios_until_end(self):
        good_bio_rating = Brate.sum_bio_ratings(self.goodBio)
        dealbreaker_bio_rating = Brate.sum_bio_ratings(self.dealbreakerBio)
        sample_bio_rating = Brate.sum_bio_ratings(self.sampleBio)

        print("good bio rating: " + str(good_bio_rating))
        print("dealbreaker bio rating: " + str(dealbreaker_bio_rating))
        print("sample bio rating: " + str(sample_bio_rating))

        assert (good_bio_rating == 14)
        assert (dealbreaker_bio_rating < 5)
