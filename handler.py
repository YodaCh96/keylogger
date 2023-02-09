lines = ["H", "a", "l", "l", "Key.backspace", "Key.backspace", "Key.backspace", "e", "l", "l", "o"]
#lines = ["1", "Key.backspace", "3", "4", "Key.backspace", "Key.backspace", "5", "6", "7"]
#lines = ["Key.backspace", "1", "Key.backspace"]
#lines = ["Key.backspace", "Key.backspace", "Key.backspace", "Key.backspace", "1", "2", "Key.backspace"]

def Parser1(lines, start):
    if start < 0: start = 0
    for val in lines[start:]:
        if val == "Key.backspace":
            current_idx = lines.index(val)
            lines.remove(val)
            if current_idx > 0: 
                del lines[current_idx-1]
            if val in lines:
                Parser1(lines, current_idx-1)
                break
            else:
                return ''.join(lines)
    return ''.join(lines)


def Parser2(lines):
    new_lines = []
    while lines:
        for i in lines:
            try:
                if i == 'Key.backspace':
                    del new_lines[-1]
                    del lines[0]
                    break
                else:
                    new_lines.append(i)
                    del lines[0]
                    break
            except IndexError:
                del lines[0]
                break
    return ''.join(new_lines)


if __name__ == "__main__":
    print(Parser1(lines, 0))
    print(Parser2(lines))
