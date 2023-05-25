with open('input.txt','r') as file:
    for line in file:
        if line.startswith('Port:'):
            with open('output.txt', 'w') as file:
                file.truncate(0)
            with open('output.txt', 'a') as output_file:
                output_file.write(line)
        if line.startswith('Satellite:'):
            with open('output.txt', 'w') as file:
                file.truncate(0)
            with open('output.txt', 'a') as output_file:
                output_file.write(line)

with open('output.txt', 'r') as input_file:
    with open('output3.txt', 'w') as output_file:
        for line in input_file:
            ex = line.split(" ")
            final = []
            for item in ex:
                if item.isdigit():
                    final.append(item)
            final.append(ex[len(ex)-1][0:3])
            finals = ' '.join(final)
            output_file.write(finals)
            output_file.write('\n')


