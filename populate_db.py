from models import Albumai, db
from app import app

with app.app_context():
    projektai = [
        Albumai(atlikejas="SAULT", pavadinimas="Earth", metai=2022, zanras="neo-seoul", kaina_online=12.99,
                kaina_store=15.99),
        Albumai(atlikejas="Charles Lloyd", pavadinimas="The Sky Will Still Be There Tomorrow", metai=2024,
                zanras="post-bop", kaina_online=11.49, kaina_store=14.99),
        Albumai(atlikejas="Self Esteem", pavadinimas="Prioritise Pleasure", metai=2021, zanras="electropop, alt-pop",
                kaina_online=9.99, kaina_store=13.49),
        Albumai(atlikejas="Fiona Apple", pavadinimas="Fetch the Bolt Cutters", metai=2020,
                zanras="art pop, progressive pop", kaina_online=14.99, kaina_store=18.49),
        Albumai(atlikejas="jaimie branch", pavadinimas="Fly or Die Fly or Die Fly or Die ((world war))", metai=2023,
                zanras="avant-garde jazz", kaina_online=13.49, kaina_store=16.99),
        Albumai(atlikejas="For Those I Love", pavadinimas="For Those I Love", metai=2021,
                zanras="progressive house, UK garage", kaina_online=10.99, kaina_store=14.49),
        Albumai(atlikejas="Aaron West & The Roaring Twenties", pavadinimas="In Lieu of Flowers", metai=2024,
                zanras="folk rock, indie folk", kaina_online=8.99, kaina_store=12.99),
        Albumai(atlikejas="Corinne Bailey Rae", pavadinimas="Black Rainbows", metai=2023,
                zanras="art pop, art rock, jazz fusion", kaina_online=12.49, kaina_store=16.49),
        Albumai(atlikejas="The Cure", pavadinimas="Songs of a Lost World", metai=2024,
                zanras="alternative rock, gothic rock", kaina_online=13.99, kaina_store=17.99),
        Albumai(atlikejas="Little Simz", pavadinimas="Sometimes I Might Be Introvert", metai=2021, zanras="UK hip-hop",
                kaina_online=11.99, kaina_store=15.99),
        Albumai(atlikejas="Julian Lage", pavadinimas="Speak To Me", metai=2024, zanras="post-bop", kaina_online=10.49,
                kaina_store=13.99),
        Albumai(atlikejas="The Callous Daoboys", pavadinimas="Celebrity Therapist", metai=2022, zanras="mathcore",
                kaina_online=9.99, kaina_store=13.49),
        Albumai(atlikejas="Perfume Genius", pavadinimas="Set My Heart On Fire Immediately", metai=2020,
                zanras="art pop", kaina_online=14.49, kaina_store=19.49),
        Albumai(atlikejas="Bad Bunny", pavadinimas="DeBÍ TiRAR MáS FOToS", metai=2025, zanras="reggaeton",
                kaina_online=13.49, kaina_store=18.49),
        Albumai(atlikejas="SAULT", pavadinimas="Untitled (Rise)", metai=2020, zanras="neo-soul, funk",
                kaina_online=10.99, kaina_store=14.99),
        Albumai(atlikejas="Charli XCX", pavadinimas="BRAT", metai=2024, zanras="electropop, EDM", kaina_online=12.49,
                kaina_store=17.49),
        Albumai(atlikejas="Run the Jewels", pavadinimas="RTJ4", metai=2020, zanras="hardcore hip-hop",
                kaina_online=11.99, kaina_store=15.99),
        Albumai(atlikejas="Allison Russell", pavadinimas="The Returner", metai=2023, zanras="singer-songwriter",
                kaina_online=13.99, kaina_store=17.99),
        Albumai(atlikejas="Rafael Toral", pavadinimas="Spectral Evolution", metai=2024,
                zanras="electroacoustic, ambient", kaina_online=9.49, kaina_store=12.99),
        Albumai(atlikejas="Gabriels", pavadinimas="Angels & Queens - Part I", metai=2022,
                zanras="contemporary R&B, soul", kaina_online=12.99, kaina_store=16.99)
    ]

    db.session.add_all(projektai)
    db.session.commit()
    print("Duomenys užpildyti")
