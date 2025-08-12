# Define mitochondrial sequence length
sequence_length = 16447
num_segments = 12
overlap = 100  # Adjust overlap size as needed

# Calculate base segment length (without overlap)
segment_size = sequence_length // num_segments

# Generate segment start and end positions
segments = []
for i in range(num_segments):
    start = max(1, i * segment_size - overlap)  # Start position (1-based)
    end = min(sequence_length, (i + 1) * segment_size)  # End position
    segments.append((start, end))

# Print segment details
print("Segment Start-End Positions:")
for i, (start, end) in enumerate(segments, 1):
    print(f"Segment {i}: {start} - {end} ({end-start+1} bp)")
