
class config():

    channelDescription = []

    def __init__(self):
        C1_description = "Clamp 30"
        C2_description = "Clamp 15"
        C3_description = "Clamp 15 Wakeup"
        C4_description = "Clamp 30 C"
        C5_description = "Clamp 30 B"
        C6_description = "Clamp 30 G"
        C7_description = "Clamp 30 Last"
        C8_description = "30V HV Simulation"

        self.channelDescription.append(C1_description)
        self.channelDescription.append(C2_description)
        self.channelDescription.append(C3_description)
        self.channelDescription.append(C4_description)
        self.channelDescription.append(C5_description)
        self.channelDescription.append(C6_description)
        self.channelDescription.append(C7_description)
        self.channelDescription.append(C8_description)

    def getChannelDescription(self,channel):
        index = channel - 1
        return self.channelDescription[index]