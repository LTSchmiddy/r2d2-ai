import ctypes

# r2d2_core = ctypes.LibraryLoader("./build/x64-windows-Debug/bin/r2d2_core").LoadLibrary()
# r2d2_core = ctypes.LibraryLoader(ctypes.CDLL).LoadLibrary("../build/x64-windows-Debug/bin/r2d2_core")

r2d2_core = ctypes.CDLL('../build/x64-windows-Debug/bin/r2d2_core')

r2d2_core.test_fn()