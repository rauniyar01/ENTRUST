from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def topology():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)

    print("*** Adding controller")
    net.addController('c0')

    print("*** Adding hosts")
    h1 = net.addHost('h1', ip='192.168.56.101/24')  # Assign an IP in the same range as the Raspberry Pi VM

    print("*** Adding switch")
    s1 = net.addSwitch('s1')

    print("*** Creating links")
    net.addLink(h1, s1)

    print("*** Starting network")
    net.start()

    # Attach the switch to the Host-Only network interface (eth0)
    print("*** Attaching switch to Host-Only network")
    s1.attach('eth0')

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
