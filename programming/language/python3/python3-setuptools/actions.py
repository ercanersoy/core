# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="setuptools-%s" % get.srcVERSION()

    
def install():
    pisitools.dosed("setuptools/command/easy_install.py", "env python", "env python3")
    
    pythonmodules.run("bootstrap.py", pyVer="3")
    pythonmodules.install(pyVer = "3")
    
    #avoid python-setuptools conflict
    #pisitools.removeDir("/usr/share")