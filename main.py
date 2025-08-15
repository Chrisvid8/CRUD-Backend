from app import create_app

app = create_app()

# Root route for API home page
@app.route("/")
def home():
    return {
        "status": "success",
        "message": "CRUD Backend API is running 🚀",
        "available_endpoints": ["/api/items"]
    }

if __name__ == '__main__':
    app.run(debug=True)
