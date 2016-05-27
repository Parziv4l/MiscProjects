from path import path
d = path("D:/NicKLz/Downloads")
files = d.walkfiles("*.exe")
for file in files:
    file.remove()
    print "Removed {} file".format(file)
