#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch, failMode='standalone')
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch, failMode='standalone')
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch, failMode='standalone')
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch, failMode='standalone')
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch, failMode='standalone')
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s2, s4)
    net.addLink(s2, s1)
    net.addLink(s1, s3)
    net.addLink(h1, s1)
    net.addLink(s2, s5)
    net.addLink(s5, s3)
    net.addLink(s7, s6)
    net.addLink(s1, s7)
    net.addLink(s6, s8)
    net.addLink(s5, s8)
    net.addLink(s8, s17)
    net.addLink(s10, s9)
    net.addLink(s10, s7)
    net.addLink(s14, s17)
    net.addLink(s11, s17)
    net.addLink(s11, s5)
    net.addLink(s4, s12)
    net.addLink(s11, s12)
    net.addLink(s15, s12)
    net.addLink(s16, s15)
    net.addLink(s13, s16)
    net.addLink(s13, s2)
    net.addLink(s12, s14)
    net.addLink(s17, s18)
    net.addLink(s19, s18)
    net.addLink(s20, s19)
    net.addLink(s15, s20)
    net.addLink(s14, s20)
    net.addLink(h2, s20)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s10').start([])
    net.get('s9').start([])
    net.get('s18').start([])
    net.get('s8').start([])
    net.get('s6').start([])
    net.get('s11').start([])
    net.get('s4').start([])
    net.get('s2').start([])
    net.get('s15').start([])
    net.get('s14').start([])
    net.get('s20').start([])
    net.get('s12').start([])
    net.get('s16').start([])
    net.get('s5').start([])
    net.get('s7').start([])
    net.get('s19').start([])
    net.get('s3').start([])
    net.get('s17').start([])
    net.get('s13').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

