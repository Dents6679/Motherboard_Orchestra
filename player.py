import asyncio

import music21 as m21
import winsound
import time
from audioplayer import AudioPlayer
import pysine

"""
    This code is ran on the client and plays the monophonic midi file.
    
    The encoding for the client looks like this:
    list of (frequency in hz, duration in ms, timing from start in ms)
    these tuples are called buzz_event from here. 
"""


def play_monophonic_midi(buzz_events):

    for buzz_event in buzz_events:
        frequency, duration, timing = buzz_event
        print(f"Playing buzz event of frequency {frequency} hz, duration {duration} ms, and timing {timing} ms.")
        winsound.Beep(frequency, duration)
        time.sleep(timing/1000)




winsound.Beep(370, 500)
winsound.Beep(440, 250)
winsound.Beep(554, 500)
winsound.Beep(440, 500)
winsound.Beep(370, 250)
winsound.Beep(293, 125)
winsound.Beep(293, 125)
winsound.Beep(293, 125)
print("Playing...")



