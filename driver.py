
from state import State 
from createmuseum import FrameCapture 

RAW_VIDEO = "samples/theview.MOV"

def main():
    outframes = FrameCapture(RAW_VIDEO)
    state = State(museum = outframes)
    

main()
