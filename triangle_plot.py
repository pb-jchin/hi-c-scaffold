import argparse, os, sys
import matplotlib.pyplot as plt

def main():
	parser = argparse.ArgumentParser()
    parser.add_argument("-a","--alignment",help="bed file for alignment")
    parser.add_argument("-o","--output",help="file to save the plot")
    args = parser.parse_args()

    cmd = './triangle_plot -a {alignment} -o {coords}'.format(alignment = args.alignment, coords = 'coords')

    os.system(cmd)

    x = []
    y = []

    with open('coords','r') as f:
    	lines = f.readlines()
    	attrs = line.split()
    	x.append(float(attrs[0]))
    	y.append(float(attrs[1]))

    plt.scatter(x,y,alpha=0.05)
    plt.xlabel('Midpoints between two mates')
    plt.ylabel('Distance between two mates')
    plt.title('Triangle Plot')
    plt.savefig(args.output)


if __name__ == '__main__':
	main()