from playsound import playsound
from flask import Flask, json, request,jsonify,Response
from flask_cors import CORS, cross_origin
import sounddevice as sd
from scipy.io.wavfile import write
import multiprocessing
import socket
import pyaudio
import wave
import time
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
import socket
import pyaudio
import wave
import time
def server():
     CHUNK = 1024
     FORMAT = pyaudio.paInt16
     CHANNELS = 1
     RATE = 44100
     RECORD_SECONDS = 4
     WAVE_OUTPUT_FILENAME = "server_output.wav"
     WIDTH = 2
     frames = []
     p = pyaudio.PyAudio()
     stream = p.open(format=p.get_format_from_width(WIDTH),
     channels=CHANNELS,
     rate=RATE,
     output=True,
     frames_per_buffer=CHUNK)
     HOST = '192.168.0.10'                 # Symbolic name meaning all available interfaces
     PORT = 50007           # Arbitrary non-privileged port
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((HOST, PORT))
     s.listen(1)
     print("PTT Server Started")
     conn, addr = s.accept()
     print('Connected by', addr)
     data = conn.recv(1024)
     i=1
     while data != '':
         stream.write(data)
         data = conn.recv(1024)
         i=i+1
         #print(i)
         # frames.append(data)
     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
     wf.setnchannels(CHANNELS)
     wf.setsampwidth(p.get_sample_size(FORMAT))
     wf.setframerate(RATE)
     wf.writeframes(b''.join(frames))
     wf.close()
     stream.stop_stream()
     stream.close()
     p.terminate()
     conn.close()
    

def client():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 40
    HOST = '192.168.196.211'    # The remote host
    PORT = 50007           # The same port as used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("*Server Connected")

    frames = []

    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data  = stream.read(CHUNK)
        frames.append(data)
        s.sendall(data)

    print("*done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    s.close()

    print("*closed")


    
p = multiprocessing.Process(target=playsound, args=("Noise.wav",))
q = multiprocessing.Process(target=playsound, args=("Starting.wav",))
r = multiprocessing.Process(target=playsound, args=("bite.wav",))
ptts = multiprocessing.Process(target=server)
pttc = multiprocessing.Process(target=client)



@app.route('/on',methods = ['GET'])
def turnon():

    global p
    #playsound("Noise.wav")
    if p.is_alive():
        p.join()
    else:
        p = multiprocessing.Process(target=playsound, args=("Noise.wav",))
        p.start()
    return jsonify({"played":"true"})

@app.route('/off',methods = ['GET'])
def turnoff():
    #playsound("Noise.wav")
    if p.is_alive():
        p.terminate()
    return jsonify({"played":"false"})

@app.route('/pttseroff',methods = ['GET'])
def turnseroff():
    global ptts
    #playsound("Noise.wav")
    if ptts.is_alive():
        ptts.terminate()
    return jsonify({"played":"false"})

@app.route('/pttclioff',methods = ['GET'])
def turnclioff():
    global pttc
    #playsound("Noise.wav")
    if pttc.is_alive():
        pttc.terminate()
    return jsonify({"played":"false"})

@app.route('/sq',methods = ['GET'])
def sq():
    global q
    if q.is_alive():
        q.join()
    else:
        q = multiprocessing.Process(target=playsound, args=("Starting.wav",))
        q.start()
    
    return jsonify({"played":"true"})

@app.route('/bite',methods = ['GET'])
def bite():
    global r
    if r.is_alive():
        r.join()
    else:
        r = multiprocessing.Process(target=playsound, args=("bite.wav",))
        r.start()
    
    return jsonify({"played":"true"})


@app.route('/test',methods = ['GET'])
def test():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording) 
    playsound("output.wav")
    return jsonify({"tested":"true"})

@app.route('/pttserver',methods = ['GET'])
def pttser():
    global ptts
    if ptts.is_alive():
        ptts.join()
    else:
        ptts = multiprocessing.Process(target=server)
        ptts.start()

   
    return({"Server":"Closed"})

@app.route('/pttclient',methods = ['GET'])
def pttcli():
    global pttc
    if pttc.is_alive():
        pttc.join()
    else:
        pttc = multiprocessing.Process(target=client)
        pttc.start()

    return({"Client":"Closed"})

if __name__ == '__main__':
    app.run(host="0.0.0.0")

