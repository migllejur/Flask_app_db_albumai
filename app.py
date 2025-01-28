from models import db, Albumai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///albumai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("search")
    if search_text:
        filtered_rows = Albumai.query.filter(Albumai.pavadinimas.ilike(f"%{search_text}%"))
        return render_template("index.html", albums=filtered_rows)
    else:
        all_albums = Albumai.query.all()
        return render_template("index.html", albums=all_albums, is_homepage=True)


# select
@app.route("/albumas/<int:row_id>")
def one_album(row_id):
    album = Albumai.query.get(row_id)
    if album:
        return render_template("one_album.html", album=album)
    else:
        return f"Albumas ID {row_id} nerastas"


# update
@app.route("/albumas/edit/<int:row_id>", methods=["get", "post"])
def update_album(row_id):
    album = Albumai.query.get(row_id)
    if not album:
        return f"Albumas ID {row_id} nerastas"
    if request.method == "GET":
        return render_template("update_album_form.html", album=album)
    elif request.method == "POST":
        artist = request.form.get("artist")
        title = request.form.get("title")
        year = int(request.form.get("year"))
        genre = request.form.get("genre")
        price_online = float(request.form.get("price_online"))
        price_store = float(request.form.get("price_store"))
        album.atlikejas = artist
        album.pavadinimas = title
        album.metai = year
        album.zanras = genre
        album.kaina_online = price_online
        album.kaina_store = price_store
        db.session.commit()
        return redirect(f"/albumas/{row_id}")


# delete
@app.route("/albumas/delete/<int:row_id>", methods=["POST"])
def delete_album(row_id):
    album = Albumai.query.get(row_id)
    if not album:
        return f"Albumas ID {row_id} nerastas"
    else:
        db.session.delete(album)
        db.session.commit()
        return redirect(url_for("home"))


# insert
@app.route("/albumas/new", methods=["get", "post"])
def create_album():
    if request.method == "GET":
        return render_template("create_album_form.html")
    if request.method == "POST":
        artist = request.form.get("artist")
        title = request.form.get("title")
        year = int(request.form.get("year"))
        genre = request.form.get("genre")
        price_online = float(request.form.get("price_online"))
        price_store = float(request.form.get("price_store"))
        if artist and title and year and genre and price_online and price_store:
            new_album = Albumai(atlikejas=artist, pavadinimas=title, metai=year, zanras=genre,
                                kaina_online=price_online, kaina_store=price_store)
            db.session.add(new_album)
            db.session.commit()
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=5001)
