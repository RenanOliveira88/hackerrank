if __name__ == '__main__':
    N = int(input())

    commands = []
    new_list = []
    possible_commands = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']

    for line in range(N):
        commands.append(input())

    for command_line in commands:
        values = command_line.split()
        command = ''
        value = 0
        second_value = 0

        if len(values) > 2:
            second_value = int(values[2])
        if len(values) > 1:
            value = int(values[1])

        command = values[0]

        if command not in possible_commands:
            continue

        if command == 'insert':
            new_list.insert(value, second_value)
        if command == 'print':
            print(new_list)
        if command == 'remove':
            new_list.remove(value)
        if command == 'append':
            new_list.append(value)
        if command == 'sort':
            new_list.sort()
        if command == 'pop':
            new_list.pop()
        if command == 'reverse':
            new_list.reverse()
