#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file


# set some default output folders (most are already set by default)
DOCDIR = ["documentation", "web"]
STANDARDS = 'tests/reference'

# set the font name and description
DESC_SHORT = "A family of fonts for the Lanna script."
TEXTSIZE = 20


for subfamily in ('Udom',) :
    getufoinfo("source/masters/Cr-" + subfamily + "-Regular" + ".ufo")
    BUILDLABEL="alpha"
    APPNAME = "Cr-fonts" + "-" + subfamily
    #APPNAME = "Cr-fonts"
    #still need a better solution to handle the artefact naming for multiple subfamilies 

    designspace('source/Cr-' + subfamily + '.designspace',
    params = '-l ${DS:FILENAME_BASE}_createinstance.log',
    target = process('${DS:FILENAME_BASE}.ttf'),
         graphite = gdl('source/' + subfamily +'.gdl',
                        master="source/lanna.gdl",
                        make_params="-l lastcomp --autodefines",
                        params="-v2 -d -q"),
         ap = "source/" + '${DS:FILENAME_BASE}.xml',
         #ap_params = '-e "L=LD;U=UD;UR=URD"',       # LR != LRD
         #opentype = fea(create("srcs/{}.fea".format(f), cmd("psfmakefea -i ${SRC[2]} -c ${SRC[1]} -o ${TGT} ${SRC[0]}",
         #                                                   ['source/{}.xml'.format(f), 'source/khun_classes.xml', 'source/khun.feap'])),
         #               no_make=1),
         woff = woff(),
         version = VERSION,
         fret = fret(params="-r -oi"),
         script = 'lana',
         classes = 'source/lanna_classes.xml')
