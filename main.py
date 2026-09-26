import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/ medium/ large/ report/ off): ").lower().strip()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice in recipes:
            sandwich = recipes[choice]
            order_ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(order_ingredients):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, cost):
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)
        else:
            print("Invalid choice. Please choose small, medium, large, report, or off.")


if __name__ == "__main__":
    main()