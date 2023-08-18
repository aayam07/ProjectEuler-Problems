# Problem - 14: Which starting number, under one million, produces the longest chain of Collatz Sequence.

track_sequence_list = []
longest_chain_sequence_length = 0
required_start_number = 0

for start_number in range(2, 1000000):
    track_sequence_list.append(start_number)

    while (start_number != 1):

        if start_number % 2 == 0:
            start_number = int(start_number / 2)
            # print(start_number)
            track_sequence_list.append(start_number)
        else: 
            start_number = int(3 * start_number + 1)
            # print(start_number)
            track_sequence_list.append(start_number)

        if (len(track_sequence_list) > longest_chain_sequence_length):
            longest_chain_sequence_length = len(track_sequence_list)
            required_start_number = track_sequence_list[0]  # first item of the sequence list

    
    track_sequence_list.clear()  # empty the list before testing for another start number
    

print(f"The starting number is : {required_start_number} with sequence length of {longest_chain_sequence_length}")
    