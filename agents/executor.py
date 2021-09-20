
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

import time
import asyncio

from behaviours.receive import ReceiveBehaviour

class Executor(Agent):

    async def setup(self):
        print("Executor starting . . .")
        self.add_behaviour(ReceiveBehaviour())
