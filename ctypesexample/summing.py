import ctypes
import numpy
import pathlib

# find the shared library, the path depends on the platform and Python version
libfile = pathlib.Path(__file__).parent / "csumlib.so"
csumlib = ctypes.CDLL(str(libfile))

type_vec = ctypes.POINTER(ctypes.c_double * 3)

csumlib.csum.restype = ctypes.c_longlong
csumlib.csum.argtypes = [ctypes.c_int, numpy.ctypeslib.ndpointer(dtype=numpy.int32)]
def csum(f: int, a: numpy.ndarray) -> int:
    return csumlib.csum(f,a)


csumlib.add.restype = type_vec
csumlib.add.argtypes = [type_vec, type_vec]
def add(a: list, b: list) -> list:
    a_p = (ctypes.c_double * 3)(*a) 
    b_p = (ctypes.c_double * 3)(*b) 
    r_p = csumlib.add(a_p,b_p)
    print(r_p.contents)
    return [l for l in r_p.contents]
