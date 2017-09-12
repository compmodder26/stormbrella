#!/bin/bash

#ifdown wlan0
rm /etc/network/interfaces && ln -s /etc/network/interfaces.stormbrella /etc/network/interfaces
#ifup wlan0

rm /etc/rc.local && ln -s /etc/rc.local.stormbrella /etc/rc.local

#update-rc.d nginx enable
#update-rc.d hostapd enable
#update-rc.d dnsmasq enable
