
# Global imports
import sys
# import graph
# import traversals

# ---------- Menu Options -----------------------------


def menu():
    """
    Displays the menu of the program.

    Args:
        None

    Returns:
        None
    """

    # Present Menu
    print("######################################")
    print("# Enter EXIT | 0 | Blank - to exit   #")
    print("######################################")
    print("# Enter the Number OR Name:          #")
    print("# 1 - Graphs                         #")
    print("# 2 - Traversals                     #")
    print("######################################")


# -----------------------------------------------------
# Main for Graphs


def graph_main():
    print("Graph Status: Not ready")

# -----------------------------------------------------
# Main for Traversals


def traversal_main():
    print("Traversal Status: Not ready")

# -----------------------------------------------------


# Driver -----------------------------------------------------
if __name__ == "__main__":
    # Menu Options
    exit_options = ["EXIT", "0", ""]
    graph_options = ["1", "GRAPH", "GRAPHS"]
    traversal_options = ["2", "TRAVERSAL", "TRAVERSALS"]

    print("######################################")
    print("#               WELCOME              #")
    print("######################################")
    print()

    option = "START"

    # Infinite Loop
    while (True):
        # Present Menu & get user option
        menu()
        option = input("# Option - ").rstrip()
        option = option.upper()

        # Check for valid options
        if (option in graph_options):
            graph_main()
        elif (option in traversal_options):
            traversal_main()
        elif (option in exit_options):
            break
        else:
            print("\n--------------------------------------")
            print(f"# {option} | Not Valid - Try Again")
            print("--------------------------------------\n")

    # Exits -----------------------------------------------
    print("\n######################################")
    print("#           Ending Program           #")
    print("######################################")
    sys.exit()
