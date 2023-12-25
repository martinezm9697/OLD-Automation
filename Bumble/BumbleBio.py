class BumbleBio:
    def __init__(self,
                 images,
                 name,
                 age,
                 photo_verified,
                 badges,
                 height,
                 occupation,
                 school,
                 exercise,
                 education,
                 drinking,
                 smoking,
                 gender,
                 intentions,
                 family_plans,
                 star_sign,
                 politics,
                 religion,
                 about_me,
                 sections,
                 locations):
        self.images = images
        self.name = name
        self.age = age
        self.photo_verified = photo_verified
        self.occupation = occupation
        self.school = school
        self.badges = badges
        self.height = height
        self.exercise = exercise
        self.education = education
        self.drinking = drinking
        self.smoking = smoking
        self.gender = gender
        self.intentions = intentions
        self.family_plans = family_plans
        self.star_sign = star_sign
        self.politics = politics
        self.religion = religion
        self.about_me = about_me
        self.sections = sections
        self.locations = locations

    def display_profile(self):
        print(f"Images Count: {len(self.images)}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Photo Verified: {self.photo_verified}")
        print(f"Occupation: {self.occupation}")
        print(f"School: {self.school}")
        print(f"Badges: {self.badges}")
        print(f"Height: {self.height}")
        print(f"Exercise: {self.exercise}")
        print(f"Education: {self.education}")
        print(f"Drinking: {self.drinking}")
        print(f"Smoking: {self.smoking}")
        print(f"Gender: {self.gender}")
        print(f"Intentions: {self.intentions}")
        print(f"Family Plans: {self.family_plans}")
        print(f"StarSign: {self.star_sign}")
        print(f"Politics: {self.politics}")
        print(f"Religion: {self.religion}")
        print(f"About Me: {self.about_me}")
        print(f"Sections: {self.sections}")
        print(f"Locations: {self.locations}")
        print('\n')







