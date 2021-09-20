from agents.communicator import Communicator
from agents.executor import Executor

import time

if __name__ == "__main__":
    communicator = Communicator("communicator@localhost", "1234")
    communicator.start()

    executor = Executor("executor@localhost", "1234")
    executor.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    
    communicator.stop()
    executor.stop()