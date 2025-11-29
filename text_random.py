"""
测试随机数生成器
"""

from random_generator import RandomGenerator

def test_random_generator():
    """测试随机数生成器功能"""
    print("=== 随机数生成器测试 ===")
    
    # 测试默认生成
    generator1 = RandomGenerator()
    result1 = generator1.generate(1, 10)
    print(f"测试1 - 范围1-10: {result1}")
    
    # 测试指定种子（可重现结果）
    generator2 = RandomGenerator(seed=123)
    result2 = generator2.generate(1, 100)
    print(f"测试2 - 指定种子123: {result2}")
    
    # 测试范围反转自动修正
    generator3 = RandomGenerator()
    result3 = generator3.generate(10, 1)  # 范围会自动修正
    print(f"测试3 - 反转范围10-1: {result3}")
    
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_random_generator()
