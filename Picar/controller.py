import pygame
import threading

class PS4Controller:
    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        pygame.init()
        pygame.joystick.init()

        # Check if a joystick is connected
        if pygame.joystick.get_count() == 0:
            raise Exception("No joystick connected.")
        
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def listen(self):
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.joystick.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.joystick.get_numhats()):
                self.hat_data[i] = (0, 0)
        
        # Listen loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

    def read(self):
        return self.axis_data, self.button_data, self.hat_data

    def start(self):
        self.init()
        # Create a separate thread for the controller listener
        self.controller_thread = threading.Thread(target=self.listen)
        self.controller_thread.start()

    def stop(self):
        # Stop the controller listener thread
        pygame.quit()
        self.controller_thread.join()
