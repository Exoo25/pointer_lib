# pointer_table.py (or __init__.py)

pointer_table = {}


class InvalidPointerError(Exception):
    pass


def store(obj):
    """
    Stores a Python object in the pointer table and returns a short hex ID.
    """
    obj_id = id(obj) & 0xFFFFF  # short 20-bit ID
    pointer_table[obj_id] = obj
    return f"0x{obj_id:05X}"


def retrieve(obj_id_hex):
    """
    Retrieves a Python object from the pointer table using its hex ID.
    """
    obj_id = int(obj_id_hex, 16)  # hex -> int

    if obj_id not in pointer_table:
        raise InvalidPointerError(f"Pointer {obj_id_hex} is invalid or freed")

    return pointer_table[obj_id]

def is_valid(ptr_hex):
    """
    Check if a pointer is valid (exists in the pointer table).

    Args:
        ptr_hex (str): The pointer hex string returned by store(), e.g. "0xABCDE"

    Returns:
        bool: True if pointer is valid, False if freed or invalid
    """
    try:
        obj_id = int(ptr_hex, 16)
    except ValueError:
        return False  # invalid hex string

    return obj_id in pointer_table

def free(ptr_hex):
    """
    Free a single pointer.
    """
    obj_id = int(ptr_hex, 16)  # IMPORTANT FIX

    if obj_id not in pointer_table:
        raise InvalidPointerError(
            f"Pointer {ptr_hex} does not exist or is already freed"
        )

    del pointer_table[obj_id]


def free_all():
    """
    Free all pointers.
    """
    pointer_table.clear()
