# 🧩 Pointer Table - Python Pointer Simulator

A lightweight Python library to **simulate C-style pointers in Python**.  
It allows you to store Python objects and retrieve them later using short hexadecimal IDs. Perfect for debugging, experimental projects, or building advanced libraries that need object references.

> **Unlike Python's normal references, this library gives you a manual pointer-like system.**

---

## 🚀 Features

- Store any Python object and get a short **hex ID**  
- Retrieve objects later using their hex ID  
- Easy-to-use functions with simple interface  
- Minimal dependencies, pure Python  
- Perfect for **experimental memory manipulation** or advanced library development  

---

## 📸 Usage Example

```python
from pointer_table import store, retrieve

my_list = [1, 2, 3]

# Store the object and get a pointer
ptr = store(my_list)
print(ptr)              # e.g., 0xABCDE

# Retrieve the object later
retrieved_list = retrieve(ptr)
print(retrieved_list)   # [1, 2, 3]
```
<img width="2920" height="1027" alt="image" src="https://github.com/user-attachments/assets/bc28aa4d-1d4f-4b66-bfe5-a4224e82c3f2" />

---

## 📦 Installation

```bash
cd your-project-path
git clone https://github.com/Exoo25/pointer_lib/
```

>⚠️ **Important:**  
> - The hex ID is generated using only the lower 20 bits of Python's `id()`, so collisions are **possible** if many objects are stored.  
> - Designed for experimentation, not for production memory management.

---

## 📄 Functions

### `store(obj)`

Stores a Python object and returns a short hex ID.  

**Args:**  
- `obj`: Any Python object to store  

**Returns:**  
- `str`: Hexadecimal ID, e.g., `"0xABCDE"`

---

### `retrieve(obj_id_hex)`

Retrieves a Python object using its hex ID.  

**Args:**  
- `obj_id_hex (str)`: Hex string returned by `store()`  

**Returns:**  
- The stored Python object  

**Raises:**  
- `KeyError` if no object exists for the given ID  

---

## 📜 Change Logs

> - [07/02/2026 10:30AM] Initial release of `pointer_lib`  

---
```
