

class RK4Integrator():
    def __init__(self, f):
        self.f = f

    def integrate(self, y, t, dt):
        k1 = self.f(y, t)
        k2 = self.f(y + 0.5*dt*k1, t + 0.5*dt)
        k3 = self.f(y + 0.5*dt*k2, t + 0.5*dt)
        k4 = self.f(y + dt*k3, t + dt)
        return y + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)