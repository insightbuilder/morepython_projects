from argparse import ArgumentParser

parse = ArgumentParser()

parse.add_argument("-a", "--alpha", help="Sets the -a flag")
parse.add_argument("-b", "--beta", help="Sets the -a flag")
parse.add_argument("-c", "--curve", help="Sets the -a flag")

parse.add_argument("max", help="Required Max", type=int)
parse.add_argument("min", help="Required Min", type=int)
parse.add_argument("med", help="Required Med", type=int)

parse.add_argument("args", nargs="*")
parse.add_argument("plusargs", nargs="+")
parse.add_argument("minusargs")


your_args = parse.parse_args()

print(your_args.alpha)
print(your_args.beta)
print(your_args.curve)

print(your_args.max)
print(your_args.min)
print(your_args.med)

print(your_args.args)
print(your_args.plusargs)

print(your_args)
