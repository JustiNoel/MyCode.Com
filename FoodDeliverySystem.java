import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class FoodDeliverySystem {

    static class FoodItem {
        int id;
        String name;
        String category;
        double price;

        FoodItem(int id, String name, String category, double price) {
            this.id = id;
            this.name = name;
            this.category = category;
            this.price = price;
        }
    }

    static class Order {
        List<FoodItem> items = new ArrayList<>();
        double taxRate = 0.1; // 10% tax
        double tipRate = 0.15; // 15% tip

        void addItem(FoodItem item) {
            items.add(item);
        }

        void removeItem(FoodItem item) {
            items.remove(item);
        }

        double calculateTotal() {
            double total = 0;
            for (FoodItem item : items) {
                total += item.price;
            }
            total += total * taxRate; // Adding tax
            total += total * tipRate; // Adding tip
            return total;
        }

        void printReceipt() {
            System.out.println("Receipt:");
            for (FoodItem item : items) {
                System.out.println(item.name + " - $" + item.price);
            }
            System.out.printf("Total (including tax and tip): $%.2f%n", calculateTotal());
        }
    }

    public static void main(String[] args) {
        Map<Integer, FoodItem> menu = new HashMap<>();
        menu.put(1, new FoodItem(1, "Spring Rolls", "Appetizer", 5.99));
        menu.put(2, new FoodItem(2, "Grilled Chicken", "Main Course", 12.99));
        menu.put(3, new FoodItem(3, "Cheesecake", "Dessert", 4.99));
        menu.put(4, new FoodItem(4, "Soda", "Beverage", 1.99));

        Scanner scanner = new Scanner(System.in);
        Order order = new Order();
        boolean ordering = true;

        while (ordering) {
            System.out.println("Menu:");
            for (FoodItem item : menu.values()) {
                System.out.println(item.id + ". " + item.name + " - $" + item.price);
            }
            System.out.println("Select an item by ID to add to your order, or type 0 to finalize your order:");

            int choice = scanner.nextInt();
            if (choice == 0) {
                ordering = false;
            } else if (menu.containsKey(choice)) {
                order.addItem(menu.get(choice));
                System.out.println(menu.get(choice).name + " added to your order.");
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }

        order.printReceipt();
        scanner.close();
    }
}
