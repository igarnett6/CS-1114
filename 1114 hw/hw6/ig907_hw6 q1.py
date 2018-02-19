
def print_shifted_triangle(n, symbol, m = 0):
    y = n-1
    for j in range (n):
        print(m*" ", y * " ", j * symbol, symbol, j * symbol, sep="")
        y-=1

def print_pine_tree(n, symbol):
    for i in range(n+1):
        print_shifted_triangle(i, symbol)

def main():
    n = int(input("Enter a positive integer: "))
    m = int(input("Enter the marginal shift: "))
    symbol = input("Enter the symbol: ")
    print("Shifted triangle:\n")
    print_shifted_triangle(n, symbol, m)
    print("\nPine cone tree: \n")
    print_pine_tree(n, symbol)
main()