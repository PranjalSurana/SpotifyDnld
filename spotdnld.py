'''import subprocess
import sys # for sys.executable (The file path of the currently using python)
from spotdl import __main__ as spotdl # To get the location of spotdl

spotifylink = "https://open.spotify.com/track/0bGJHUPR6ems9tzIljlPFR?si=807e283c0dc84ab3"
subprocess.check_call([sys.executable, spotdl.__file__, spotifylink])'''

import os

files='C:\\Users\\pranj\\Desktop\\spotify.txt'
f = open(files,'r')

os.chdir('C:\\Users\\pranj\\Documents\\PyDnldsYT\\spotify')

i = 1  # Downloaded
nd = 0  # Not Downloaded
for url in f:
    if url!='\n':
        print()
        print(url)
        st = 'spotdl ' + url
        try:
            os.system(st)
            print(str(i) + ' ' + url + 'Done')
            i += 1
        except:
            print(str(i) + ' ' + url + 'Already Downloaded')
            nd += 1