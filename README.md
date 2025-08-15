# CRUD-Backend

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
1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
