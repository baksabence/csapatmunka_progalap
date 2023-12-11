import random

def ajandekok_keszitese(also_hatar=-10, felso_hatar=80):
    ajandekok = [random.randint(also_hatar, felso_hatar) for _ in range(20)]
    return ajandekok


def harmadik_ajandekok(ajandekok):
    harmadik_ajandekok = ajandekok[2::3]
    print("Harmadik ajándékok kategória azonosítói:")
    for i, azonosito in enumerate(harmadik_ajandekok, start=1):
        print(f"{i}. ajándék: {azonosito}")

if __name__ == "__main__":
    ajandekok = ajandekok_keszitese()
    harmadik_ajandekok(ajandekok)