class Point:
    def reset(self):
        self.x = 0
        self.y = 0
        
p = Point()
p.reset()
print(p.x, p.y)

p2 = Point()
Point.reset(p2)
print(p2.x, p2.y)