Gold = 1500

quantity = 0

repair = 300

print(f"Current Gold: {Gold}")

quantity = int(input("How many time would you like to repair it? "))

Gold -= repair* quantity


print(f"Remaining Gold: {Gold}")