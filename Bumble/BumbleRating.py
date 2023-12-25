from Extra import PreferedMatchConfig as Preferred
from Extra.PreferedMatchConfig import DEALBREAKERS

#locations are not rated
#badges are not rated

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

    bio_occupation_lower = bio.occupation.lower()
    preferred_occupations_lower = to_lower_case(Preferred.OCCUPATIONS)

    for preferred_occupation in preferred_occupations_lower:
        if preferred_occupation in bio_occupation_lower:
            return 1
    return 0


def rate_bio_school(bio):
    if bio.school is None:
        return 0

    if Preferred.SCHOOLS is None:
        return 0

    bio_school_lower = bio.school.lower()
    preferred_schools_lower = to_lower_case(Preferred.SCHOOLS)

    for preferred_school in preferred_schools_lower:
        if preferred_school in bio_school_lower:
            return 1
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

    bio_exercise_lower = bio.exercise.lower()
    preferred_exercise_lower = to_lower_case(Preferred.EXERCISE)

    for preferred_exercise in preferred_exercise_lower:
        if preferred_exercise in bio_exercise_lower:
            return 1
    return 0


def rate_bio_education(bio):
    if bio.education is None:
        return 0

    if Preferred.EDUCATION is None:
        return 0

    bio_education_lower = bio.education.lower()
    preferred_education_lower = to_lower_case(Preferred.EDUCATION)

    for preferred_education in preferred_education_lower:
        if preferred_education in bio_education_lower:
            return 1
    return 0


def rate_bio_drinking(bio):
    if bio.drinking is None:
        return 0

    if Preferred.DRINKING is None:
        return 0

    bio_drinking_lower = bio.drinking.lower()
    preferred_drinking_lower = to_lower_case(Preferred.DRINKING)

    for preferred_drinking in preferred_drinking_lower:
        if preferred_drinking in bio_drinking_lower:
            return 1
    return 0


def rate_bio_smoking(bio):
    if bio.smoking is None:
        return 0

    if Preferred.SMOKING is None:
        return 0

    bio_smoking_lower = bio.smoking.lower()
    preferred_smoking_lower = to_lower_case(Preferred.SMOKING)

    for preferred_smoking in preferred_smoking_lower:
        if preferred_smoking in bio_smoking_lower:
            return 1
    return 0


def rate_bio_gender(bio):
    if bio.gender is None:
        return 0

    if Preferred.GENDER is None:
        return 0

    bio_gender_lower = bio.gender.lower()
    preferred_gender_lower = to_lower_case(Preferred.GENDER)

    for preferred_smoking in preferred_gender_lower:
        if preferred_smoking in bio_gender_lower:
            return 1
    return 0


def rate_bio_intentions(bio):
    if bio.intentions is None:
        return 0

    if Preferred.INTENTIONS is None:
        return 0

    bio_intentions_lower = bio.intentions.lower()
    preferred_intentions_lower = to_lower_case(Preferred.INTENTIONS)

    for preferred_intention in preferred_intentions_lower:
        if preferred_intention in bio_intentions_lower:
            return 1
    return 0


def rate_bio_family_plans(bio):
    if bio.family_plans is None:
        return 0

    if Preferred.FAMILY_PLANS is None:
        return 0

    bio_family_plans_lower = bio.family_plans.lower()
    preferred_family_plans_lower = to_lower_case(Preferred.FAMILY_PLANS)

    for preferred_family_plan in preferred_family_plans_lower:
        if preferred_family_plan in bio_family_plans_lower:
            return 1
    return 0


def rate_bio_star_sign(bio):
    if bio.star_sign is None:
        return 0

    if Preferred.STAR_SIGN is None:
        return 0

    bio_star_sign_lower = bio.star_sign.lower()
    preferred_star_sign_lower = to_lower_case(Preferred.STAR_SIGN)

    for preferred_star_sign in preferred_star_sign_lower:
        if preferred_star_sign in bio_star_sign_lower:
            return 1
    return 0


def rate_bio_politics(bio):
    if bio.politics is None:
        return 0

    if Preferred.POLITICS is None:
        return 0

    bio_politics_lower = bio.politics.lower()
    preferred_politics_lower = to_lower_case(Preferred.POLITICS)

    for preferred_politic in preferred_politics_lower:
        if preferred_politic in bio_politics_lower:
            return 1
    return 0


def rate_bio_religion(bio):
    if bio.religion is None:
        return 0

    if Preferred.RELIGION is None:
        return 0

    bio_religion_lower = bio.religion.lower()
    preferred_religion_lower = to_lower_case(Preferred.RELIGION)

    for preferred_religion in preferred_religion_lower:
        if preferred_religion in bio_religion_lower:
            return 1
    return 0


def rate_bio_words(bio):
    score = 0
    for keyword in to_lower_case(Preferred.KEYWORDS):
        if keyword in bio.about_me.lower():
            score += 1
        for section in to_lower_case(bio.sections):
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