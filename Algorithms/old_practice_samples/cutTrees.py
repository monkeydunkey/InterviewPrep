def cutOffTree(forest):
      """
      :type forest: List[List[int]]
      :rtype: int
      """
      x, y = 0, 0
      valAvoid = 0
      trees = []
      for i, r in enumerate(forest):
          for j, t in enumerate(r):
              if t > 1:
                  trees.append((i, j, t))
      trees = sorted(trees, key = lambda x: x[-1])

      if len(trees) == 0:
          return 0
      totalSteps = 0
      while len(trees):
          destX, desty, TreeHeight = trees.pop(0)
          distToTree = bfsPath(forest, (x, y), (destX, desty))
          if distToTree is None:
              return -1
          else:
              totalSteps += distToTree
              x, y = destX, desty
      return totalSteps

def getsucc(forest, pos, count):
      x, y = pos
      pos = []
      for hor in [-1,0,1]:
          dx = x + hor
          for ver in [-1,0,1]:
              if (hor == 0 and ver == 0) or (ver != 0 and hor != 0) :
                  continue
              dy = y + ver
              try:
                  if dx >=0 and dy >=0 and dy < len(forest[0]) and dx < len(forest) and forest[dx][dy] != 0:
                      pos.append(((dx, dy), count+1))
              except Exception as e:
                  print dx, dy, len(forest[0]), len(forest)
                  raise
      return pos

def bfsPath(forest, start, dest):
      que = [(start, ) + (0,)]
      pathLength = None
      seenStates = set()
      while len(que):
          pos, c = que.pop(0)
          if pos not in seenStates:
              seenStates.add(pos)
              if pos == dest:
                  pathLength = c
              else:
                  que.extend(getsucc(forest, pos, c))
          else:
              continue

      return pathLength

if __name__ == '__main__':
    print cutOffTree([[2395,206,0,5388],[4985,2866,0,1789],[0,0,7052,0],[0,3029,3327,685],[0,0,7846,0],[0,0,1542,0],[7577,0,2902,623],[2610,9817,0,8198]])
