from path import path
d = path("D:/NicKLz/Pictures")
files = d.walkfiles("*.zip")
for file in files:
    file.remove()
    print('Removed {} file'.format(file))
