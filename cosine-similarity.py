norm = lambda x:sum([y**2 for y in x])**.5
dot = lambda x,y:sum([a*b for a, b in zip(x,y)])
cos = lambda x,y:dot(x,y)/norm(x)/norm(y)
import scipy.spatial
1 - cos([1,2,3],[1,2,0])
scipy.spatial.distance.cosine([1,2,3],[1,2,0])

euclidean = lambda x,y: sum([(a-b)**2 for a, b in zip(x,y)])**0.5
euclidean([1,2,3],[1,2,0])
scipy.spatial.distance.euclidean([1,2,3],[1,2,0])

