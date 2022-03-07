import bisect
import itertools

N = int(input())
ais = [int(x) for x in input().split()]
intervals = []
cur_interval = []
cur_height = 0
total_sequences = 0
for i, ai in enumerate(ais):
  if ai < cur_height:
    merged = True
    while merged:
      if not intervals or intervals[-1][-1] > cur_interval[-1]:
        intervals.append(cur_interval)
        break
      pi = intervals.pop()
      mpi_top = bisect.bisect_right(pi, cur_interval[0])
      pi[mpi_top:] = cur_interval
      cur_interval = pi
    cur_interval = []
  cur_height = ai
  cur_interval.append(ai)
  total_sequences += len(cur_interval)
  prev_min = cur_interval[0]
  for prev_interval_i in range(len(intervals) - 1, -1, -1):
    pi = intervals[prev_interval_i]
    if pi[-1] > ai: break
    pi_lower = bisect.bisect_right(pi, prev_min)
    if pi_lower > 0: prev_min = pi[0]
    total_sequences += pi_lower
print(total_sequences)