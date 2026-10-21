from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for books
books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt & David Thomas",
        "year": 1999,
    },
]


@app.route("/books", methods=["GET"])
def get_books():
    """Retrieve all books in the library catalog."""
    return jsonify({"books": books, "total": len(books)}), 200


@app.route("/books", methods=["POST"])
def add_book():
    """Add a new book to the library catalog."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    title = data.get("title")
    author = data.get("author")
    year = data.get("year")

    if not title or not isinstance(title, str) or not title.strip():
        return jsonify({"error": "'title' is required and must be a non-empty string"}), 400

    if not author or not isinstance(author, str) or not author.strip():
        return jsonify({"error": "'author' is required and must be a non-empty string"}), 400

    new_id = (max([b["id"] for b in books], default=0)) + 1
    new_book = {
        "id": new_id,
        "title": title.strip(),
        "author": author.strip(),
        "year": int(year) if year is not None and str(year).isdigit() else None,
    }
    books.append(new_book)
    return jsonify({
        "message": "Book added successfully",
        "book": new_book,
    }), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
