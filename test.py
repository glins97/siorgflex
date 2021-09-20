import argparse
from spade_bdi.bdi import BDIAgent

parser = argparse.ArgumentParser(description='spade bdi master-server example')
parser.add_argument('--server', type=str, default="communicator@localhost", help='XMPP server address.')
parser.add_argument('--password', type=str, default="1234", help='XMPP password for the agents.')
args = parser.parse_args()

a = BDIAgent("BasicAgent@" + args.server, args.password, "basic.asl")
a.start()

a.bdi.set_belief("car", "blue", "big")
a.bdi.print_beliefs()

print(a.bdi.get_belief("car"))
a.bdi.print_beliefs()

a.bdi.remove_belief("car", 'blue', "big")
a.bdi.print_beliefs()

print(a.bdi.get_beliefs())
a.bdi.set_belief("car", 'yellow')