APPNAME='CrFonts'
VERSION=0.5
LICENSE='ofl.txt'
COPYRIGHT="Charin Jamjitt. All rights reserved."
TEXTSIZE=20

for f in ('Udom',) :
    font(target = "Cr-"+f+".ttf",
         source = "source/masters/Cr-"+f+".ufo",
         graphite = gdl('source/'+f+'.gdl',
                        master="source/lanna.gdl",
                        make_params="-l lastcomp --autodefines",
                        params="-v2 -d -q"),
         license = ofl(f),
         copyright = COPYRIGHT,
         ap = 'source/'+f+'.xml',
         #ap_params = '-e "L=LD;U=UD;UR=URD"',       # LR != LRD
         #opentype = fea(create("srcs/{}.fea".format(f), cmd("psfmakefea -i ${SRC[2]} -c ${SRC[1]} -o ${TGT} ${SRC[0]}",
         #                                                   ['source/{}.xml'.format(f), 'source/khun_classes.xml', 'source/khun.feap'])),
         #               no_make=1),
#         woff = woff(),
         fret = fret(),
         version = VERSION,
         script = 'lana',
         classes = 'source/lanna_classes.xml')

