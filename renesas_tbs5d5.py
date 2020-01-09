from base import *
from devices import *

import uplinker.uplinker as uplinker

class Renesas_TBS5D5(Board):

    @staticmethod
    def match(dev):
        # SEGGER JLink Plus, replace with storage usb VID & PID
        return dev["vid"] =="1366" and dev["pid"]=="0101"
        # return dev["vid"] =="0403" and dev["pid"]=="6001"

    def _exe_jlink_script(self, jlink_script_content):
        jlink_script = fs.get_tempfile(jlink_script_content)
        res, out,err = proc.runcmd("jlinkexe", "-If", "swd", "-device", "R7FS5D57C", "-speed", "4000", "-autoconnect", "1", "-CommanderScript", jlink_script)
        fs.del_tempfile(jlink_script)
        return out

    
    def reset(self):
        self._exe_jlink_script('r\nexit')
    
    def burn(self,bin,outfn=None):
        vm_bin = fs.get_tempfile(bin)
        out = self._exe_jlink_script('loadbin "' + vm_bin + '", 0x0\nr\nexit')
        fs.del_tempfile(vm_bin)

        for line in out.split('\n'):
            if 'O.K.' in line:
                break
        else:
            return False, out

        return True,out

