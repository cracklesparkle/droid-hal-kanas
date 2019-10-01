# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device kanas
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Samsung Galaxy Core 2

%define installable_zip 1

%define straggler_files \
/d\
/bugreports\
/cache\
/nonplat_file_contexts\
/nonplat_hwservice_contexts\
/nonplat_property_contexts\
/nonplat_seapp_contexts\
/nonplat_service_contexts\
/plat_file_contexts\
/plat_hwservice_contexts\
/plat_property_contexts\
/plat_seapp_contexts\
/plat_service_contexts\
/sdcard\
/vendor\
/vndservice_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

