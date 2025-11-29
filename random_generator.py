"""
随机数生成器模块
"""

import random
import time

class RandomGenerator:
    """随机数生成器类"""
    
    def __init__(self, seed=None):
        """
        初始化随机数生成器
        
        Args:
            seed: 随机数种子，如果为None则使用系统时间
        """
        if seed is None:
            seed = int(time.time())
        random.seed(seed)
        self.seed = seed
    
    def generate(self, min_val=1, max_val=100):
        """
        生成指定范围内的随机整数
        
        Args:
            min_val: 最小值（包含）
            max_val: 最大值（包含）
            
        Returns:
            int: 生成的随机数
        """
        if min_val > max_val:
            min_val, max_val = max_val, min_val
            
        return random.randint(min_val, max_val)
    
    def get_seed(self):
        """获取当前使用的种子"""
        return self.seed

# 使用示例
if __name__ == "__main__":
    generator = RandomGenerator()
    random_num = generator.generate(1, 100)
    print(f"生成的随机数: {random_num}")
    print(f"使用的种子: {generator.get_seed()}")
