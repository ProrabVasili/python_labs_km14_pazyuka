import re
p = re.compile(r'0\...')
s = "[BodyPart:0-(0.56, 0.23) score=0.80 BodyPart:1-(0.57, 0.33) score=0.79 BodyPart:2-(0.52, 0.35) score=0.70 BodyPart:3-(0.46, 0.40) score=0.69 BodyPart:4-(0.36, 0.41) score=0.84 BodyPart:5-(0.61, 0.32) score=0.72 BodyPart:6-(0.61, 0.21) score=0.58 BodyPart:7-(0.59, 0.11) score=0.80 BodyPart:8-(0.56, 0.52) score=0.43 BodyPart:9-(0.61, 0.65) score=0.36 BodyPart:10-(0.60, 0.80) score=0.63 BodyPart:11-(0.59, 0.51) score=0.50 BodyPart:12-(0.56, 0.65) score=0.50 BodyPart:13-(0.53, 0.80) score=0.69 BodyPart:14-(0.55, 0.22) score=0.64 BodyPart:15-(0.57, 0.22) score=0.67 BodyPart:17-(0.60, 0.24) score=0.33]"
f = p.findall(s)
points, scores = [float(f[i]) for i in range(len(f)) if i%3!=2], [float(f[i]) for i in range(len(f)) if i%3==2]
print(f'points = {points}',f'scores = {scores}', sep='\n')
