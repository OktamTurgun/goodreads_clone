# 📚 Goodreads Clone

A Goodreads-inspired web application built with Django and Django REST Framework.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![DRF](https://img.shields.io/badge/DRF-3.x-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🛠 Tech Stack

**Backend**
- Python 3.12
- Django 6.0
- Django REST Framework
- PostgreSQL

**Frontend**
- Django Templates
- Bootstrap 5
- JavaScript (Fetch API)

**Tools**
- Git & GitHub
- python-dotenv
- Docker (coming soon)

## ✨ Current Features

- 📖 Browse and search books
- ✍️ Write reviews and rate books (1–5)
- 📚 Add books to personal shelf (want to read / reading / read)
- 👤 User registration and authentication
- 🔐 Session-based authentication
- 🛠 Admin panel for managing books and authors

## 🔮 Roadmap

### v1.1
- [ ] Book search and filtering
- [ ] Pagination
- [ ] Book cover image upload
- [ ] User avatar

### v1.2
- [ ] Follow other users
- [ ] Reading activity feed
- [ ] Book recommendations

### v1.3
- [ ] REST API (DRF)
- [ ] JWT Authentication
- [ ] API documentation (Swagger)

### v2.0
- [ ] Docker & Docker Compose
- [ ] CI/CD (GitHub Actions)
- [ ] Deploy (Railway / Render)
- [ ] Redis + Celery (async tasks)
- [ ] Email notifications

## 🚀 Getting Started

### Requirements
- Python 3.12+
- PostgreSQL 16+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/OktamTurgun/goodreads.git
cd goodreads
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```
Edit `.env` and fill in your values:
```bash
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=goodreads
DB_USER=goodreads_user
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Set up PostgreSQL
```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE goodreads;
CREATE USER goodreads_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE goodreads TO goodreads_user;
ALTER USER goodreads_user CREATEDB;
\q
```

### 6. Run migrations
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

## 🗄 Database Schema

| Table | Description |
|---|---|
| `users` | Django built-in User model |
| `books` | Book information |
| `authors` | Author information |
| `books_author` | Book ↔ Author (Many-to-Many) |
| `reviews` | User reviews and ratings |
| `user_books` | User's personal book shelf |

## 📁 Project Structure
```
goodreads/
├── config/           # Project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── accounts/         # Authentication
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── books/            # Books, authors, reviews
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   └── urls.py
├── templates/        # HTML templates
│   ├── base.html
│   ├── landing_page.html
│   └── accounts/
├── .env.example
└── requirements.txt
```

## 🧪 Running Tests
```bash
# All tests
python manage.py test

# Specific app
python manage.py test accounts

# Specific class
python manage.py test accounts.tests.LoginViewTest
```

## 📝 API Endpoints

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| GET | `/api/books/` | List all books | No |
| GET | `/api/books/:id/` | Book detail | No |
| GET | `/api/books/:id/reviews/` | Book reviews | No |
| GET | `/api/authors/` | List all authors | No |
| POST | `/api/reviews/` | Create review | Yes |
| PUT | `/api/reviews/:id/` | Update review | Owner |
| DELETE | `/api/reviews/:id/` | Delete review | Owner |
| GET | `/api/user-books/` | My shelf | Yes |
| POST | `/api/user-books/` | Add to shelf | Yes |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👤 Author

**Uktam Turgunov** — Backend Developer
- GitHub: [@OktamTurgun](https://github.com/OktamTurgun)

## 📄 License

MIT License — see [LICENSE](LICENSE) file for details.