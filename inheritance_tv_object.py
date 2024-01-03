class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume is already at the maximum limit (100). Unable to increase volume.")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is already at the minimum limit (0). Unable to decrease volume.")

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            print(f"Invalid channel. {self.brand} stays at the current channel: {self.channel}")

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def get_status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LEDTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = None
        self.backlight = None
        self.display_details = None

    def set_viewing_angle(self, angle):
        self.viewing_angle = angle

    def set_backlight(self, backlight):
        self.backlight = backlight

    def set_display_details(self, details):
        self.display_details = details


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = None
        self.backlight = None
        self.display_details = None

    def set_viewing_angle(self, angle):
        self.viewing_angle = angle

    def set_backlight(self, backlight):
        self.backlight = backlight

    def set_display_details(self, details):
        self.display_details = details


# Example Usage
led_tv = LEDTV("Sony", "Thin", "Low", "5 years", "120Hz")
led_tv.set_viewing_angle("180 degrees")
led_tv.set_backlight("LED")
led_tv.set_display_details("4K UHD")

plasma_tv = PlasmaTV("Samsung", "Thick", "High", "7 years", "60Hz")
plasma_tv.set_viewing_angle("160 degrees")
plasma_tv.set_backlight("Plasma")
plasma_tv.set_display_details("Full HD")

# Testing TV class methods
led_tv.increase_volume()
led_tv.set_channel(18)
print(led_tv.get_status())  # Output: Sony at channel 10, volume 51

plasma_tv.decrease_volume()
plasma_tv.set_channel(59)
print(plasma_tv.get_status())  # Output: Samsung at channel 1, volume 49
