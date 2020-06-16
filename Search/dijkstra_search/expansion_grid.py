# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    # for i in expand:
    #     print(i)

    x = init[0]
    y = init[1]
    g = 0
    count = 0
    expand[x][y] = count

    open = [[g, x, y]]

    found = False  # goal is found
    resign = False  # goal not found

    # print("Initial open list:")
    # for i in range(len(open)):
    #     print(" ", open[i])
    # print("___")

    while found is False and resign is False:

        # check if we still have elements on open list
        if len(open) == 0:
            resign = True
            print("fail")

        else:
            # remove node from list
            open.sort()
            next = open.pop(0)
            # print("take list item")
            # print(next)

            # print("Open list:")
            # for i in range(len(open)):
            #     print(" ", open[i])
            # print("___")

            x = next[1]
            y = next[2]
            g = next[0]

            # check if we are done

            if x == goal[0] and y == goal[1]:
                found = True
                # print(next)
                # print("goal found!")
            else:
                # expand winning element and add to new open list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            # print("append list item")
                            # print(g2, x2, y2)
                            closed[x2][y2] = 1
                            count += 1
                            expand[x2][y2] = count

    # ----------------------------------------
    #expand = None
    return expand


result = search(grid, init, goal, cost)
print("Initial grid")
for line in grid:
    print(line)
print("Expand grid")
for i in result:
    print(i)
