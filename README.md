<div align="center">
  <h1><b>REDIS CACHE MANAGEMENT</b></h1>
  <h4>Optimized caching solution for Django applications using Redis</h4>
</div>

## 📗 Table of Contents

- 📖 About the Project
- 👀 Overview
- 🛠 Built With
  - 🔥 Tech Stack
- 🔑 Key Features
- 💻 Getting Started
  - 📜 Prerequisites
  - ⚙️ Setup
  - ▶️ Run Application
  - 🕹️ Usage
- 👥 Author

## 📖 About the Project

Redis Cache Management is a backend microservice integrated into a Django application, designed to optimize data retrieval and application performance by leveraging Redis as an in-memory data store. This service streamlines cache management, reduces latency, and minimizes load on backend databases.

## 👀 Overview

- The service provides methods to store (`setredisdata`), retrieve (`getredisdata`), and delete (`deleteredisdata`) cached data in Redis.
- It handles caching efficiently, storing responses for up to 45 days to reduce the need for repeated data fetching from the backend.

## 🛠 Built With

- Python
- Django
- Redis
- JSON

### 🔥 Tech Stack

- Django
- Redis

### 🔑 Key Features

- **Efficient Caching**: Caches data for up to 45 days to reduce backend load.
- **Data Retrieval**: Retrieves data from the cache, minimizing response time.
- **Cache Management**: Provides methods to set, get, and delete cache entries.

## 💻 Getting Started

### 📜 Prerequisites

To use this service, you will need:

- Python 3.x
- Django
- Redis server installed
- Required Python libraries: `django-redis`, `json`.

### ⚙️ Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/redis-cache-management.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd redis-cache-management
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Redis in Django**:

    In your Django project's `settings.py`, add the following configuration:

    ```python
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    ```

5. **Start the Redis server**:
    ```bash
    sudo service redis-server start
    ```

### ▶️ Run Application

1. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

### 🕹️ Usage

1. **Set Data**: Use the `setredisdata` method to store data in Redis.
2. **Get Data**: Use the `getredisdata` method to retrieve cached data.
3. **Delete Data**: Use the `deleteredisdata` method to delete cache entries as needed.

- [👥 Author](#author)
  - Vedant Vartak
    - Email ✉️: vedantvartakworkk@gmail.com
    - Country 🌍: India 🇮🇳

**Example Usage**:

To set data in the cache, you can send a POST request to the `setredisdata` endpoint with the following payload:

```json
{
    "key": "unique_key",
    "value": {
        "data": "your_data"
    }
}
