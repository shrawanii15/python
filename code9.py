def capitalize_lines():
    lines = []
    
    print("Enter lines (type END to stop):")
    
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    for line in lines:
        print(line.upper())
capitalize_lines()