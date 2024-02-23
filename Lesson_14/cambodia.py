from random import choice

capital="Phnom Penh"
bird ="animal can fly"

flower="is for smell"

song = "Honkai Before go out"

def randomfunfact():
    funfacts =[
        "in the sky",
        "the center of camboida capital",
        "that good",
        "sad song and good memories"
    ]
    
    index= choice("0123")
    
    print (funfacts[int(index)])
    
    # ///////////////////////////
    if __name__ == "__main__":
        randomfunfact()