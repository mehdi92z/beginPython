"""
error=True
while error==True:
    try:
        ageUtilisateur=int(input('donnez votre age'))
    except:
        print('un nombre svp')
    else:
        print("votre age est {}".format(ageUtilisateur))
        error=False
"""
#asssertio unse exception direct au lieu de if

try:
    ageUtilisateur = int(input('donnez votre age'))
    assert ageUtilisateur > 18
except AssertionError:
    print('vous etes mineur')