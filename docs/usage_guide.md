# 使用指南

## 基本用法

### 1. 导入模块
```python
from random_generator import RandomGenerator
# 使用系统时间作为种子
generator = RandomGenerator()

# 或指定固定种子（用于重现结果）
generator = RandomGenerator(seed=123)

# 生成 1-100 的随机数
random_num = generator.generate(1, 100)

# 生成 0-1 的随机数
random_num = generator.generate(0, 1)

seed = generator.get_seed()
print(f"当前使用的种子: {seed}")
