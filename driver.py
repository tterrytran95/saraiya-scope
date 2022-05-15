
from state import State 
from createmuseum import FrameCapture 
import tty, sys

RAW_VIDEO = "samples/theview.MOV"


def get_key_input():
    tty.setcbreak(sys.stdin)
    return sys.stdin.read(1)[0]

def main():
    outframes = FrameCapture(RAW_VIDEO)
    state = State(museum = outframes)
    
    i = 0
    while True: # let this run forever 
        event = get_key_input()
        print("you pressed ", event)
        if event == 'q':
            exit()
        
        

main()
