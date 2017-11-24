import scipy as sp
import numpy as np


frame_num = 4  # frame settings
val = [(-1) for i in range(frame_num)]
frame = np.array(val)


def page_gen(total_num):
	page_sequence = np.random.randint(0, 10, size=[total_num])
	return page_sequence


def fif(page_sequence):
	stat2 = frame_num
	q = 0
	for i in range(0, len(page_sequence)):
		if page_sequence[i] not in frame and q != frame_num:
			frame[q] = page_sequence[i]
			q = q+1
		if q == frame_num:
			break
	for j in range(i+1, len(page_sequence)):
		if page_sequence[j] not in frame:
			stat2 = stat2 + 1
			temp = [10000 for i in range(frame_num)]
			count = np.array(temp)
			for k in range(j+1, len(page_sequence)):
				if (page_sequence[k] in frame) and (count[np.argwhere(frame == page_sequence[k])] == 10000):
					count[np.argwhere(frame == page_sequence[k])] = k
				if 10000 not in count:
					break
			frame[np.argwhere(count == np.max(count))[0]] = page_sequence[j]
	return stat2


def alg_lru_plus(page_sequence):
	stat2 = frame_num
	q = 0
	for i in range(0, len(page_sequence)):
		if page_sequence[i] not in frame and q != frame_num:
			frame[q] = page_sequence[i]
			q = q+1
		if q == frame_num:
			break
	for j in range(i+1, len(page_sequence)):
		if page_sequence[j] not in frame:
			stat2 = stat2 + 1
			mark = np.zeros(frame_num, dtype=np.int)
			if (j+1 < len(page_sequence)) and page_sequence[j+1] in frame:
				mark[np.argwhere(frame == page_sequence[j+1])] = 1
			for k in range(j-1, -1, -1):
				if page_sequence[k] in frame:
					mark[np.argwhere(frame == page_sequence[k])] = 1
				if 0 not in mark:
					frame[np.argwhere(frame == page_sequence[k])] = page_sequence[j]
					break

	return stat2


max_ratio = 0
for i in range(100):
	page = page_gen(1000)
	res1 = alg_lru_plus(page)
	res2 = fif(page)
	if (res1/res2) > max_ratio:
		max_ratio = res1/res2
print(max_ratio)

