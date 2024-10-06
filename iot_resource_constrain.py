from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Add hosts with CPU and memory limits
        h1 = self.addHost('h1', cpu=.75)
        h2 = self.addHost('h2', cpu=.25)

        # Add a switch
        s1 = self.addSwitch('s1')

        # Add links with bandwidth, delay, and packet loss limits
        self.addLink(h1, s1, bw=10, delay='5ms', loss=1)
        self.addLink(h2, s1, bw=10, delay='5ms', loss=1)

def run():
    topo = MyTopo()
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)

    # Start the network
    net.start()

    # Check CPU limit on hosts
    print("CPU Limits:")
    for host in net.hosts:
        cpu_info = host.cmd('grep "cpu " /proc/stat')
        print("{}: {}".format(host.name, cpu_info))

    # Check Memory limit on hosts
    print("Memory Limits:")
    for host in net.hosts:
        mem_info = host.cmd('free -m')
        print("{}: {}".format(host.name, mem_info))

    # Perform a bandwidth test to check link limits
    print("Bandwidth Test:")
    h1, h2 = net.get('h1', 'h2')
    net.iperf((h1, h2))

    # Open CLI for manual testing
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
