class Rechteck:
    def __init__(self, b, h):
        self.breite = b
        self.hoehe = h

    def umfang(self):
        return 2 * self.breite + 2 * self.hoehe
    
    def flaeche(self):
        return self.breite * self.hoehe
    

rechteck1 = Rechteck(4, 8)
rechteck2 = Rechteck(5, 12)

print(f"Rechteck 1: Fläche = {rechteck1.flaeche()}, Umfang = {rechteck1.umfang()}")
print(f"Rechteck 2: Fläche = {rechteck2.flaeche()}, Umfang = {rechteck2.umfang()}")