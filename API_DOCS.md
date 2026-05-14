# Driver Management API Documentation

## Overview

A REST API for managing drivers, vehicles, routes, and packages. Built with Flask and backed by PostgreSQL.

- **Base URL:** `http://localhost:5000`
- **Content-Type:** `application/json`
- **Authentication:** None

---

## Health Check

### `GET /`

Returns server status.

**Response**
```json
{ "message": "server online" }
```

---

## Drivers

### `GET /driver/`

Returns all drivers.

**Response `200`**
```json
[
  {
    "driver_id": 1,
    "name": "Jane Smith",
    "license_type": "CDL-A"
  }
]
```

---

### `POST /driver/`

Creates a new driver.

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Driver's full name |
| `license_type` | string | Yes | License class (e.g. `CDL-A`, `CDL-B`) |

```json
{
  "name": "Jane Smith",
  "license_type": "CDL-A"
}
```

**Response `201`**
```json
{ "message": "object created" }
```

---

### `PUT /driver/<id>`

Updates an existing driver by ID.

**Path Parameter:** `id` — integer driver ID

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Driver's full name |
| `license_type` | string | Yes | License class |

```json
{
  "name": "Jane Smith",
  "license_type": "CDL-B"
}
```

**Response `201`**
```json
{ "message": "object updated" }
```

---

### `DELETE /driver/<id>`

Deletes a driver by ID.

**Path Parameter:** `id` — integer driver ID

**Response `201`**
```json
{ "message": "object updated" }
```

---

## Vehicles

### `GET /vehicle/`

Returns all vehicles.

**Response `200`**
```json
[
  {
    "vehicle_id": 1,
    "license_plate": "ABC-1234",
    "model": "Ford Transit",
    "driver_id": 1
  }
]
```

---

### `POST /vehicle/`

Creates a new vehicle.

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Vehicle model name |
| `license_plate` | string | Yes | License plate number |
| `driver_id` | integer | Yes | ID of the assigned driver |

```json
{
  "model": "Ford Transit",
  "license_plate": "ABC-1234",
  "driver_id": 1
}
```

**Response `201`**
```json
{ "message": "object created" }
```

> **Note:** Each driver can only be assigned to one vehicle (`driver_id` is unique).

---

### `PUT /vehicle/<id>`

Updates an existing vehicle by ID.

**Path Parameter:** `id` — integer vehicle ID

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Vehicle model name |
| `license_plate` | string | Yes | License plate number |
| `driver_id` | integer | Yes | ID of the assigned driver |

```json
{
  "model": "Chevy Express",
  "license_plate": "XYZ-5678",
  "driver_id": 2
}
```

**Response `201`**
```json
{ "message": "object updated" }
```

---

### `DELETE /vehicle/<id>`

Deletes a vehicle by ID.

**Path Parameter:** `id` — integer vehicle ID

**Response `201`**
```json
{ "message": "object updated" }
```

---

## Routes

### `GET /routes/`

Returns all routes.

**Response `200`**
```json
[
  {
    "route_id": 1,
    "service_zone": "North District",
    "date": "2026-05-14",
    "driver_id": 1
  }
]
```

---

### `POST /routes/`

Creates a new route.

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date` | date | Yes | Route date (`YYYY-MM-DD`) |
| `service_zone` | string | Yes | Zone or area name |
| `driver_id` | integer | Yes | ID of the assigned driver |

```json
{
  "date": "2026-05-14",
  "service_zone": "North District",
  "driver_id": 1
}
```

**Response `201`**
```json
{ "message": "object created" }
```

---

### `PUT /routes/<id>`

Updates an existing route by ID.

**Path Parameter:** `id` — integer route ID

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date` | date | Yes | Route date (`YYYY-MM-DD`) |
| `service_zone` | string | Yes | Zone or area name |
| `driver_id` | integer | Yes | ID of the assigned driver |

```json
{
  "date": "2026-05-15",
  "service_zone": "South District",
  "driver_id": 2
}
```

**Response `201`**
```json
{ "message": "object updated" }
```

---

### `DELETE /routes/<id>`

Deletes a route by ID.

**Path Parameter:** `id` — integer route ID

**Response `201`**
```json
{ "message": "object updated" }
```

---

## Packages

### `GET /packages/`

Returns all packages.

**Response `200`**
```json
[
  {
    "package_id": 1,
    "description": "Electronics - fragile",
    "weight": 5,
    "route_id": 1
  }
]
```

---

### `POST /packages/`

Creates a new package.

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `weight` | integer | Yes | Package weight |
| `description` | string | Yes | Package description (max 75 chars) |
| `route_id` | integer | Yes | ID of the assigned route |

```json
{
  "weight": 5,
  "description": "Electronics - fragile",
  "route_id": 1
}
```

**Response `201`**
```json
{ "message": "object created" }
```

---

### `PUT /packages/<id>`

Updates an existing package by ID.

**Path Parameter:** `id` — integer package ID

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `weight` | integer | Yes | Package weight |
| `description` | string | Yes | Package description (max 75 chars) |
| `route_id` | integer | Yes | ID of the assigned route |

```json
{
  "weight": 10,
  "description": "Clothing",
  "route_id": 2
}
```

**Response `201`**
```json
{ "message": "object updated" }
```

---

### `DELETE /packages/<id>`

Deletes a package by ID.

**Path Parameter:** `id` — integer package ID

**Response `201`**
```json
{ "message": "object delete" }
```

---

## Data Models

### Driver
| Column | Type | Constraints |
|--------|------|-------------|
| `driver_id` | SERIAL | PRIMARY KEY |
| `name` | VARCHAR(50) | NOT NULL |
| `license_type` | VARCHAR(50) | NOT NULL |

### Vehicle
| Column | Type | Constraints |
|--------|------|-------------|
| `vehicle_id` | SERIAL | PRIMARY KEY |
| `license_plate` | VARCHAR(50) | NOT NULL |
| `model` | VARCHAR(50) | NOT NULL |
| `driver_id` | INT | FK → driver, UNIQUE |

### Route
| Column | Type | Constraints |
|--------|------|-------------|
| `route_id` | SERIAL | PRIMARY KEY |
| `service_zone` | VARCHAR(50) | NOT NULL |
| `date` | DATE | |
| `driver_id` | INT | FK → driver |

### Package
| Column | Type | Constraints |
|--------|------|-------------|
| `package_id` | SERIAL | PRIMARY KEY |
| `description` | VARCHAR(75) | NOT NULL |
| `weight` | INT | NOT NULL |
| `route_id` | INT | FK → route |

### Relationships
```
driver ──< route ──< package
driver ──── vehicle  (1-to-1)
```

---

## Error Responses

All endpoints return a JSON error object on failure.

```json
{ "error": "<error message>" }
```

---

## Quick Reference

| Resource | GET | POST | PUT | DELETE |
|----------|-----|------|-----|--------|
| Drivers | `GET /driver/` | `POST /driver/` | `PUT /driver/<id>` | `DELETE /driver/<id>` |
| Vehicles | `GET /vehicle/` | `POST /vehicle/` | `PUT /vehicle/<id>` | `DELETE /vehicle/<id>` |
| Routes | `GET /routes/` | `POST /routes/` | `PUT /routes/<id>` | `DELETE /routes/<id>` |
| Packages | `GET /packages/` | `POST /packages/` | `PUT /packages/<id>` | `DELETE /packages/<id>` |
