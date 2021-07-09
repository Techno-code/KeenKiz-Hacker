# Get list of lengths and list of widths
lengths = [2, 6, 3, 12]
widths = [8, 1, 7, 4]

# Verify length of list of length = length of list of lengths
if len(lengths) == len(widths):

    areas = []

    # Expected output: [16, 6, 21, 48]

    for i in range(0, len(lengths)):
        areas.append(lengths[i]*widths[i])

    for j in range(0, len(areas)):
        print(areas[j])