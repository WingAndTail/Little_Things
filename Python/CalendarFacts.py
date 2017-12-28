###XKDC Calendar Facts###
# https://xkcd.com/1930/

#import necessary libraries
import random

#all the needed tuples
DidYouKnowThat1 = ("Easter ", "Toyota Truck Month ", "Shark Week ", "the fall equinox ", "the spring equinox ",
                   "the winter solstice ", "the winter olympics ", "the summer solstice ", "the summer olympics ",
                   "the earliest sunrise ", "the earliest sunset ", "the latest sunrise ", "the latest sunset ",
                   "daylight saving time ", "daylight savings time ", "leap day ", "leap year ", "the harvest moon ",
                   "the super moon ", "the blood moon ")
DidYouKnowThat2 = ("happens earlier every year ", "happens later every year ", "happens at the wrong time every year ",
                   "drifts out of sync with the  sun ", "drifts out of sync with the moon ",
                   "drifts out of sync with the zodiac ", "drifts out of sync with the gregorian calendar ",
                   "drifts out of sync with the mayan calendar ", "drifts out of sync with the lunar calendar ",
                   "drifts out of sync with the iPhone calendar ", "drifts out of sync with the atomic clock in Colorado ",
                   "might not happen this year ", "might happen twice this year ")
BecauseOf = ("a decree by the pope in the 1500s?", "magnetic field reversal?", "time zone legislation in Indiana?",
             "time zone legislation in Arizona?", "time zone legislation in Russia?", "precession of the moon?",
             "precession of the sun?", "precession of the earth's axis?", "precession of the equator?",
             "precession of the prime meridian?", "precession of the international date line?",
             "precession of the mason-dixon line?", "libration of the moon?", "libration of the sun?",
             "libration of the earth's axis?", "libration of the equator?", "libration of the prime meridian?",
             "libration of the international date line?", "libration of the mason-dixon line?", "nutation of the moon?",
             "nutation of the sun?", "nutation of the earth's axis?", "nutation of the equator?",
             "nutation of the prime meridian?", "nutation of the international date line?",
             "nutation of the mason-dixon line?", "libation of the moon?", "libation of the sun?",
             "libation of the earth's axis?", "libation of the equator?", "libation of the prime meridian?",
             "libation of the international date line?", "libation of the mason-dixon line?", "eccentricity of the moon?",
             "eccentricity of the sun?", "eccentricity of the earth's axis?", "eccentricity of the equator?",
             "eccentricity of the prime meridian?", "eccentricity of the international date line?",
             "eccentricity of the mason-dixon line?", "obliquity of the moon?", "obliquity of the sun?",
             "obliquity of the earth's axis?", "obliquity of the equator?", "obliquity of the prime meridian?",
             "obliquity of the international date-line?", "obliquity of the mason-dixon line?")
Apparently =("it causes a predictable increase in car accidents.", "that's why we have leap seconds.",
             "scientists are really worried.", "it's getting worse and no one knows why.",
             "it was even more extreme during the bronze age.", "it was even more extreme during the ice age.",
             "it was even more extreme during the cretaceous.", "it was even more extreme during the 1990s.",
             "there's a proposal to fix it, but it will never happen.",
             "there's a proposal to fix it, but it actually makes things worse.",
             "there's a proposal to fix it, but it is stalled in congress.",
             "there's a proposal to fix it, but it might be unconstitutional.")

#the main function
def CalFacts():
    DidYou = "Did you know that "
    BeOf = "because of "
    App = " Apparently "
    DidYouKnow1Rando = random.choice(DidYouKnowThat1)
    DidYouKnow2Rando = random.choice(DidYouKnowThat2)
    BecauseRando = random.choice(BecauseOf)
    ApprentRando = random.choice(Apparently)
    AllTheFacts = DidYou + DidYouKnow1Rando + DidYouKnow2Rando + BeOf + BecauseRando + App + ApprentRando
    return AllTheFacts
