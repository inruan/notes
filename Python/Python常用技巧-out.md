<!-- 该文件由"Python常用技巧.md"文件编译生成请勿直接编辑 -->
* 原地交换两个数

```python
a = 10
b = 20
a, b = b, a
print(b, a)
print(a, b)
```

 输出:

```
10 20
20 10
```


* 链状比较

```python
n = 10
print(6 < n < 20)
print(11 < n < 20)
```

 输出:

```
True
False
```


* 三元组操作

```python
# [表达式为真的返回值] if [表达式] else [表达式为假的返回值]

a = 10
b = 1 if a == 0 else 0
print(b)

```

 输出:

```
0
```


* 列表推导

```python
a = [1,4,5,6,2,8,3,7,9]
b = [i for i in a if i > 5]
print(b)

c = [(0,1), (2,3), (4,6)]
d = [r[1] for r in c]
print(d)
```

 输出:

```
[6, 8, 7, 9]
[1, 3, 6]
```


* 列表/元组切片

```python
a = [1,2,3,4,5,6] # (1,2,3,4,5,6)
b = a[2:]
c = a[1:2]  # 半闭半开
print(b)
print(c)
```

 输出:

```
[3, 4, 5, 6]
[2]
```


* 列表中某元素出现的次数

```python
a = [1,2,3,3,2,4,5]
print(a.count(2))

```

 输出:

```
2
```


* 统计列表中元素次数

```python
a = [1,2,3,3,2,4,5]
# 方法1
from collections import Counter
b = Counter(a)
print(b)

# 方法2
c = {
    i: a.count(i) for i in set(a)
}
print(c)
```

 输出:

```
Counter({2: 2, 3: 2, 1: 1, 4: 1, 5: 1})
{1: 1, 2: 2, 3: 2, 4: 1, 5: 1}
```


* 列表去重

```python
a = [1,2,3,3,2,4,5]
b = list(set(a))
print(a, b)
```

 输出:

```
[1, 2, 3, 3, 2, 4, 5] [1, 2, 3, 4, 5]
```


* 字典推导

```python
a = [['name','Robin'], ['age',30]]
b = {
    r[0]: r[1] for r in a
}
print(b)

```

 输出:

```
{'name': 'Robin', 'age': 30}
```


* 字典生成

```python
a = [['name','Robin'], ['age',30]]
b = dict(a)
print(b)
```

 输出:

```
{'name': 'Robin', 'age': 30}
```


* 字典转元组

```python
a = {'name':'Robin', 'age':30}
print(list(a.items()))
```

 输出:

```
[('name', 'Robin'), ('age', 30)]
```


* 元素打包

```python
a = [1,2,3,4]
b = ['a','b','c','d']
c = zip(a, b)
print(list(c))

```

 输出:

```
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```


* 字符串重复

```python
a = 'a'
b = a * 10
print(b)
```

 输出:

```
aaaaaaaaaa
```


* 字符串拼接

```python
a = ['Hello', 'World', '!']
b = '~'.join(a)
print(b)
```

 输出:

```
Hello~World~!
```


* 字符串包含

```python
a = 'Hello World !'
print('World' in a)
print('abc' in a)
```

 输出:

```
True
False
```


* 简化if操作

```python
a = 1
if a == 1 or a == 2 or a == 3 or a == 8: pass # 不推荐做法
if a in [1,2,3,8,9]: pass # 推荐做法
```

 输出:

```

```


* 获取索引和元素

```python
# 丑代码
a = ['A', 'B', 'C']
n = 0
for i in a:
    print(n, i)
    n += 1
    
for i in range(len(a)):
    print(i, a[i])

# 推荐代码
for n, i in enumerate(a):
    print(n, i)
```

 输出:

```
0 A
1 B
2 C
0 A
1 B
2 C
0 A
1 B
2 C
```


* 函数参数

```python
def test(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

test(1,2)

test(1,2,3,4,t=5)

n = [4,5]
m = {'x':6, 'y':7}
test(1,2, *n, **m)  # 结构传递，等同test(1,2,3,4,x=6,y=7)
```

 输出:

```
1 2 () {}
1 2 (3, 4) {'t': 5}
1 2 (4, 5) {'x': 6, 'y': 7}
```


* map函数

```python
a = [{'name':'A', 'id':1}, {'name':'B', 'id':2}]
b = map(lambda d:d['id'], a)
print(list(b))

# 列表推导实现
c = [d['id'] for d in a]
print(c)
```

 输出:

```
[1, 2]
[1, 2]
```


* filter函数

```python
a = [1,4,5,6,2,8,3,7,9]
b = filter(lambda i: i > 5, a)
print(list(b))

# 列表推导实现
c = [i for i in a if i > 5]
print(c)
```

 输出:

```
[6, 8, 7, 9]
[6, 8, 7, 9]
```


* max、min、sum函数

```python
a = [1,2,3,3,2,4,5]
print(max(a))
print(min(a))
print(sum(a))
```

 输出:

```
5
1
20
```


* 用字典简化if

```python
# 丑代码
a = 1
if a == 1:
    b = 'A'
elif a == 2:
    b = 'B'
else:
    b = 'C'
print(b)

# 简化代码
d = {1:'A', 2:'B'}
b = d.get(a, 'C')
print(b)
```

 输出:

```
A
A
```
