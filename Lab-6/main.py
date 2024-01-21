class Firearm:
    def __init__(self, ammo_count, rate_of_fire, range):
        self.ammo_count = ammo_count
        self.rate_of_fire = rate_of_fire
        self.range = range

    def time_until_empty(self):
        return self.ammo_count / self.rate_of_fire

    def fire_rate_to_range_ratio(self):
        return self.rate_of_fire / self.range

    def __add__(self, other):
        new_ammo_count = self.ammo_count + other.ammo_count
        new_rate_of_fire = self.rate_of_fire * other.rate_of_fire
        new_range = self.range + other.range

        return Firearm(new_ammo_count, new_rate_of_fire, new_range)


class AssaultRifle(Firearm):
    ammo_count = 60
    rate_of_fire = 10

    def __init__(self, range, automatic):
        super().__init__(self.ammo_count, self.rate_of_fire, range)
        self.automatic = automatic

    def fire_rate_to_range_ratio(self):
        if self.automatic:
            return self.rate_of_fire / self.range
        else:
            return self.rate_of_fire / (self.range * 2)

    def splash_damage(self):
        return self.rate_of_fire * self.ammo_count
        pass


class SniperRifle(Firearm):
    ammo_count = 30
    rate_of_fire = 1

    def __init__(self, range, scope_zoom):
        super().__init__(self.ammo_count, self.rate_of_fire, range)
        self.scope_zoom = scope_zoom

    def scope_and_zoom(self):
        return self.range * self.scope_zoom


def run_tests():
    print("Assault rifle tests:")
    ASSAULT_RANGE = 100
    automaticRifle = AssaultRifle(ASSAULT_RANGE, True)
    unautomaticRifle = AssaultRifle(ASSAULT_RANGE, False)

    print("Time until empty: " +
          str(unautomaticRifle.time_until_empty()))
    print("Fire rate Automatic: " +
          str(automaticRifle.fire_rate_to_range_ratio()))
    print("Fire rate unAutomatic: " +
          str(unautomaticRifle.fire_rate_to_range_ratio()))

    print("\nSniper Rifle tests:")
    SNIPER_RANGE = 1000
    ZOOM_FACTOR = 5
    sniperRifle = SniperRifle(SNIPER_RANGE, ZOOM_FACTOR)

    print("Time until empty: " +
          str(sniperRifle.time_until_empty()))
    print("Fire rate Automatic: " +
          str(sniperRifle.fire_rate_to_range_ratio()))
    print("Fire rate: " +
          str(sniperRifle.fire_rate_to_range_ratio()))
    print("Zoom factor rate: " +
          str(sniperRifle.scope_and_zoom()))

    print("\nSuper Rifle (Assault + Sniper) tests:")
    frankensteinRifle = AssaultRifle(
        ASSAULT_RANGE, True) + AssaultRifle(ASSAULT_RANGE, True)

    print("Time until empty: " +
          str(frankensteinRifle.time_until_empty()))
    print("Fire rate: " +
          str(frankensteinRifle.fire_rate_to_range_ratio()))


run_tests()
