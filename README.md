# API

## normalize_headers(headers)

Normalizes CSV header names.

### **Parameters**

- headers (list of strings): raw header names

### **Returns**

- list of strings: normalized header names

### **Behavior**

- trims leading/trailing whitespace
- converts to lowercase
- replaces spaces with underscores

### **Does not**

- validate CSV files
- remove duplicate headers
- infer data types
