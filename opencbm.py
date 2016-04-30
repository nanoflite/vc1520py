from ctypes import *
from ctypes.util import find_library

# Configure function calls.
#
opencbm = cdll.LoadLibrary(find_library('opencbm'))

# 1. open
opencbm.cbm_driver_open.argtypes = [c_void_p, c_int]
opencbm.cbm_driver_open.restype = c_int

# 2. close
opencbm.cbm_driver_close.argtypes = [c_void_p]

# 3. lock
opencbm.cbm_lock.argtypes = [c_void_p]

# 4. unlock
opencbm.cbm_unlock.argtypes = [c_void_p]

# 5. open
opencbm.cbm_open.argtypes = [c_void_p, c_ubyte, c_ubyte, c_void_p, c_size_t]
opencbm.cbm_open.restype = c_int

# 6. close
opencbm.cbm_close.argtypes = [c_void_p, c_ubyte, c_ubyte]
opencbm.cbm_close.restype = c_int

# 7. listen
opencbm.cbm_listen.argtypes = [c_void_p, c_ubyte, c_ubyte]
opencbm.cbm_listen.restype = c_int

# 8. unlisten
opencbm.cbm_unlisten.argtypes = [c_void_p]
opencbm.cbm_unlisten.restype = c_int

# 9. write
opencbm.cbm_raw_write.argtypes = [c_void_p, c_void_p, c_size_t]
opencbm.cbm_raw_write.restype = c_int

# 10. reset
opencbm.cbm_reset.argtypes = [c_void_p]
opencbm.cbm_reset.restype = c_int

# 10. to petscii
opencbm.cbm_ascii2petscii.argtypes = [c_char_p]
opencbm.cbm_ascii2petscii.restype = c_char_p\

def cbm_open_driver():
    fp = c_void_p()
    i = opencbm.cbm_driver_open(byref(fp), 0)
    if i == 0:
        return fp
    return None

def cbm_close_driver(handle):
    opencbm.cbm_driver_close(handle)

def cbm_lock(handle):
    opencbm.cbm_lock(handle)

def cbm_unlock(handle):
    opencbm.cbm_unlock(handle)

def cbm_open(handle, dev, secadr, name):
    fname = create_string_buffer(name)
    return opencbm.cbm_open(handle, dev, secadr, fname, len(fname))

def  cbm_close(handle, dev, secadr):
    return opencbm.cbm_close(handle, dev, secadr)

def cbm_listen(handle, dev, secadr):
    return opencbm.cbm_listen(handle, dev, secadr)

def cbm_unlisten(handle):
    return opencbm.cbm_unlisten(handle)

def cbm_write(handle, data):
    fdata = create_string_buffer(data)
    return opencbm.cbm_raw_write(handle, fdata, len(fdata))

def cbm_reset(handle):
    return opencbm.cbm_reset(hanlde)

def cbm_to_petscii(text):
    return opencbm.cbm_ascii2petscii(text)

