# belajar casting
# merubah tipe data ke tipe data lain
# tipe data = int, float, str, bool

# INT
print("===INT===")
data_int = 10
print("data :", data_int,",","tipe data :", type(data_int))

data_float = float(data_int) # ubah ke tipe data float
print("data :", data_float,",","tipe data :", type(data_float))

data_str = str(data_int) # ubah ke tipe data str
print("data :", data_str,",","tipe data :", type(data_str))

data_bool = bool(data_int) # ubah ke tipe data bool, akan False jika nilai = 0
print("data :", data_bool,",","tipe data :", type(data_bool))

# FLOAT
print("===FLOAT===")
data_float = 9.8
print("data :", data_float,",","tipe data :", type(data_float))

data_int = int(data_float) # ubah ke tipe data int
print("data :", data_int,",","tipe data :", type(data_int))

data_str = str(data_float) # ubah ke tipe data str
print("data :", data_str,",","tipe data :", type(data_str))

data_bool = bool(data_float) # ubah ke tipe data bool, akan False jika nilai = 0
print("data :", data_bool,",","tipe data :", type(data_bool))

# BOOLEAN
print("===BOOLEAN===")
data_bool = True
print("data :", data_bool,",","tipe data :", type(data_bool))

data_int = int(data_bool) # ubah ke tipe data int
print("data :", data_int,",","tipe data :", type(data_int))

data_str = str(data_bool) # ubah ke tipe data str
print("data :", data_str,",","tipe data :", type(data_str))

data_float = float(data_bool) # ubah ke tipe float
print("data :", data_float,",","tipe data :", type(data_float))

# STRING
print("===STRING===")
data_str = "True"
print("data :", data_str,",","tipe data :", type(data_str))

data_int = int(data_str) # ubah ke tipe data int, string harus angka
print("data :", data_int,",","tipe data :", type(data_int))

data_bool = str(data_str) # ubah ke tipe data bool, jika false harus string kosong
print("data :", data_bool,",","tipe data :", type(data_bool))

data_float = float(data_str) # ubah ke tipe float, string harus angka
print("data :", data_float,",","tipe data :", type(data_float))