# CS5 Black, Lab 4 - hw3pr1
# Filename: hw4pr1.py
# Name: Myles Fabre
# Problem description: Lab 4 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed in 2015
# if you are having trouble, comment out the above line...




# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC



# Function to write #1:  scale
'''takes in a list and returns a list with "mapped" elements multiplied by the
scale_factor'''
def scale(L, scale_factor):
    multList = [x*scale_factor for x in L]
    return multList


# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC


# Function to write #2:  add_2
''' accepts 2 lists and adds each element from each together and
returns a list of the resulting list'''
def add_2(L,M):
    N = min(len(L), len(M))
    AL = [L[i]+M[i] for i in range(N)]
    return AL


# Function to write #3:  add_3
'''accepts 3 lists and adds each element from each together and
returns a list of the resulting list'''
def add_3(L,M,P):
    N = min(len(L), len(M), len(P))
    AL2 = [L[i]+M[i]+P[i] for i in range(N)]
    return AL2


# Function to write #4:  add_scale_2
'''accepts 2 lists and 2 multiplicative values, we multiply the respective
lists by the multiplicative value and return a list of sums of the two lists'''
def add_scale_2(L,M, L_scale, M_scale):
    LmultList = [L[i]*L_scale for i in range(L)]
    MmultList = [M[i]* M_scale for i in range(M)]
    N =  min(len(L), len(M))
    x = [LmultList[i]+MmultList[i] for i in range(N)]
    return x


# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x

# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
        LC = [randomize(L, chance_of_replacing) for x in L]
        return LC


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    sound_data = [0, 0]           # an "empty" list
    read_wav(filename, sound_data)# get data INTO sound_data

    samps = sound_data       # the raw pressure samples

    print("The first 10 sound-pressure samples are\n", samps[:10])
    sr = sound_data[1]            # the sampling rate, sr
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsamps = samps                     # same samples as before
    new_sound_data = [newsamps, newsr]   # new sound data pair
    write_wav(new_sound_data, "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')


def reverse(filename):
    '''reverse takes in a file and reverses the sound profile by flipping the sound
    data within the string'''
    print("Playing the original sound...")
    play(filename)

    print("Reading in the sound data...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[::-1]
    sr = sound_data[1]

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    newsr = sr
    new_sound_data = [samps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')


# Sound function to write #2:  volume
def volume(filename, scale_factor):
    '''volume takes in a sound file and a scale factor, which is
    effectively the change in volume, it returns a scaled up, down or the same
    sound profile list'''
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    newsamps = scale(sound_data, scale_factor)
    write_wav(newsamps, "out.wav")
    play('out.wav')

# Sound function to write #3:  static
def static(filename, probability_of_static):
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    newsamps = replace_some(sound_data, probability_of_static)
    write_wav(newsamps, "out.wav")
    play('out.wav')
# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    sound_data1 = [0,0]
    sound_data2 = [0,0]
    read_wav(filename1, sound_data1)
    read_wav(filename2, sound_data2)
    N = min(len(sound_data1), len(sound_data2))
    newList = [sound_data1[i]+sound_data2[i] for i in range(N)]
    write_wav(newList, "out.wav")
    play('out.wav')
    return newList
# Sound function to write #5:  echo
def echo(filename, time_delay):
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    waitTimeList = [add_scale_2(sound_data[i], sound_data[i], time_delay, 1) for i in range(sound_data)]#+ sound_data[i]
    echoData = 




# Helper function for generating pure tones
def gen_pure_tone(freq, seconds, sound_data):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    if sound_data != [0, 0]:
        print("Please proivde a value of [0, 0] for sound_data.")
        return
    sampling_rate = 22050
    # how many data samples to create
    nsamples = int(seconds*sampling_rate) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sampling_rate   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    sound_data[0] = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    sound_data = [0, 0]
    gen_pure_tone(freq, time_in_seconds, sound_data)

    print("Writing out the sound data...")
    write_wav(sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #6:  chord


