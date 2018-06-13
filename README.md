# portknockcombinations
The nuclear option for port knocking by trying all combinations from a user-provided list


usage:
python portknockcombinations.py <ip> <space-separated ports list>
(UDP ports are denoted by appending 'u')
  
  e.g.
  
  python portknockcombinations.py 127.0.0.1 80 443 53u
