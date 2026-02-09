def detect_aggregation_propensity(sequence): 
    # will report regions with high local hydrophobicity (e.g., >4 consecutive hydrophobic residues)

    hydrophobic = "AVILMFWY"   # hydrophobic amino acids
    window_size = 4          # based on the question
    found = False


    # creating an window for checking
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]

        # Check if all residues in the window are hydrophobic
        is_hydrophobic = True
        for aa in window:
            if aa not in hydrophobic:
                is_hydrophobic = False
                break

        if is_hydrophobic:
            print(f"Hydrophobic region found at position {i + 1}: {window}")
            found = True

    if not found:
        print("No hydrophobic regions found.")

# our sequence
sequence = 'MYRMQLLSCIALSLALVTNSAPTSSSTKKTQLQLEHLLLDLQMVILNGINNYKNPKLTRMLTFKFYMPKKATELKHLQCLEEELKPLEEVLNLAQSKNFHLRPRDLISNINVIVLELKGSETTFMCEYADEKTATIVEFLNRWITFCQSIISTLT'
# calling the function
detect_aggregation_propensity(sequence)

