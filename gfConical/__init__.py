__author__ = 'github.com/wardsimon'
__version__ = '0.0.3'

GRAINFATHER_AUTH_URL = "https://community.grainfather.com/api/auth/login"
GRAINFATHER_TOKENS_URL = "https://community.grainfather.com/api/particle/tokens"
PARTICLE_EVENT_URL = "https://api.particle.io/v1/devices"

from .grainfather import Grainfather
