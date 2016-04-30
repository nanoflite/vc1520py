from opencbm import *

cbm = cbm_open_driver()
cbm_lock(cbm)
cbm_open(cbm, 6, 0, "")
cbm_listen(cbm, 6, 0)
cbm_write(cbm, "@ABC\r")
cbm_unlisten(cbm)
cbm_close(cbm, 6, 0)
cbm_unlock(cbm)
cbm_close_driver(cbm)
