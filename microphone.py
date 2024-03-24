# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)

import argparse
import queue
import sys
import sounddevice as sd

from vosk import Model, KaldiRecognizer


class Microphone:
    q = queue.Queue()
  

    def int_or_str(self, text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l", "--list-devices", action="store_true",
        help="show list of audio devices and exit")
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])

    parser.add_argument(
        "-f", "--filename", type=str, metavar="FILENAME",
        help="audio file to store recording to")
    parser.add_argument(
        "-d", "--device", type=int_or_str,
        help="input device (numeric ID or substring)")
    parser.add_argument(
        "-r", "--samplerate", type=int, help="sampling rate")
    parser.add_argument(
        "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
    args = parser.parse_args(remaining)

    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        
        args.samplerate = 8 * int(device_info["default_samplerate"])
        
    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

        rec = KaldiRecognizer(model, args.samplerate)


    def passiveListen(self, stopWord):
        stopWord = stopWord.lower()

        with sd.RawInputStream(samplerate=self.args.samplerate, blocksize = 64000, device=self.args.device,
            dtype="int16", channels=1, callback=self.callback):

                loop_continue = True
                words = ""
                while loop_continue:
                    data = self.q.get()
                    if self.rec.AcceptWaveform(data):
                        words = self.rec.Result().strip("{\n  \"text\" : \"").rstrip("\"\n}")
                        if words == stopWord or words.startswith(stopWord):
                            loop_continue = False
                    else:
                        words = self.rec.PartialResult()#.strip("{\n  \"partial\" : \"").rstrip("\"\n}")
                        

                    if self.dump_fn is not None:
                        self.dump_fn.write(data)

        
    def getSpeach(self):
            with sd.RawInputStream(samplerate=self.args.samplerate, blocksize = 64000, device=self.args.device,
            dtype="int16", channels=1, callback=self.callback):

                loop_continue = True
                words = ""
                while loop_continue:
                    data = self.q.get()
                    if self.rec.AcceptWaveform(data):
                        words = self.rec.Result().strip("{\n  \"text\" : \"").rstrip("\"\n}")
                        loop_continue = False
                        return words
                    else:
                        words = self.rec.PartialResult()
                    if self.dump_fn is not None:
                        self.dump_fn.write(data)
                        

microphone = Microphone()
      
def mic():
    return microphone


"""
#command line test
m = Microphone()

speach = m.getSpeach()
while speach != "":
    print(" " + speach)
    speach = m.getSpeach()
"""