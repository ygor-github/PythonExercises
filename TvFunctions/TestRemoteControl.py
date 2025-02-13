from TvFunctions.RemoteControl import *
from TvFunctions.Television import *

tv = Television('SONY','SONY-123')
control = RemoteControl(tv)

control.tune_channel('SBT')
control.change_channel('SBT')
control.tune_channel('BRT')

print(tv.current_channel)
print(tv.model)
print(tv.channel_list)