https://nesi.github.io/perf-training/python-scatter/ctypes

python .\setup.py build --force --verbose



#include <Python.h>

//https://stackoverflow.com/questions/34689210/error-exporting-symbol-when-building-python-c-extension-in-windows
//void PyInit_csum() {}

// PyMODINIT_FUNC PyInit_csum(void) {
//     // do stuff...
// }