CHANNELS = ["BBC", "Discovery", "TV1000"]


class TvController:
    def __init__(self, first_channel, second_channel, third_channel):
        self.default_channel = first_channel
        self.current_channel = self.default_channel
        self.first_channel = first_channel
        self.second_channel = second_channel
        self.third_channel = third_channel
        self.user_input = None

    def to_current_channel(self):
        print(self.current_channel)

    def to_first_channel(self):
        print(f'{self.first_channel} channel was turned on')
        self.current_channel = self.first_channel

    def to_last_channel(self):
        print(f'{self.third_channel} channel was turned on')
        self.current_channel = self.third_channel

    def turn_channel(self):
        self.user_input = int(input('Choose your channel: '))
        while True:
            if self.user_input == 1:
                print(f'The {self.first_channel} channel was turned on')
                self.current_channel = self.first_channel
            elif self.user_input == 2:
                print(f'The {self.second_channel} channel was turned on')
                self.current_channel = self.second_channel
            elif self.user_input == 3:
                print(f'The {self.third_channel} channel was turned on')
                self.current_channel = self.third_channel
            else:
                print('Try again!')
            break

    def next_channel(self):
        while True:
            if self.current_channel == self.first_channel:
                self.current_channel = self.second_channel
                self.to_current_channel()
            elif self.current_channel == self.second_channel:
                self.current_channel = self.third_channel
                self.to_current_channel()
            elif self.current_channel == self.third_channel:
                self.current_channel = self.first_channel
                self.to_current_channel()
            break

    def previous_channel(self):
        while True:
            if self.current_channel == self.first_channel:
                self.current_channel = self.third_channel
                self.to_current_channel()
            elif self.current_channel == self.second_channel:
                self.current_channel = self.first_channel
                self.to_current_channel()
            elif self.current_channel == self.third_channel:
                self.current_channel = self.second_channel
                self.to_current_channel()
            break

    def is_exist(self):
        while True:
            self.user_input = input('Which channel do you want to check?(Write the name of the channel)\n')
            if self.user_input in CHANNELS:
                print('Yes!')
            else:
                print('No!')


def user_interface():
    controller = TvController(CHANNELS[0], CHANNELS[1], CHANNELS[2])
    while True:
        user_input = int(input('''
+--------------------------------+
|          TvController          |
| 1 - To check current channel   |
| 2 - Switch to first channel    |
| 3 - Switch to last channel     |
| 4 - Switch to your channel     |
| 5 - Switch to next channel     |
| 6 - Switch to previous channel |
| 7 - Check for a channel        |
+--------------------------------|
Choose your action: '''))
        if user_input == 1:
            controller.to_current_channel()
        elif user_input == 2:
            controller.to_first_channel()
        elif user_input == 3:
            controller.to_last_channel()
        elif user_input == 4:
            controller.turn_channel()
        elif user_input == 5:
            controller.next_channel()
        elif user_input == 6:
            controller.previous_channel()
        elif user_input == 7:
            controller.is_exist()
        else:
            print('Try again!')
        continue


user_interface()
