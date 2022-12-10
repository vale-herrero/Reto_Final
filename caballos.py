NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(), 
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}
def neighbors(position):
    return NEIGHBORS_MAP[position]

def yield_sequences(starting_position, num_hops, sequence=None):
    if sequence is None:
        sequence = [starting_position]
    
    if num_hops == 0:
        yield sequence
        return
    for neighbor in neighbors(starting_position):
        yield from yield_sequences(
            neighbor, num_hops - 1, sequence + [neighbor])

def count_sequences(num_hops):
    num_sequences = 0
    for posible_start_number in [1,2,3,4,5,6,7,8,9,0]:
        for sequence in yield_sequences(posible_start_number, num_hops):
            num_sequences += 1
    return num_sequences

for n_hop in [1,2,3,5,8,10,15,18,21,23,32]:
    pos_val = count_sequences(num_hops=n_hop)
    print('Número de movimientos: {} --> posibilidades válidas: {}'.format(n_hop, pos_val))
    

