from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
app.json.sort_keys = False

DATA_FILE = 'books.json'

def read_json():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_json(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def check_book(data, require_all=True):
    fields = ["id_buku", "judul", "penulis", "tahun", "stok"]
    if require_all:
        for f in fields:
            if f not in data:
                return False, f"field {f} wajib ada"
    if "id_buku" in data:
        if not isinstance(data["id_buku"], int):
            return False, "id_buku harus angka"
    if "tahun" in data:
        if not isinstance(data["tahun"], int):
            return False, "tahun harus angka"
    if "stok" in data:
        if not isinstance(data["stok"], int) or data["stok"] < 0:
            return False, "stok harus angka dan tidak boleh negatif"
    return True, None

@app.route("/")
def home():
    return jsonify({
        "message": "API Sistem Perpustakaan",
        "routes": [
            "GET /books",
            "GET /books?id=<id_buku>",
            "GET /books?penulis=<nama_penulis>",
            "POST /books",
            "PUT /books",
            "DELETE /books"
        ]
    })

@app.route("/books", methods=["GET"])
def get_books():
    books = read_json()
    id_buku = request.args.get("id")
    penulis = request.args.get("penulis")

    if id_buku is not None:
        for b in books:
            if b["id_buku"] == int(id_buku):
                return jsonify(b)
        return jsonify({"message": "data tidak ditemukan"}), 404

    if penulis is not None:
        result = [b for b in books if b["penulis"].lower() == penulis.lower()]
        if not result:
            return jsonify({"message": "data tidak ditemukan"}), 404
        return jsonify(result)

    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not data:
        return jsonify({"message": "body kosong"}), 400

    valid, err = check_book(data)
    if not valid:
        return jsonify({"message": err}), 400

    books = read_json()
    for b in books:
        if b["id_buku"] == data["id_buku"]:
            return jsonify({"message": "id_buku sudah ada"}), 409

    books.append(data)
    write_json(books)

    return jsonify({"message": "Buku berhasil ditambahkan"}), 201

@app.route("/books", methods=["PUT"])
def update_book():
    data = request.get_json()
    if not data or "id_buku" not in data:
        return jsonify({"message": "id_buku wajib ada"}), 400

    valid, err = check_book(data, require_all=False)
    if not valid:
        return jsonify({"message": err}), 400

    books = read_json()
    for b in books:
        if b["id_buku"] == data["id_buku"]:
            b.update(data)
            write_json(books)
            return jsonify({"message": "Data berhasil diperbarui"})

    return jsonify({"message": "data tidak ditemukan"}), 404

@app.route("/books", methods=["DELETE"])
def delete_book():
    data = request.get_json()
    if not data or "id_buku" not in data:
        return jsonify({"message": "id_buku wajib ada"}), 400

    books = read_json()
    for i, b in enumerate(books):
        if b["id_buku"] == data["id_buku"]:
            books.pop(i)
            write_json(books)
            return jsonify({"message": "Data berhasil dihapus"})

    return jsonify({"message": "data tidak ditemukan"}), 404

if __name__ == "__main__":
    app.run(debug=True)
