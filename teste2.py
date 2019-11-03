import mpimap
import time

def func_cheap(*args):
	"""Do nothing"""
	return


def func_expensive(n):
	"""Basic factorising problem"""
	factors = set([])
	for i in xrange(n - 1):
		i = i + 1
		# Skip factors
		if i in factors:
			continue
		# Find factors
		if n % i == 0:
			factors.add(i)
			factors.add(n / i)

	return sorted(factors)


# Build mpi
mpi = mpimap.Mpimap(sleep=0, debug=False)
mpi.info()
mpi.start()

# Run function on all nodes
mpi.run(func_cheap)

# Set up function and arguments
args = range(5000, 10000)

# Not in parallel
t0 = time.time()
res = map(func_expensive, args)
dt = time.time() - t0
print('\nNon Parallel: {}'.format(dt))

# Parallel
t0 = time.time()
res = mpi.map(func_expensive, args)
dt = time.time() - t0
print('\nParallel: {}\n'.format(dt))

mpi.stop()
mpi.exit()