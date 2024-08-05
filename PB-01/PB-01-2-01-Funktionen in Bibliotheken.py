#==========================================================================
#
# PB-01-2-01-Funktionen in Bibliotheken.py
#
# (keine Bauteile)
#
#==========================================================================
#
help('modules')

print("-----------------------------------------------------------")

import ujson;print("Funktionen von ujson: ");print(dir(ujson)),print()
import neopixel;print("Funktionen von neopixel: ");print(dir(neopixel)),print()
import umachine;print("Funktionen von umachine: ");print(dir(umachine)),print()
import micropython;print("Funktionen von micropython: ");print(dir(micropython)),print()
import onewire;print("Funktionen von onewire: ");print(dir(onewire)),print()
import ds18x20;print("Funktionen von ds18x20: ");print(dir(ds18x20)),print()
import utime;print("Funktionen von utime: ");print(dir(utime)),print()
import urandom;print("Funktionen von urandom: ");print(dir(urandom)),print()
import dht;print("Funktionen von dht: ");print(dir(dht)),print()


"""
Der erste Befehl help('modules') zeigt eine Liste aller auf dem System verfügbaren Module an.
Die help()-Funktion gibt eine kurze Beschreibung jedes Moduls, einschließlich der Version und
des Autors, sowie eine Liste der in dem Modul enthaltenen Funktionen zurück.

Die nächsten Zeilen zeigen den Import von verschiedenen Modulen und den Aufruf der
dir()-Funktion, um alle Funktionen aufzulisten, die im jeweiligen Modul enthalten sind.
dir() gibt eine Liste der Namen aller in dem angegebenen Objekt (in diesem Fall einem
Modul) definierten Namen zurück. Diese Liste enthält auch spezielle Namen, die von Python
definiert sind und nicht für den Benutzer gedacht sind.

Durch den Import von Modulen und das Anzeigen der enthaltenen Funktionen können Sie
untersuchen, welche Funktionalität für Ihre Anwendungen verfügbar ist und wie Sie sie
nutzen können. Wenn Sie zum Beispiel ein Programm schreiben möchten, das auf den
Temperatursensor DS18B20 zugreift, können Sie das Modul onewire und ds18x20
importieren und die enthaltenen Funktionen wie onewire.onewire() und ds18x20.DS18X20()
verwenden.

Das Ausführen des Codes gibt eine Liste der aufgelisteten Module sowie alle darin
enthaltenen Funktionen aus.


>>> %Run -c $EDITOR_CONTENT
__main__          framebuf          uasyncio/funcs    ujson
_boot             gc                uasyncio/lock     umachine
_boot_fat         math              uasyncio/stream   uos
_onewire          micropython       ubinascii         urandom
_rp2              neopixel          ucollections      ure
_thread           onewire           ucryptolib        uselect
_uasyncio         rp2               uctypes           ustruct
builtins          uarray            uerrno            usys
cmath             uasyncio/__init__ uhashlib          utime
dht               uasyncio/core     uheapq            uzlib
ds18x20           uasyncio/event    uio
Plus any modules on the filesystem
-----------------------------------------------------------
Funktionen von ujson: 
['__class__', '__name__', 'dump', 'dumps', 'load', 'loads']

Funktionen von neopixel: 
['__class__', '__name__', '__file__', 'bitstream', 'NeoPixel']

Funktionen von umachine: 
['__class__', '__name__', 'ADC', 'I2C', 'I2S', 'PWM', 'PWRON_RESET', 'Pin', 'RTC', 'SPI', 'Signal', 'SoftI2C', 'SoftSPI', 'Timer', 'UART', 'WDT', 'WDT_RESET', 'bitstream', 'bootloader', 'deepsleep', 'disable_irq', 'enable_irq', 'freq', 'idle', 'lightsleep', 'mem16', 'mem32', 'mem8', 'reset', 'reset_cause', 'soft_reset', 'time_pulse_us', 'unique_id']

Funktionen von micropython: 
['__class__', '__name__', 'const', 'alloc_emergency_exception_buf', 'heap_lock', 'heap_unlock', 'kbd_intr', 'mem_info', 'opt_level', 'qstr_info', 'schedule', 'stack_use']

Funktionen von onewire: 
['__class__', '__name__', '__file__', 'OneWireError', 'OneWire', '_ow']

Funktionen von ds18x20: 
['__class__', '__name__', 'const', '__file__', 'DS18X20']

Funktionen von utime: 
['__class__', '__name__', 'gmtime', 'localtime', 'mktime', 'sleep', 'sleep_ms', 'sleep_us', 'ticks_add', 'ticks_cpu', 'ticks_diff', 'ticks_ms', 'ticks_us', 'time', 'time_ns']

Funktionen von urandom: 
['__class__', '__init__', '__name__', 'choice', 'getrandbits', 'randint', 'random', 'randrange', 'seed', 'uniform']

Funktionen von dht: 
['__class__', '__name__', '__file__', 'dht_readinto', 'sys', 'DHTBase', 'DHT11', 'DHT22']

>>> 

"""