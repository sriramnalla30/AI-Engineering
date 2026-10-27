import numpy as np
import math 

a = np.array([1, 2, 3, 4])

b = np.array([-2, 1, -4, 3]) 

print('Vector a : ', a)
print('Vector b : ', b)

numerator = np.dot(a, b) 

x = 0
for i in a:
    x += i * i

y = 0
for i in b:
    y += i * i

denominator = math.sqrt(x) * math.sqrt(y)
print('cosine similarity : ', numerator / denominator)

# #vector b [-1,-2,-3,-4] says the vectors in opposite direction returns -1 meaning 
# the same topic in opposite perspectives
# example: the move is great vs the movie is worst
# #vector b [-2, 1, -4, 3]says the vectors in orthogonal/perpendicular  returns 0 meaning there are not related in meaning/topic etc.
# example: the goat is black vs India will be developing country
# #vector b [1,2,3,4]says the vectors are in same direction meaning 
# the both sentences are talking about the same topic 
# example: the weather is great vs the climate is good