
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

import time
import asyncio

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

from threading import _start_new_thread

class Communicator(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0
            
        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            
            msg = Message(to="executor@localhost")
            msg.set_metadata("performative", "inform")  
            msg.set_metadata("ontology", "myOntology")  
            msg.set_metadata("language", "OWL-S")       
            msg.body = "Hello World"                    
            print("Sending message...", end='')
            await self.send(msg)
            print("done")

            await asyncio.sleep(1)
    
    class BehaviourHandleGET(CyclicBehaviour):
        period = 1

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.path[1:].encode())
                
        async def on_start(self):
            self.server = ThreadingHTTPServer(('', 3000), self.Handler)
            print('HTTP server running on port %s' % 3000)
            # _start_new_thread(self.server.serve_forever, tuple())

        async def run(self):
            self.server.handle_request()

    async def setup(self):
        print("Communicator starting . . .")
        self.add_behaviour(self.MyBehav())
        self.add_behaviour(self.BehaviourHandleGET())
        
        # _start_new_thread(self.serve_http, tuple())
        