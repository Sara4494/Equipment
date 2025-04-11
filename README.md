# API Documentation

## Base URL
`https://sara545.pythonanywhere.com`

## Authentication

### Register a new user
**Endpoint**: `POST /user/register/`

**Request Body**:
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "phone": "string",
    "governorate": "string",
    "city": "string",
    "user_type": "worker|contractor|equipment_owner",
    "worker_specialization": "string (required if user_type=worker)",
    "profile_image": "file",
    "password": "string",
    "password_confirmation": "string",
    "price": "number (optional)"
}
```

**Response**:
```json
{
    "email": "string",
    "user_type": "string",
    "first_name": "string",
    "last_name": "string",
    "profile_image": "string (URL)",
    "token": "string",
    "message": "string",
    "worker_specialization": "string (if user_type=worker)"
}
```

### Login
**Endpoint**: `POST /user/login/`

**Request Body**:
```json
{
    "email": "string",
    "password": "string"
}
```

**Response**:
```json
{
    "token": "string",
    "user_type": "string",
    "email": "string"
}
```

### Get Profile Image
**Endpoint**: `GET /user/profile-image/`

**Headers**:
```
Authorization: Token <your_token>
```

**Response**:
```json
{
    "profile_image": "string (URL)"
}
```

## User Management

### List Workers
**Endpoint**: `GET /user/workers/`

**Response**:
```json
[
    {
        "first_name": "string",
        "last_name": "string",
        "price": "number",
        "governorate": "string",
        "city": "string",
        "worker_specialization": "string",
        "profile_image": "string (URL)"
    }
]
```

## Equipment Management

### List Equipment Categories
**Endpoint**: `GET /equipment/categories/`

**Response**:
```json
[
    {
        "id": "number",
        "name": "string",
        "image": "string (URL)"
    }
]
```

### Get Equipment by Category
**Endpoint**: `GET /equipment/categories/<category_id>/equipments/`

**Response**:
```json
[
    {
        "id": "number",
        "name": "string",
        "price": "number",
        "description": "string",
        "image": "string (URL)",
        "category": "number"
    }
]
```

### Create Equipment (Equipment Owners only)
**Endpoint**: `POST /equipment/equipments/create/`

**Headers**:
```
Authorization: Token <your_token>
```

**Request Body**:
```json
{
    "name": "string",
    "price": "number",
    "description": "string",
    "image": "file",
    "category": "number"
}
```

**Response**:
```json
{
    "id": "number",
    "name": "string",
    "price": "number",
    "description": "string",
    "image": "string (URL)",
    "category": "number"
}
```

## Construction Management

### List Construction Categories
**Endpoint**: `GET /construction/categories_construction/`

**Response**:
```json
[
    {
        "id": "number",
        "name": "string",
        "image": "string (URL)"
    }
]
```

### List All Construction Projects
**Endpoint**: `GET /construction/construction_list/`

**Response**:
```json
[
    {
        "id": "number",
        "name": "string",
        "price": "number",
        "description": "string",
        "image": "string (URL)",
        "category": "number"
    }
]
```

## Models Reference

### User Model
```javascript
{
    "email": "string (unique)",
    "phone": "string",
    "governorate": "string",
    "city": "string",
    "user_type": "worker|contractor|equipment_owner",
    "worker_specialization": "string (optional)",
    "profile_image": "string (URL)",
    "first_name": "string",
    "last_name": "string",
    "price": "number (optional)"
}
```

### Equipment Model
```javascript
{
    "owner": "number (user ID)",
    "name": "string",
    "price": "number",
    "description": "string",
    "image": "string (URL)",
    "category": "number"
}
```

### Construction Model
```javascript
{
    "name": "string",
    "price": "number",
    "description": "string",
    "image": "string (URL)",
    "category": "number"
}
```

## Enumerations

### User Types
```javascript
[
    {"value": "worker", "label": "عامل"},
    {"value": "contractor", "label": "مقاول"},
    {"value": "equipment_owner", "label": "صاحب معدات"}
]
```

### Worker Specializations
```javascript
[
    {"value": "plumbing", "label": "عامل سباكة"},
    {"value": "carpentry", "label": "عامل نجارة"},
    {"value": "blacksmith", "label": "عامل حدادة"},
    {"value": "electrician", "label": "عامل كهرباء"},
    {"value": "plaster", "label": "عامل محارة"},
    {"value": "painter", "label": "عامل نقاشة"}
]
```