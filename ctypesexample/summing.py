import ctypes
import numpy
import pathlib

# find the shared library, the path depends on the platform and Python version
libfile = pathlib.Path(__file__).parent / "csumlib.so"
csumlib = ctypes.CDLL(str(libfile))


csumlib.csum.restype = ctypes.c_longlong
csumlib.csum.argtypes = [ctypes.c_int, numpy.ctypeslib.ndpointer(dtype=numpy.int32)]
def csum(f: int, a: numpy.ndarray) -> int:
    return csumlib.csum(f,a)
