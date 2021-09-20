
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

import time
import asyncio

class BaseAgent(Agent):

    def send(self, to, msg):
        pass
