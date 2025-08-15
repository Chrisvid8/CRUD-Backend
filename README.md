# CRUD Dashboard — Backend

This is the **backend** of the CRUD Dashboard personal project, built with Flask and SQLAlchemy.  
It provides RESTful API endpoints to manage items in a Supabase (PostgreSQL) database.

## 🚀 Live API
🔗 **[Live API on Render](https://crud-backend-q5f8.onrender.com/api/items)**

## 🛠️ Technologies Used
- **Flask** — Python web framework
- **Flask-SQLAlchemy** — ORM for database management
- **Flask-Migrate** — Database migrations
- **PostgreSQL (Supabase)** — Cloud database
- **Render** — Backend deployment

## 📂 Features
- Create, read, update, and delete items
- JSON API responses
- Cross-Origin Resource Sharing (CORS) enabled
- Database migrations with Alembic

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/items` | Get all items |
| GET    | `/api/items/<id>` | Get a single item |
| POST   | `/api/items` | Create a new item |
| PUT    | `/api/items/<id>` | Update an existing item |
| DELETE | `/api/items/<id>` | Delete an item |

## 📦 Installation (Local Development)
You can run the backend locally if you want to test without deploying to Render.

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chrisvid8/CRUD-Backend.git
   cd CRUD-Backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**  
   Create a `.env` file in the project root and add your database URL:
   ```env
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxxxxx.supabase.co:5432/postgres
   ```

5. **Run database migrations**
   ```bash
   flask db upgrade
   ```

6. **Start the development server**
   ```bash
   flask run
   ```
