
# Motherboard Orchestra
Motherboard Orchestra is my bodged-together brainchild from a solo hackathon project undertaken during the 2024 Hack Sussex hackathon. However, it remains a rather low-priority work in progress as I fell asleep mid-hackathon, possibly due to a lack of caffeine, missing about 9 hours of the 24
hour hackathon...

This ReadMe serves as a brief overview of my journey over those 15 hours...
## Concept
The idea behind Motherboard Orchestra was to develop an application that links a 'composer' (server) computer to several 'instrument' (client) computers to perform a musical piece.

The composer receives a MIDI file, distributing instructions to all connected clients to play the song.

Here's the kicker: the music isn't played through conventional speakers, but instead through the buzzers nestled on the clients' motherboards.

## Implementation
During the limited time I had, I managed to set up the basic framework for communication between the composer and the client computers, as well as create GUIs for both the clients and composer. 
The composer can receive a MIDI file, check the number of clients required for a song to be played, and display the number of clients connected.
All of my efforts after this point were solely dedicated to getting a noise to play from a computer, which was oddly difficult

### Adapting the plan
As it turns out, many computers nowadays don't have buzzers integrated into their motherboards. I'm not too sure when the collective descision was made to stop our computers from beeping, but it resulted in a rather devastating 'oh dear.' when I realised the _none_ of the computers 
I had access to during the hackathon, (Desktop or Laptop) had a buzzer.

I resorted to generating buzzing noises through the clients' speakers instead, sacrificing one of the project's main attractions.

### Frequency & Pitch?
My attempts to create the buzzing noise from the client's speakers didn't fare much better than using the motherboard buzzers.

It turns out that there is an unusual lack of Python libraries which are able to precisely control both the pitch _and_ timing of a generated Wave.
_I salute anyone who has made a full-on synthesizer using Python, because I was barely able to get something to buzz._


## Lessons Learned
- Making a small client-server network is pretty easy with Python.
- Know when to drop a project that isn't going to work.
- Know your hardware!
- Don't fall asleep during a hackathon.
- Experimentation takes a surprising amount of time.

## Future Work
I'm probably not going to continue work on this project, unless I have a seriously large amount of free time. It was doomed from the start.


