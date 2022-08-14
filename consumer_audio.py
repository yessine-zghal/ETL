from email import message_from_string
from kafka import KafkaConsumer
from json import loads, dumps
import base64
import os
import multiprocessing
import time
import json
import uuid
from scipy.io import wavfile
import wavio
import librosa
import soundfile 
import wave


def consume_data(topic_name):
    print("Consuming from " + topic_name)
    consumer = KafkaConsumer(topic_name,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        value_deserializer=lambda x: loads(x.decode('utf-8'))
       )
    
    print(consumer) 
    
    for msg in consumer:
        print(json.loads(msg.value))
if __name__ == "__main__":
    topic_name = 'wav_tracks'
    consume_data(topic_name)