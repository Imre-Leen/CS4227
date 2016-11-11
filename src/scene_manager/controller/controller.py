class Controller:
    def __init__(self, command_list=[]):
        self.button_command_list = command_list

    def update(self, button):
        for button_command in self.button_command_list:
            if button_command.button == button[0]:
                if button[0].find("mouse") != -1:
                    button_command.x = button[2]
                    button_command.y = button[3]
                button_command.execute()

    def add_command(self, command):
        self.button_command_list.append(command)