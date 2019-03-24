import numpy as np
import pandas as pd
import json

file_name = song_lst.json
file = json.loads(open(file_name).read())

## File should be formatted with songs and names
song_array = np.zeros_like((file.shape[0],3))
for i in range(len(file.shape[0])):
    song_array[i][0] = file['song']
    song_array[i][1] = file['artist']
    song_array[i][2] = file['album']
