guests = ['Alex', 'Mike', 'Helen']
for guest in guests:
    print(f"Hi, {guest.title()}! You are invited.")
print('Alex is busy')
guests.remove('Alex')
guests.append('Raf')
for guest in guests:
    print(f"Hi, {guest.title()}! You are invited.")
print('We found a bigger table')
guests.insert(0, 'Zab')
guests.insert(int(len(guests)/2), 'Masha')
print(guests.index('Masha'))
guests.append('Galina')
for guest in guests:
    print(f"Hi, {guest.title()}! You are invited.")
