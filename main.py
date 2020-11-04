from managers.bananas import find_bananas_per_hour

import time

if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    H = 8
    print(f'Input: {piles}')
    starting_time = time.process_time()
    print(f'Output: {find_bananas_per_hour(piles, H)}')
    ending_time = time.process_time()
    print(f'Elapsed {ending_time - starting_time} seconds')
