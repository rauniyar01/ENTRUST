import json
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def topology():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch, link=TCLink)

    # Read JSON configuration
    with open('network_config.json') as f:
        config = json.load(f)

    print("*** Adding controller")
    net.addController('c0')

    print("*** Adding IoT hosts and gateways")
    hosts = {}
    gateways = {}
    switches = {}

    # Add hosts
    for host in config['hosts']:
        hosts[host['name']] = net.addHost(host['name'], ip=host['ip'])

    # Add gateways (as hosts)
    for gateway in config['gateways']:
        gateways[gateway['name']] = net.addHost(gateway['name'], ip=gateway['ip'])
        # Add corresponding switches for gateways
        switches[gateway['name']] = net.addSwitch(f's_{gateway["name"]}')

    print("*** Creating links")
    for link in config['links']:
        source = link['source']
        target = link['target']
        if source in hosts and target in gateways:
            net.addLink(hosts[source], switches[target])
        elif source in gateways and target in hosts:
            net.addLink(switches[source], hosts[target])

    # Link gateways to their switches
    for gateway in gateways:
        net.addLink(gateways[gateway], switches[gateway])

    print("*** Starting network")
    net.start()

    # Attach the gateway switches to the Host-Only network
    for switch in switches.values():
        switch.attach('eth0')

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
