import math

m = 0.00000628
Pe = 0.22
λ = 1550*10**3
b = 3.5
c = 2.5
t = 0.6
e = 10
h = 3.6
w = 5
Af = 0.01227
Ef = 70000
l = 5
# 质量块的质心到椭圆铰链中心的距离d为
d = b+e/2
E = 210000
a = 9.8*10**3
# k表示光纤弹性系数
k=(Af*Ef)/l
# c表示椭圆铰链的短半轴，t表示铰链间最小厚度

s=c/t
# U 是转动惯量
u1 = ((12*s**3+14*s**2+6*s+1)/((2*s+1)**2*(4*s+1)**2))
u2 = (6*s*(2*s+1)*(math.atan(1/(math.sqrt(4*s+1))))/math.sqrt((4*s+1)**5))
u3 = (6*s*(8*s**3+12*s**2+6*s+1)*(math.atan(2*s/(math.sqrt(4*s+1))))/math.sqrt((4*s+1)**5)/(2*s+1)**2)
U = u1+u2+u3

# K表示椭圆铰链的转动刚度
K = (E*w*t**3)/(24*b*U)
# S是灵敏度
S = ((1-Pe)*λ/l)*(m*d)/(k*h/2+(2*K/h))
#Q θ表示椭圆铰链的转动角度=Δl表示长度为l的光栅在质量块拉伸作用下的伸长量=Q
Q = (2*m*a*d)/(k*h+2*K)

J = m*(e**2+h**2)/12 + m*d**2

f = (1/(2*3.14))*math.sqrt((k*(h/2)**2+K)/J)
print(d,S,k,K,U,Q,f)