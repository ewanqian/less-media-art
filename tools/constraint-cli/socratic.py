#!/usr/bin/env python3
"""
苏格拉底模式 - 十轮批判对话
让AI扮演提问者，通过对话显形思维过程
"""

import json
import sys
from datetime import datetime
from pathlib import Path


class SocraticDialogue:
    """十轮批判对话管理器"""
    
    def __init__(self, topic: str, model: str = "llama3.2:3b"):
        self.topic = topic
        self.model = model
        self.current_round = 0
        self.max_rounds = 10
        self.dialogue_history = []
        self.start_time = datetime.now()
        
    def generate_question(self, user_response: str = None) -> str:
        """生成AI问题"""
        # 在实际实现中，这里应该调用Ollama API
        # 现在使用模拟的问题模板
        
        questions = [
            f"你想探索'{self.topic}'，能告诉我是什么吸引你关注这个话题吗？",
            "你刚才的回答中，有一个潜在的假设，你能识别出来吗？",
            "如果这个假设不成立，你的观点会有什么变化？",
            "有没有一个具体的例子可以支持你的说法？",
            "相反的观点会怎么反驳你？",
            "你在这个话题上的立场，和你个人的经历有什么关系？",
            "如果五年后再看这个问题，你可能会怎么看？",
            "你现在的观点和第一轮相比，有什么变化吗？",
            "如果要用一句话概括你的核心洞察，会是什么？",
            "这次对话让你对自己有了什么新的认识？"
        ]
        
        if self.current_round < len(questions):
            return questions[self.current_round]
        else:
            return "还有什么你想补充的吗？"
    
    def run(self):
        """运行十轮对话"""
        print(f"\n{'='*60}")
        print(f"苏格拉底模式 - 十轮批判对话")
        print(f"主题: {self.topic}")
        print(f"{'='*60}\n")
        
        print("规则:")
        print("1. AI只会提问，不会直接回答")
        print("2. 每轮你必须回应，不能跳过")
        print("3. 共10轮，结束后生成对话档案")
        print("4. 输入 'quit' 可提前结束\n")
        
        while self.current_round < self.max_rounds:
            self.current_round += 1
            
            # 生成问题
            question = self.generate_question()
            
            print(f"\n[{self.current_round}/10] AI: {question}")
            print("-" * 60)
            
            # 获取用户输入
            try:
                user_input = input("你: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n对话被中断")
                break
            
            if user_input.lower() == 'quit':
                print("\n对话提前结束")
                break
            
            if not user_input:
                print("请输入你的回应（不能跳过）")
                self.current_round -= 1
                continue
            
            # 记录对话
            self.dialogue_history.append({
                "round": self.current_round,
                "ai_question": question,
                "user_response": user_input,
                "timestamp": datetime.now().isoformat()
            })
        
        # 结束对话
        self.finish()
    
    def finish(self):
        """结束对话，生成档案"""
        print(f"\n{'='*60}")
        print("对话结束")
        print(f"{'='*60}\n")
        
        # 生成档案
        archive = self.generate_archive()
        
        # 保存到文件
        filename = f"socratic_{self.topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = Path.home() / ".less-media-art" / "archives" / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(archive, f, ensure_ascii=False, indent=2)
        
        print(f"对话档案已保存: {filepath}")
        print(f"\n反思问题:")
        print("1. 哪一轮的问题最让你意外？为什么？")
        print("2. 你的观点在对话中如何演变？")
        print("3. 如果没有AI的追问，你会得出同样的结论吗？")
        print("4. 这次对话揭示了你什么思维模式？")
    
    def generate_archive(self) -> dict:
        """生成对话档案"""
        return {
            "type": "socratic_dialogue",
            "topic": self.topic,
            "metadata": {
                "start_time": self.start_time.isoformat(),
                "end_time": datetime.now().isoformat(),
                "total_rounds": len(self.dialogue_history),
                "model": self.model
            },
            "dialogue": self.dialogue_history,
            "reflection_prompts": [
                "哪一轮的问题最让你意外？为什么？",
                "你的观点在对话中如何演变？",
                "如果没有AI的追问，你会得出同样的结论吗？",
                "这次对话揭示了你什么思维模式？"
            ]
        }


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='苏格拉底模式 - 十轮批判对话')
    parser.add_argument('--topic', '-t', required=True, help='对话主题')
    parser.add_argument('--model', '-m', default='llama3.2:3b', help='使用的AI模型')
    
    args = parser.parse_args()
    
    # 创建对话实例
    dialogue = SocraticDialogue(topic=args.topic, model=args.model)
    
    # 运行对话
    dialogue.run()


if __name__ == "__main__":
    main()
