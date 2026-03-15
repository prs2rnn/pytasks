def wash(program):
    if program == 'color':
        cycles = 700
    else:
        cycles = 500
    
    while cycles > 0:
        print('Белье еще стирается')
        
        cycles = cycles - 100
    print('Белье постирано!')

wash('color')