#COINES_INSTALL_PATH ?= ../../../..
COINES_INSTALL_PATH ?= /home/pi/COINES/v2.6.0

EXAMPLE_FILE ?= sensor_data.c

API_LOCATION ?= ../..

C_SRCS += \
$(API_LOCATION)/bmp2.c \
../common/common.c

INCLUDEPATHS += \
$(API_LOCATION) \
../common

include $(COINES_INSTALL_PATH)/coines.mk
