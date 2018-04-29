
start_state = 0x1f
lfsr = start_state;
period = 0;

bit = ((lfsr >> 0) ^ (lfsr >> 1) ^ (lfsr >> 2) ^ (lfsr >> 4) ) & 1;
print(bit, end='')
lfsr = (lfsr >> 1) | (bit << 4);
period += 1

while lfsr != start_state:
    bit = ((lfsr >> 0) ^ (lfsr >> 1) ^ (lfsr >> 2) ^ (lfsr >> 4) ) & 1;
    print(bit, end='')
    lfsr = (lfsr >> 1) | (bit << 4);
    period += 1

print()
print(period)