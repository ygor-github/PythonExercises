class Television:
    def __init__(self, fab, modelo):
        self.manufacturer = fab
        self.model = modelo
        self.current_channel = None
        self.channel_list = []
        self.volume = 20

    def increase_volume(self, value):
        if self.volume+ value <= 100:
            self.volume += value
        else:
            self.volume = 100

    def decrease_volume(self,value):
        if self.volume- value >= 0:
            self.volume -= value
        else:
            self.volume = 0

    def change_channel(self, channel):
        if channel in self.channel_list:
            self.current_channel = channel

    def tune_channel(self, channel):
        if channel not in self.channel_list:
            self.channel_list.append(channel)





