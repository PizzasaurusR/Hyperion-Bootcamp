usr_input = int(input("Please enter a number. To end enter -1. "))
input_count = 0
run_total = 0
avg = 0

while usr_input != -1:
    input_count += 1
    run_total += usr_input
    usr_input = int(input("Please enter the next number: "))
    if usr_input == -1:
        break

avg = run_total / input_count
print(f"Your average is {avg}")
