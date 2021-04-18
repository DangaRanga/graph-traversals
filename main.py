
# Global imports
import sys
# import graph
# import traversals

# Global Variables
exit_options = ["EXIT", "0", ""]
# Lexicographical options
lex_options = {"EARLY": False, "LATE": True, "LATEST": True,
               "1": False, "2": True, "E": False, "L": True}

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


def graph_menu():

    # Present Menu
    print()
    print("######################################")
    print("# 0 - EXIT                           #")
    print("# 1 - BFS | Breadth First            #")
    print("# 2 - Dijkstra's                     #")
    print("# 3 - DFS | Depth First              #")
    print("######################################")


# -----------------------------------------------------
# Main for Graphs


def graph_main():

    # Valid Options
    bfs_options = ["1", "BFS", "BREADTH", "BREATH"]
    dfs_options = ["2", "DFS", "DEPTH"]
    dijk_options = ["3", "DIJK", "DJ"]

    # Infinite Loop
    while (True):
        # Present Menu & get user option
        graph_menu()
        option = input("# Option - ").rstrip()
        option = option.upper()

        # Check for valid options
        if (option in bfs_options):
            bfs_main()
        elif (option in dfs_options):
            dfs_main()
        elif (option in dijk_options):
            dijkstra_main()
        elif (option in exit_options):
            break
        else:
            print("\n--------------------------------------")
            print(f"# {option} | Not Valid - Try Again")
            print("--------------------------------------\n")


# BFS Main
# -----------------------------------------------------
def bfs_main():
    # Intro
    print()
    print("####################################")
    print("# BFS")
    print("####################################")

    # Get the graph
    graph = create_graph()

    # Get lexicographically Early or Latest
    print()
    print("####################################")
    print("# Lexicographically                #")
    print("####################################")
    print("# 1 - EARLY                        #")
    print("# 2 - LATEST                       #")
    print("#----------------------------------#")

    # Get the latest boolean
    latest_option = input("# ").rstrip()
    latest_option = latest_option.upper()
    if latest_option in lex_options.keys():
        latest = lex_options[latest_option]
    else:
        print("\n--------------------------------------")
        print(f"# {latest_option} | Not Valid - False will be used as default value")
        print("--------------------------------------\n")
    print("####################################")

    print()
    print("####################################")
    starting_node = input("# Start Node = ").rstrip()
    starting_node = starting_node.upper()
    print("####################################")

    print(f"{graph}\n{latest}\n{starting_node}")

# DFS Main
# -----------------------------------------------------


def dfs_main():
    # Intro
    print()
    print("####################################")
    print("# DFS")
    print("####################################")

    # Get the graph
    graph = create_graph()

    # Get lexicographically Early or Latest
    print()
    print("####################################")
    print("# Lexicographically                #")
    print("####################################")
    print("# 1 - EARLY                        #")
    print("# 2 - LATEST                       #")
    print("#----------------------------------#")

    # Get the latest boolean
    latest_option = input("# ").rstrip()
    latest_option = latest_option.upper()
    if latest_option in lex_options.keys():
        latest = lex_options[latest_option]
    else:
        print("\n--------------------------------------")
        print(f"# {latest_option} | Not Valid - False will be used as default value")
        print("--------------------------------------\n")
    print("####################################")

    print()
    print("####################################")
    starting_node = input("# Start Node = ").rstrip()
    starting_node = starting_node.upper()
    print("####################################")

    print(f"{graph}\n{latest}\n{starting_node}")

# DIJKSTRA Main
# -----------------------------------------------------


def dijkstra_main():
    pass

# -----------------------------------------------------
# Main for Traversals


def traversal_main():
    print("Traversal Status: Not ready")

# -----------------------------------------------------
# Create Graph


def create_graph():
    graph = dict()

    print()
    print("#--------------------------------------")
    print("# Enter Format --> NODE : Neighbours")
    print("#--------------------------------------")

    user_input = "GO"
    while (True):
        user_input = input("# ").rstrip()
        user_input = user_input.upper()

        if len(user_input) == 0:
            break
        # -----------------------

        try:
            # Split up input
            broken = user_input.split(":")
            node, neighbor = broken[0].strip(), broken[1]
        except ValueError:
            print("\n--------------------------------------")
            print(f"# An error occurred.")
            print("--------------------------------------\n")

        # Assign values to graph
        graph[node] = neighbor

    print("#--------------------------------------")

    return graph


# Driver -----------------------------------------------------
if __name__ == "__main__":
    # Menu Options
    graph_options = ["1", "GRAPH", "GRAPHS"]
    traversal_options = ["2", "TRAVERSAL", "TRAVERSALS"]

    print()
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
