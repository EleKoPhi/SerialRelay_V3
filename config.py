class config:
    channelDescription = []

    def __init__(self):
        C1_description = "C1"
        C2_description = "C2"
        C3_description = "C3"
        C4_description = "C4"
        C5_description = "C5"
        C6_description = "C6"
        C7_description = "C7"
        C8_description = "C8"

        self.channelDescription.append(C1_description)
        self.channelDescription.append(C2_description)
        self.channelDescription.append(C3_description)
        self.channelDescription.append(C4_description)
        self.channelDescription.append(C5_description)
        self.channelDescription.append(C6_description)
        self.channelDescription.append(C7_description)
        self.channelDescription.append(C8_description)

    def getChannelDescription(self, channel):
        index = channel - 1
        return self.channelDescription[index]
