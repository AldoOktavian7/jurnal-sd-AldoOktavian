# API Contract - User Profile

## Endpoint Profile

**Endpoint:** `/api/v1/profile`

**Method:** `GET`

### Response Body (JSON)

```json
{
  "id": 1,
  "username": "Aldo Oktavian",
  "email": "aldooktavian93@univ.ac.id",
  "avatar_url": "https://image.com/avatar.png"
}
```

---

## Endpoint Login

**Endpoint:** `/api/v1/login`

**Method:** `POST`

### Request Body (JSON)

```json
{
  "email": "aldooktavian93@univ.ac.id",
  "password": "aldookta123"
}
```

### Response Body (JSON)

```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "abc123xyz"
}
```