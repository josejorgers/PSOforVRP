import pso, sys

# if __name__ == '__main__':

    # if len(sys.argv) != 2:
    #     print('Usage: run <clients> where clients stands for how many clients the problem has')
    # c = int(sys.argv[1])
s = pso.pso(12)
for r in s:
    print(r)

