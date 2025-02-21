class Reflex_Agents:
    def __init__(self, required_temp):
        self.required_temp = required_temp
        self.previous_action = None

    def perceive(self, current_temp):
        return current_temp

    def act(self, current_temp):
        if current_temp < self.required_temp:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        
        if action == self.previous_action:
            return "No change"
        
        self.previous_action = action
        return action

def user_temp():
    rooms = {}
    num_rooms = int(input("Enter the number of rooms: "))
    
    for i in range(num_rooms):
        room_name = input("Enter room name: ")
        room_temp = float(input(f"Enter current temperature for {room_name}: "))
        rooms[room_name] = room_temp
        i += 1    
    return rooms

def main():
    print("Welcome to Temperature Control System")
    
    required_temp = float(input("Enter the required temperature for rooms (°C): "))
    
    rooms = user_temp()
    agent = Reflex_Agents(required_temp)

    print("\nRunning the AI for each room...\n")
    
    for room, temperature in rooms.items():
        action = agent.act(temperature)
        print(f"{room}: Current temperature = {temperature}°C. {action}.")
        
main()
