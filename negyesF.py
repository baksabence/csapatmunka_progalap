class KariVersKezelo:
    def __init__(self, be_fajl, kieg_fajl):
        self.be_fajl = be_fajl
        self.kieg_fajl = kieg_fajl

    def beolvas(self):
        beolvasas = open(self.be_fajl, "r", encoding="utf-8")
        beolvasas.readlines()
        return beolvasas.read()

    def kiir(self, kiegeszitett_vers):
        kiiras = open(self.kieg_fajl, "w", encoding="utf-8")
        kiiras.write(kiegeszitett_vers)

def main():
    vers_kezelo = KariVersKezelo("KariVers.txt", "KariVers2.txt")

    kari_vers = vers_kezelo.beolvas()

    uj_versszak = "Tiszta öröm tüze átég\na szemeken, a harangjáték\nszól, éjféli üzenet:\nKis Jézuska született!"

    kari_vers_kiegeszitett = kari_vers + "\n" + uj_versszak

    vers_kezelo.kiir(kari_vers_kiegeszitett)