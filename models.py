from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Albumai(db.Model):
    __tablename__ = "projektas"
    id = db.Column(db.Integer, primary_key=True)
    atlikejas = db.Column(db.String)
    pavadinimas = db.Column(db.String)
    metai = db.Column(db.Integer)
    zanras = db.Column(db.String)
    kaina_online = db.Column(db.Float)
    kaina_store = db.Column(db.Float)

    @property
    def kainu_vidurkis(self):
        return round((self.kaina_online + self.kaina_store) / 2, 2)

    def __repr__(self):
        return (f"ID: {self.id}, {self.atlikejas}, {self.pavadinimas}, "
                f"{self.metai}, {self.zanras}, {self.kaina_online}, {self.kaina_store}")
