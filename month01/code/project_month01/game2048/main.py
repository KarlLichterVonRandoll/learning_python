from ui import *

from model import MapModel

model = MapModel(4)
map01 = model.generate_map()

view = GameManagerView(map01)
view.main()
