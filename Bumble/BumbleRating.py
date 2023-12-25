from Extra import PreferedMatchConfig as Preferred
from Extra.PreferedMatchConfig import DEALBREAKERS


def rate_bio_name(bio):
    if bio.name is None:
        return 0

    if Preferred.NAMES is None:
        return 0

    if bio.name.lower() in to_lower_case(Preferred.NAMES):
        return 1
    else:
        return 0


def rate_bio_age(bio):
    if bio.age is None:
        return 0

    if Preferred.MIN_AGE > bio.age > Preferred.MAX_AGE:
        return 0
    else:
        return 1


def rate_bio_photo_verified(bio):
    if bio.photo_verified is None:
        return 0

    if Preferred.PHOTO_VERIFIED is None:
        return 0

    if bio.photo_verified == Preferred.PHOTO_VERIFIED:
        return 1
    else:
        return 0


def rate_bio_occupation(bio):
    if bio.occupation is None:
        return 0

    if Preferred.OCCUPATIONS is None:
        return 0

    if bio.occupation.lower() in to_lower_case(Preferred.OCCUPATIONS):
        return 1
    else:
        return 0


def rate_bio_school(bio):
    if bio.school is None:
        return 0

    if Preferred.SCHOOLS is None:
        return 0

    if bio.school in to_lower_case(Preferred.SCHOOLS):
        return 1
    else:
        return 0


def rate_bio_height(bio):
    if bio.height is None:
        return 0

    if Preferred.MIN_HEIGHT > bio.height > Preferred.MAX_HEIGHT:
        return 0
    else:
        return 1


def rate_bio_exercise(bio):
    if bio.exercise is None:
        return 0

    if Preferred.EXERCISE is None:
        return 0

    if bio.exercise in to_lower_case(Preferred.EXERCISE):
        return 1
    else:
        return 0


def rate_bio_education(bio):
    if bio.education is None:
        return 0

    if Preferred.EDUCATION is None:
        return 0

    if bio.education in to_lower_case(Preferred.EDUCATION):
        return 1
    else:
        return 0


def rate_bio_drinking(bio):
    if bio.drinking is None:
        return 0

    if Preferred.DRINKING is None:
        return 0

    if bio.drinking in to_lower_case(Preferred.DRINKING):
        return 1
    else:
        return 0


def rate_bio_smoking(bio):
    if bio.smoking is None:
        return 0

    if Preferred.SMOKING is None:
        return 0

    if bio.smoking in to_lower_case(Preferred.SMOKING):
        return 1
    else:
        return 0


def rate_bio_gender(bio):
    if bio.gender is None:
        return 0

    if Preferred.GENDER is None:
        return 0

    if bio.gender in to_lower_case(Preferred.GENDER):
        return 1
    else:
        return 0


def rate_bio_intentions(bio):
    if bio.intentions is None:
        return 0

    if Preferred.INTENTIONS is None:
        return 0

    if bio.intentions in to_lower_case(Preferred.INTENTIONS):
        return 1
    else:
        return 0


def rate_bio_family_plans(bio):
    if bio.family_plans is None:
        return 0

    if Preferred.FAMILY_PLANS is None:
        return 0

    if bio.family_plans in to_lower_case(Preferred.FAMILY_PLANS):
        return 1
    else:
        return 0


def rate_bio_star_sign(bio):
    if bio.star_sign is None:
        return 0

    if Preferred.STAR_SIGN is None:
        return 0

    if bio.star_sign in to_lower_case(Preferred.STAR_SIGN):
        return 1
    else:
        return 0


def rate_bio_politics(bio):
    if bio.politics is None:
        return 0

    if Preferred.POLITICS is None:
        return 0

    if bio.politics in to_lower_case(Preferred.POLITICS):
        return 1
    else:
        return 0


def rate_bio_religion(bio):
    if bio.religion is None:
        return 0

    if Preferred.RELIGION is None:
        return 0

    if bio.religion in to_lower_case(Preferred.RELIGION):
        return 1
    else:
        return 0


def rate_bio_words(bio):
    score = 0
    for keyword in to_lower_case(Preferred.KEYWORDS):
        if keyword in bio.about_me:
            score += 1
        for section in bio.sections:
            if keyword in section:
                score += 1
    return score


def bio_has_dealbreaker(bio):
    dealbreaker_list = []
    for dealbreaker in DEALBREAKERS:
        dealbreaker = dealbreaker.lower()

        if dealbreaker in bio.name.lower():
            print("deal breaker found in name: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.occupation.lower():
            print("deal breaker found in occupation: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.school.lower():
            print("deal breaker found in school: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.exercise.lower():
            print("deal breaker found in exercise: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.education.lower():
            print("deal breaker found in education: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.drinking.lower():
            print("deal breaker found in drinking: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.smoking.lower():
            print("deal breaker found in smoking: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.gender.lower():
            print("deal breaker found in gender: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.intentions.lower():
            print("deal breaker found in intentions: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.family_plans.lower():
            print("deal breaker found in family_plans: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.star_sign.lower():
            print("deal breaker found in star_sign: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.politics.lower():
            print("deal breaker found in politics: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.religion.lower():
            print("deal breaker found in religion: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        if dealbreaker in bio.about_me.lower():
            print("deal breaker found in about_me: " + dealbreaker)
            dealbreaker_list.append(dealbreaker)

        for section in bio.sections:
            if dealbreaker in section.lower():
                print("deal breaker found in section: " + dealbreaker)
                dealbreaker_list.append(dealbreaker)

        for location in bio.locations:
            if dealbreaker in location.lower():
                print("deal breaker found in locations: " + dealbreaker)
                dealbreaker_list.append(dealbreaker)

    if len(dealbreaker_list) > 0:
        print("deal breaker found in " + bio.name + "'s bio: ")
        print(dealbreaker_list)
        return True
    else:
        print("no deal breaker found in " + bio.name + "'s bio")
        return False


def sum_bio_ratings(bio):
    rating = \
        rate_bio_name(bio) + \
        rate_bio_age(bio) + \
        rate_bio_photo_verified(bio) + \
        rate_bio_occupation(bio) + \
        rate_bio_school(bio) + \
        rate_bio_height(bio) + \
        rate_bio_exercise(bio) + \
        rate_bio_education(bio) + \
        rate_bio_drinking(bio) + \
        rate_bio_smoking(bio) + \
        rate_bio_gender(bio) + \
        rate_bio_intentions(bio) + \
        rate_bio_family_plans(bio) + \
        rate_bio_star_sign(bio) + \
        rate_bio_politics(bio) + \
        rate_bio_religion(bio) + \
        rate_bio_words(bio)

    return rating


def to_lower_case(lst):
    return [element.lower() for element in lst]