with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for line in input_file:
            if line.startswith("Port:"):
                output_file.write(line)