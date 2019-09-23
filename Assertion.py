def KelvinToFarenhight(Temperature):
    assert(Temperature >=0),"colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print (KelvinToFarenhight(273))
