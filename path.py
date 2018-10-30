#-*-coding:iso-8859-1-*-
"""
_cmd is an import, wich alowes, to make commands from cmdline and
get the output back in pythonfile
"""
def cout(cmd=""):
    """is the only attribute from _cmd, wich get the output
    from cmdline and send it back to pythonfile
    """
    from subprocess import Popen as op, PIPE as pi
    if cmd=="":
        return None
    else:
        liste=cmd.split(" ")
        r=op(liste,stdout=pi,stderr=pi,stdin=pi)
        t,p=r.communicate()
        return str(t,"iso8859_2")
