
# 🛍️ FastAPI Shop - Полнофункциональный интернет-магазин

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python) ![FastAPI](https://img.shields.io/badge/FastAPI-0.119.0-009688?style=for-the-badge&logo=fastapi) ![Vue.js](https://img.shields.io/badge/Vue.js-3.5-4FC08D?style=for-the-badge&logo=vue.js) ![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)

Современный, масштабируемый интернет-магазин с REST API на FastAPI и SPA frontend на Vue.js 3

</div>

---

## 📋 Содержание

- [О проекте](#-%D0%BE-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B5)
- [Структура проекта](#-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
- [Технологический стек](#-%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D1%81%D1%82%D0%B5%D0%BA)
- [Быстрый старт](#-%D0%B1%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9-%D1%81%D1%82%D0%B0%D1%80%D1%82)
- [API документация](#-api-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F)
- [Архитектура](#-%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0)

---

## 🎯 О проекте

**FastAPI Shop** - это современное веб-приложение для электронной коммерции. Проект демонстрирует best practices разработки full-stack приложений с разделением backend и frontend.

### ✨ Ключевые возможности

- 🛒 **Управление корзиной** - добавление, удаление, изменение количества товаров
- 📦 **Каталог товаров** - просмотр товаров с фильтрацией по категориям
- 🔍 **Детальная информация** - подробные страницы товаров
- 💾 **Персистентность данных** - сохранение корзины в localStorage
- 🎨 **Современный UI** - адаптивный дизайн на Tailwind CSS
- 🚀 **Production-ready** - автоматический деплой с SSL сертификатами

---

## 📁 Структура проекта

```
fastapi-shop/
│
├── backend/                      # Backend часть (FastAPI)
│   ├── app/
│   │   ├── models/              # SQLAlchemy модели БД
│   │   │   ├── category.py     # Модель категорий
│   │   │   └── product.py      # Модель товаров
│   │   │
│   │   ├── schemas/             # Pydantic схемы для валидации
│   │   │   ├── cart.py         # Схемы корзины
│   │   │   ├── category.py     # Схемы категорий
│   │   │   └── product.py      # Схемы товаров
│   │   │
│   │   ├── repositories/        # Слой работы с БД (Repository Pattern)
│   │   │   ├── category_repository.py
│   │   │   └── product_repository.py
│   │   │
│   │   ├── services/            # Бизнес-логика приложения
│   │   │   ├── cart_service.py
│   │   │   ├── category_service.py
│   │   │   └── product_service.py
│   │   │
│   │   ├── routes/              # API endpoints (Controllers)
│   │   │   ├── cart.py         # Эндпоинты корзины
│   │   │   ├── categories.py   # Эндпоинты категорий
│   │   │   └── products.py     # Эндпоинты товаров
│   │   │
│   │   ├── config.py            # Конфигурация приложения
│   │   ├── database.py          # Настройка SQLAlchemy
│   │   └── main.py              # Точка входа FastAPI
│   │
│   ├── static/images/           # Статические файлы (изображения)
│   ├── Dockerfile               # Docker образ backend
│   ├── requirements.txt         # Python зависимости
│   ├── run.py                   # Скрипт запуска сервера
│   └── seed_data.py            # Заполнение БД тестовыми данными
│
├── frontend/                     # Frontend часть (Vue.js 3)
│   ├── src/
│   │   ├── components/          # Vue компоненты
│   │   │   ├── CartItem.vue    # Элемент корзины
│   │   │   ├── CategoryFilter.vue  # Фильтр категорий
│   │   │   ├── Header.vue      # Шапка сайта
│   │   │   └── ProductCard.vue # Карточка товара
│   │   │
│   │   ├── views/               # Страницы приложения
│   │   │   ├── HomePage.vue    # Главная (каталог)
│   │   │   ├── ProductDetailPage.vue  # Детали товара
│   │   │   └── CartPage.vue    # Страница корзины
│   │   │
│   │   ├── stores/              # Pinia stores (State Management)
│   │   │   ├── cart.js         # Store корзины
│   │   │   └── products.js     # Store товаров
│   │   │
│   │   ├── services/            # API клиенты
│   │   │   └── api.js          # Axios конфигурация и методы
│   │   │
│   │   ├── router/              # Vue Router конфигурация
│   │   │   └── index.js        # Определение маршрутов
│   │   │
│   │   ├── assets/              # Статические ресурсы
│   │   ├── App.vue              # Корневой компонент
│   │   └── main.js              # Точка входа приложения
│   │
│   ├── Dockerfile               # Docker образ frontend
│   ├── nginx.conf               # Конфигурация Nginx для SPA
│   ├── package.json             # NPM зависимости
│   └── vite.config.js          # Конфигурация Vite
│
├── nginx/                        # Reverse proxy конфигурация
│   └── nginx.conf               # Главная конфигурация Nginx
│
├── docker-compose.yml            # Оркестрация Docker контейнеров
├── deploy.sh                     # Скрипт автоматического деплоя
└── README.md                     # Документация проекта
```

### 🔍 Назначение компонентов

#### Backend (FastAPI)

|Компонент|Назначение|
|---|---|
|**models/**|SQLAlchemy модели для работы с БД (ORM)|
|**schemas/**|Pydantic схемы для валидации входящих/исходящих данных|
|**repositories/**|Инкапсуляция логики работы с БД (Repository Pattern)|
|**services/**|Бизнес-логика приложения (Service Layer)|
|**routes/**|HTTP endpoints и маршрутизация (Controllers)|
|**config.py**|Настройки приложения (CORS, DB, пути)|
|**database.py**|Конфигурация SQLAlchemy и управление сессиями|
|**main.py**|Инициализация FastAPI, подключение middleware и роутеров|

#### Frontend (Vue.js 3)

|Компонент|Назначение|
|---|---|
|**components/**|Переиспользуемые UI компоненты|
|**views/**|Страницы приложения (роутинг)|
|**stores/**|Глобальное состояние приложения (Pinia)|
|**services/**|HTTP клиент для взаимодействия с API|
|**router/**|Конфигурация маршрутизации (Vue Router)|

---

## 🛠 Технологический стек

### Backend

- **FastAPI** 0.119.0 - современный, быстрый web-framework
- **SQLAlchemy** 2.0.44 - ORM для работы с базой данных
- **Pydantic** 2.12.1 - валидация данных и настроек
- **SQLite** - легковесная реляционная СУБД
- **Uvicorn** - ASGI сервер для production

### Frontend

- **Vue.js** 3.5.22 - прогрессивный JavaScript фреймворк
- **Pinia** 3.0.3 - официальный state management для Vue 3
- **Vue Router** 4.5.1 - роутинг для SPA
- **Axios** 1.12.2 - HTTP клиент
- **Tailwind CSS** - utility-first CSS фреймворк
- **Vite** 7.1.7 - быстрый build tool

### DevOps

- **Docker** - контейнеризация приложений
- **Docker Compose** - оркестрация multi-container приложений
- **Nginx** - reverse proxy и веб-сервер
- **Let's Encrypt** - бесплатные SSL сертификаты
- **Certbot** - автоматическое обновление сертификатов

---

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.11+
- Node.js 20+
- npm/yarn
- Git

### Локальная разработка

#### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/yourusername/fastapi-shop.git
cd fastapi-shop
```

#### 2️⃣ Запуск Backend

```bash
# Переход в директорию backend
cd backend

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Заполнение базы данных тестовыми данными
python seed_data.py

# Запуск сервера разработки
python run.py
```

Backend будет доступен по адресу: **http://localhost:8000**
API документация (Swagger UI): **http://localhost:8000/api/docs**

#### 3️⃣ Запуск Frontend

```bash
# Переход в директорию frontend (новый терминал)
cd frontend

# Установка зависимостей
npm install

# Запуск dev сервера
npm run dev
```

Frontend будет доступен по адресу: **http://localhost:5173**

## 📚 API документация

### Основные endpoints

#### Products (Товары)

|Метод|Endpoint|Описание|
|---|---|---|
|GET|`/api/products`|Получить все товары|
|GET|`/api/products/{id}`|Получить товар по ID|
|GET|`/api/products/category/{category_id}`|Товары по категории|

#### Categories (Категории)

|Метод|Endpoint|Описание|
|---|---|---|
|GET|`/api/categories`|Получить все категории|
|GET|`/api/categories/{id}`|Получить категорию по ID|

#### Cart (Корзина)

|Метод|Endpoint|Описание|
|---|---|---|
|POST|`/api/cart/add`|Добавить товар в корзину|
|POST|`/api/cart`|Получить содержимое корзины|
|PUT|`/api/cart/update`|Обновить количество товара|
|DELETE|`/api/cart/remove/{id}`|Удалить товар из корзины|

### Примеры запросов

#### Получить все товары

```bash
curl -X GET "http://localhost:8000/api/products"
```

**Ответ:**

```json
{
  "products": [
    {
      "id": 1,
      "name": "Wireless Headphones",
      "description": "High-quality wireless headphones...",
      "price": 299.99,
      "category_id": 1,
      "image_url": "https://...",
      "created_at": "2024-01-15T10:30:00",
      "category": {
        "id": 1,
        "name": "Electronics",
        "slug": "electronics"
      }
    }
  ],
  "total": 13
}
```

#### Добавить товар в корзину

```bash
curl -X POST "http://localhost:8000/api/cart/add" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 2,
    "cart": {}
  }'
```

**Ответ:**

```json
{
  "cart": {
    "1": 2
  }
}
```

Полная документация API с интерактивными примерами доступна по адресу:
**http://localhost:8000/api/docs** (Swagger UI)

---

## 🏗 Архитектура

### Backend Architecture (Layered Architecture)

```
┌─────────────────────────────────────────┐
│           API Layer (Routes)            │  ← HTTP Endpoints
├─────────────────────────────────────────┤
│        Service Layer (Services)         │  ← Business Logic
├─────────────────────────────────────────┤
│    Repository Layer (Repositories)      │  ← Data Access
├─────────────────────────────────────────┤
│      Database Layer (SQLAlchemy)        │  ← ORM
└─────────────────────────────────────────┘
```

**Преимущества подхода:**

- ✅ Разделение ответственности (Separation of Concerns)
- ✅ Легкое тестирование каждого слоя
- ✅ Возможность замены компонентов без изменения других слоев
- ✅ Масштабируемость кода

### Frontend Architecture (Component-Based)

```
┌─────────────────────────────────────────┐
│         Views (Pages)                   │  ← Route Components
├─────────────────────────────────────────┤
│         Components                       │  ← Reusable UI
├─────────────────────────────────────────┤
│         Stores (Pinia)                  │  ← State Management
├─────────────────────────────────────────┤
│         Services (API)                  │  ← HTTP Client
└─────────────────────────────────────────┘
```

### Data Flow (Client-Server)

```
┌──────────┐         ┌─────────┐         ┌──────────┐         ┌──────────┐
│  Vue.js  │ ──────> │  Nginx  │ ──────> │  FastAPI │ ──────> │  SQLite  │
│ Frontend │ <────── │  Proxy  │ <────── │  Backend │ <────── │    DB    │
└──────────┘  HTTPS  └─────────┘   HTTP  └──────────┘   SQL   └──────────┘
```

### Docker Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Docker Host                          │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │
│  │   Nginx      │  │   Frontend   │  │   Backend   │ │
│  │ (Port 80/443)│  │  (Vue.js)    │  │  (FastAPI)  │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬──────┘ │
│         │                 │                  │         │
│         └─────────────────┴──────────────────┘         │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │           Docker Network (fashop_network)        │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
│  ┌──────────────┐                                     │
│  │   Certbot    │  (SSL Certificate Renewal)          │
│  └──────────────┘                                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🧪 Тестирование

### Backend тесты (pytest)

```bash
cd backend
pytest
```

### Frontend тесты (Vitest)

```bash
cd frontend
npm run test
```

### API тестирование (Postman)

---


<div align="center">


[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Otmorojeni)

</div>