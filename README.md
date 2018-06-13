# portknockcombinations
The nuclear option for port knocking by trying all combinations from a user-provided list. Pauses for one second between each probe to prevent retransmission caps from being hit


usage:
python portknockcombinations.py <ip> <space-separated ports list>
(UDP ports are denoted by appending 'u')
  
  e.g.
  
  python portknockcombinations.py 127.0.0.1 80 443 53u
