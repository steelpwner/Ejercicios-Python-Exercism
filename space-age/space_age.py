class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds / (365.25*24*60*60)

    def handleFloat(self, f):
        return round(f, 2)

    def on_earth(self):
        return self.handleFloat(self.years)

    def on_mercury(self):
        return self.handleFloat(self.years/0.2408467)

    def on_venus(self):
        return self.handleFloat(self.years/0.61519726)

    def on_mars(self):
        return self.handleFloat(self.years/1.8808158)

    def on_jupiter(self):
        return self.handleFloat(self.years/11.862615)

    def on_saturn(self):
        return self.handleFloat(self.years/29.447498)

    def on_uranus(self):
        return self.handleFloat(self.years/84.016846)

    def on_neptune(self):
        return self.handleFloat(self.years/164.79132)
