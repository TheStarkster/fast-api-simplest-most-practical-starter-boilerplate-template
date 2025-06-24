# Audio-to-Video Generator Backend

A modern FastAPI backend service for generating videos from audio files. Built with Python 3.12+ and featuring JWT authentication, PostgreSQL database integration, and a clean REST API architecture.

## 🚀 Features

- **Modern FastAPI Framework** - High-performance async API with automatic OpenAPI documentation
- **JWT Authentication** - Secure token-based authentication system
- **User Management** - User registration, login, and profile management
- **PostgreSQL Integration** - Robust database with SQLAlchemy ORM
- **Password Security** - bcrypt hashing for secure password storage
- **Email Validation** - Pydantic email validation with proper formatting
- **Auto-Reload Development** - Modern development server with hot reload
- **Fast Package Management** - uv package manager for lightning-fast dependency installation

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.115+
- **Database**: PostgreSQL with SQLAlchemy 2.0+
- **Authentication**: JWT tokens with python-jose
- **Password Hashing**: bcrypt
- **Validation**: Pydantic with email validation
- **Package Manager**: uv (modern pip alternative)
- **Python**: 3.12+

## 📋 Prerequisites

- Python 3.12 or higher
- PostgreSQL database server
- uv package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))

## ⚡ Quick Start

### 1. Install uv (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Setup

```bash
git clone <your-repo-url>
cd audio-to-video/backend
```

### 3. Install Dependencies

```bash
# Install all dependencies (creates virtual environment automatically)
uv sync
```

### 4. Database Setup

Make sure PostgreSQL is running and create the database:

```sql
CREATE DATABASE video_gen;
CREATE USER destinpq_user WITH PASSWORD 'destinpq_user_1234';
GRANT ALL PRIVILEGES ON DATABASE video_gen TO destinpq_user;
```

### 5. Run Development Server

```bash
# Modern development server with auto-reload
uv run fastapi dev main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register` | Register new user | ❌ |
| POST | `/api/auth/login` | User login | ❌ |
| GET | `/api/auth/me` | Get current user | ✅ |

### Request/Response Examples

#### Register User
```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com", 
    "password": "secretpassword"
  }'
```

#### Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "secretpassword"
  }'
```

#### Get Current User
```bash
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🏗️ Project Structure

```
backend/
├── config/
│   ├── db.py              # Database configuration
│   ├── jwt.py             # JWT token handling
│   └── password.py        # Password hashing utilities
├── models/
│   └── user.py            # SQLAlchemy user model
├── routes/
│   ├── auth.py            # Authentication routes
│   ├── deps.py            # Dependency injection
│   └── routes.py          # Main router
├── schemas/
│   ├── token.py           # Token request/response schemas
│   └── user.py            # User validation schemas
├── main.py                # FastAPI application entry point
├── pyproject.toml         # Dependencies and project config
└── README.md              # This file
```

## 🔧 Development

### Adding Dependencies

```bash
# Add new package
uv add package-name

# Add development dependency
uv add --dev package-name

# Remove package
uv remove package-name
```

### Running Commands

```bash
# Development server (auto-reload)
uv run fastapi dev main.py

# Production server
uv run fastapi run main.py

# Run Python scripts
uv run python script.py

# Access Python shell with project dependencies
uv run python
```

### Database Migrations

Currently using SQLAlchemy with declarative models. To add database migrations:

```bash
# Add Alembic for migrations
uv add alembic

# Initialize Alembic
uv run alembic init alembic

# Create migration
uv run alembic revision --autogenerate -m "Add new table"

# Run migrations
uv run alembic upgrade head
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file for environment-specific settings:

```env
# Database
DATABASE_URL=postgresql://destinpq_user:destinpq_user_1234@localhost:5432/video_gen

# JWT
JWT_SECRET_KEY=your-super-secret-key-here
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60

# Development
DEBUG=True
```

### Database Configuration

Update `config/db.py` to use environment variables:

```python
import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://destinpq_user:destinpq_user_1234@localhost:5432/video_gen")
```

## 🧪 Testing

```bash
# Add testing dependencies
uv add --dev pytest pytest-asyncio httpx

# Run tests
uv run pytest

# Run with coverage
uv add --dev pytest-cov
uv run pytest --cov=.
```

## 🚀 Production Deployment

### Using Docker

```dockerfile
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy project files
COPY . /app
WORKDIR /app

# Install dependencies
RUN uv sync --frozen --no-cache

# Run the application
CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]
```

### Using uv in Production

```bash
# Install production dependencies only
uv sync --no-dev

# Run production server
uv run fastapi run main.py --port 8000 --host 0.0.0.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and test them
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature/new-feature`
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**Built with ❤️ using FastAPI and modern Python tooling**
