class ReflexAgent:
    def __init__(self, required_temp):
        self.required_temp = required_temp
        self.history = {}

    def act(self, room_name, current_temp):
        if current_temp < self.required_temp:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        
        self.history[room_name] = action
        return action

    def get_history(self):
        return self.history

def user_temp():
    rooms = {}
    num_rooms = int(input("Enter the number of rooms: "))
    
    for i in range(num_rooms):
        room_name = input("Enter room name: ")
        room_temp = float(input(f"Enter current temperature for {room_name}: "))
        rooms[room_name] = room_temp
    return rooms

def main():
    print("Welcome to Temperature Control System")
    
    required_temp = float(input("Enter the required temperature for rooms (°C): "))
    
    rooms = user_temp()
    agent = ReflexAgent(required_temp)

    print("\nRunning the AI for each room...\n")
    
    for room, temperature in rooms.items():
        action = agent.act(room, temperature)
        print(f"{room}: Current temperature = {temperature}°C. {action}.")
    
    print("\nAction history:")
    for room, action in agent.get_history().items():
        print(f"{room}: {action}")

main()
