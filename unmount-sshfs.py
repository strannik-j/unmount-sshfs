#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  unmount-sshfs.py
#
#  Copyright 2011 Strannik-j <mail@strannik-j.org>
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  * All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#
#		This product includes software developed by a Bessonov Jurij  
#		aka Strannik-j (http://strannik-j.org) and his contributors.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import commands

def process_num(process=''):
    return commands.getoutput('ps aux| grep %s | grep -v grep | grep -v python' % process)

def create_list(str0):
    list0 = []
    x = ''
    for i in str0:

        if i != '\n':
            x += i
        else:
            list0.append(x)
            x = ''
    list0.append(x)
    return list0
    
def main():
    name = 'sshfs'
    proc_list_str = process_num(name)
    proc_list = create_list(proc_list_str)
    for i in proc_list:
        ch0 = 0
        name_index = i.find(name)
        index0 = i.find(' ', name_index + 6, -1)
        index1 = i.find(' ', index0 + 1, -1)
        path0 = i[index0:index1]
        print 'unmount ', path0
        out = commands.getoutput('fusermount -u -z %s' % path0)
        if out == '':
            print 'done'
        else:
            print 'error: ', out
    return 0

if __name__ == '__main__':
    main()

