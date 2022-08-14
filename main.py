from asyncore import file_dispatcher
import os, sys
import argparse
import time
import json
import uuid
from scipy.io import wavfile
import wavio
import librosa
import soundfile 
import wave


from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
topic = 'wav_tracks'

def audio_to_bytes(input_file):
    #wa = wavio.read(input_file+"/audio0.wav")  #Read a .wav file
    wav_file = input_file+"/test.wav"
    wa = wavio.read(wav_file)  #Read a .wav file
    print("x= "+str(wa.data))   #Data
    print("rate= "+str(wa.rate))    #Rate
    print("sampwidth= "+str(wa.sampwidth))
    print(type(wa.data.tolist()))
    print(type(wa.rate))
    print(type(wa.sampwidth))
    ditc = {
                                                #'uuid' : str(uuid.uuid4()),
                                                'data' : str(bytearray(wa.data)),
                                                'rate' : str(wa.rate),
                                                'sampwidth' : str(wa.sampwidth)
                                            }
    #print(ditc)

    
    producer.send(topic,value = ditc)
            # Reduce CPU usage
    time.sleep(0.1)

if __name__ == '__main__':
    audio_to_bytes('/home/yessine/Desktop/kafka/data')