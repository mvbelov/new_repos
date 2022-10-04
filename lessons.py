class Car:
    engine_status = "OFF"
    wheels = 4

    def start_engine(self):
        self.engine_status = "ON"

    def go(self):
        if self.engine_status == "ON" and self.wheels == 4:
            return "driving"

    def stop_engine(self):
        self.engine_status = "OFF"


a1 = Car()
print(a1.start_engine())
