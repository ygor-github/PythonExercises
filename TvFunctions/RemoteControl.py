class RemoteControl:

    def __init__(self, tv):
        self.tv = tv

    def increase_volume(self):
        self.tv.increase_volume(90)

    def decrease_volume(self):
        self.tv.decrease_volume(90)

    def change_channel(self, channel):
        self.tv.change_channel(channel)

    def tune_channel(self, channel):
        self.tv.tune_channel(channel)

