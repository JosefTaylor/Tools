#This tool converts points of the compass to azimuth in degrees. It's useful for interpreting weather data.
# Josef Taylor, 2014-09-19

dictcomPoint2Dirs = {
    'N'   : 348.75,
    'NNE' : 11.25,
    'NE'  : 33.75,
    'ENE' : 56.25,
    'E'   : 78.75,
    'ESE' : 101.25,
    'SE'  : 123.75,
    'SSE' : 146.25,
    'S'   : 168.75,
    'SSW' : 191.25,
    'SW'  : 213.75,
    'WSW' : 236.25,
    'W'   : 258.75,
    'WNW' : 281.25,
    'NW'  : 303.75,
    'NNW' : 326.25,
}


def replace_all(name, dictcomPoint2Dirs):
    for comPoint, direction in dictcomPoint2Dirs.iteritems():
        name = name.replace(comPoint, direction)
    return name

try:
    with open('new_output.txt', 'w') as new_file:
        with open('test_file.txt', 'r') as f:
            for line in f:
                new_line = replace_all(line, dictcomPoint2Dirs)
                new_file.write(new_line)
except:
    print "Can't open file!"


