import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import DrawingSpec

# Helper for getting drawing tools
def get_drawing_tools():
    return (mp.solutions.drawing_utils, mp.solutions.drawing_styles, mp.solutions.face_mesh)

# Additional specs for drawing nose
FACEMESH_FACE_NOSE = frozenset([(245, 134), (134, 129), (129, 98), (98, 97), (97, 326), (326, 327), (327, 358), (358, 363), (363, 465), (97, 242), (242, 241), (241, 44), (44, 274), (274, 461), (461, 462), (462, 326)])  

GREEN_COLOR = (48, 255, 48)

def get_face_landmark_style():
        return DrawingSpec(color=GREEN_COLOR, thickness=2)