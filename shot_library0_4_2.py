Hfreq = 400
azm_freq = 50
alt_freq = 50
top_pin = 11
bot_pin = 13
azm_pin = 32
alt_pin = 33

hhspd = 100
hspd = 95
mspd = 85
lspd = 75

azm_center = 7.5
azm_left = 5
azm_right = 10

alt_center = 7.5
alt_up = 2.5
alt_down = 11


class Shot:

    def __init__(self, tfreq, bfreq, azmfreq, altfreq, tpin, bpin, azmpin, altpin, tduty, bduty,
                 azmduty, altduty, name):
        self.tfreq = tfreq
        self.bfreq = bfreq
        self.azmfreq = azmfreq
        self.altfreq = altfreq
        self.tpin = tpin
        self.bpin = bpin
        self.azmpin = azmpin
        self.altpin = altpin
        self.tduty = tduty
        self.bduty = bduty
        self.azmduty = azmduty
        self.altduty = altduty
        self.name = name

    def startup(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = lspd
        self.bduty = lspd
        self.azmduty = azm_center
        self.altduty = alt_center
        self.name = "Starting Motors"

    def t_c(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hspd
        self.bduty = mspd
        self.azmduty = azm_center
        self.altduty = alt_center
        self.name = "Topspin Center"

    def t_l(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hspd
        self.bduty = mspd
        self.azmduty = azm_left
        self.altduty = alt_center
        self.name = "Topspin Left"

    def t_r(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hspd
        self.bduty = mspd
        self.azmduty = azm_right
        self.altduty = alt_center
        self.name = "Topspin Right"

    def t_c_d(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hhspd
        self.bduty = hspd
        self.azmduty = azm_center
        self.altduty = alt_center
        self.name = "Topspin Center Deep"

    def t_l_d(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hhspd
        self.bduty = hspd
        self.azmduty = azm_left
        self.altduty = alt_center
        self.name = "Topspin Left Deep"

    def t_r_d(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hhspd
        self.bduty = hspd
        self.azmduty = azm_right
        self.altduty = alt_center
        self.name = "Topspin Right Deep"

    def b_c(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = mspd
        self.bduty = hspd
        self.azmduty = azm_center
        self.altduty = alt_down
        self.name = "Backspin Center"

    def b_l(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = mspd
        self.bduty = hspd
        self.azmduty = azm_left
        self.altduty = alt_down
        self.name = "Backspin Left"

    def b_r(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = mspd
        self.bduty = hspd
        self.azmduty = azm_left
        self.altduty = alt_down
        self.name = "Backspin Right"

    def b_c_d(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hspd
        self.bduty = hhspd
        self.azmduty = azm_center
        self.altduty = alt_down
        self.name = "Backspin Center Deep"

    def b_l_d(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hspd
        self.bduty = hhspd
        self.azmduty = azm_left
        self.altduty = alt_down
        self.name = "Backspin Left Deep"

    def b_r_d(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.azmfreq = azm_freq
        self.altfreq = alt_freq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.azmpin = azm_pin
        self.altpin = alt_pin
        self.tduty = hspd
        self.bduty = hhspd
        self.azmduty = azm_left
        self.altduty = alt_down
        self.name = "Backspin Right Deep"

    # def d_t_spin(self):
    #     self.tfreq = Hfreq
    #     self.bfreq = Hfreq
    #     self.tpin = top_pin
    #     self.bpin = bot_pin
    #     self.tduty = hhspd
    #     self.bduty = hspd
    #     self.name = "DeepTopspin"
    #
    # def d_b_spin(self):
    #     self.tfreq = Hfreq
    #     self.bfreq = Hfreq
    #     self.tpin = top_pin
    #     self.bpin = bot_pin
    #     self.tduty = hspd
    #     self.bduty = hhspd
    #     self.name = "Deep Backspin"
    #
    # def d_shot(self):
    #     self.tfreq = Hfreq
    #     self.bfreq = Hfreq
    #     self.tpin = top_pin
    #     self.bpin = bot_pin
    #     self.tduty = mspd
    #     self.bduty = mspd
    #     self.name = "Dropshot"
    #
    # def wideopen(self):
    #     self.tfreq = Hfreq
    #     self.bfreq = Hfreq
    #     self.tpin = top_pin
    #     self.bpin = bot_pin
    #     self.tduty = hhspd
    #     self.bduty = hhspd
    #     self.name = "Wide Open"


Shot = Shot(100, 100, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # Initial shot paramaters
