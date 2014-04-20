#TARGET = jolla_sensorgestures_plugin
TARGET = qtsensorgestures_plugin

QT += core sensors
DESTDIR = build
PLUGIN_TYPE = sensorgestures
load(qt_plugin)

# Input
HEADERS += qtsensorgestureplugin.h \
    qcoversensorgesturerecognizer.h \
    qdoubletapsensorgesturerecognizer.h \
    qhoversensorgesturerecognizer.h \
    qfreefallsensorgesturerecognizer.h \
    qpickupsensorgesturerecognizer.h \
    qshakerecognizer.h \
    qslamgesturerecognizer.h \
    qturnoversensorgesturerecognizer.h \
    qtwistsensorgesturerecognizer.h \
    qwhipsensorgesturerecognizer.h \
    qtsensorgesturesensorhandler.h

SOURCES += qtsensorgestureplugin.cpp \
    qcoversensorgesturerecognizer.cpp \
    qdoubletapsensorgesturerecognizer.cpp \
    qhoversensorgesturerecognizer.cpp \
    qfreefallsensorgesturerecognizer.cpp \
    qpickupsensorgesturerecognizer.cpp \
    qshakerecognizer.cpp \
    qslamgesturerecognizer.cpp \
    qturnoversensorgesturerecognizer.cpp \
    qtwistsensorgesturerecognizer.cpp \
    qwhipsensorgesturerecognizer.cpp \
    qtsensorgesturesensorhandler.cpp

OTHER_FILES += \
    plugin.json
