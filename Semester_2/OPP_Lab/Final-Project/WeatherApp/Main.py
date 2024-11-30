from MenuHandler import MenuHandler

API_KEY = "30d4741c779ba94c470ca1f63045390a"

def main():
    menu = MenuHandler(API_KEY)
    menu.display_menu()

if __name__ == "__main__":
    main()
