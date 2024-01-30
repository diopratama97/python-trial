# data satuan integer
data_integer = 1
print(type(data_integer))
print("data :", data_integer,",","tipe data :", type(data_integer))

# data angka dengan koma : float
data_float = 1.5
print(type(data_float))
print("data :", data_float,",","tipe data :", type(data_float))

# data karakter : string
data_string = "babang tamvan"
print(type(data_string))
print("data :", data_string,",","tipe data :", type(data_string))

# data biner true/false : boolean
data_biner = False
print(type(data_biner))
print("data :", data_biner,",","tipe data :", type(data_biner))

# tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print(type(data_complex))
print("data :", data_complex,",","tipe data :", type(data_complex))

# tipe data dari bahasa C. bisa dipakai karena phyton dibuat dengan bahasa C
from ctypes import c_double #import library ctypes
data_c_double = c_double(10.5)
print("data :", data_c_double,",","tipe data :", type(data_c_double))