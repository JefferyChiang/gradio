import gradio as gr
import time, random

def calculator(num1, operation, num2):
    time.sleep(5 + random.random() * 3)
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


demo = gr.Interface(
    calculator,
    ["number", gr.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    "number",
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="test calculator",
    description="heres a sample toy calculator. enjoy!",
    flagging_options=["this", "or", "that"],
)

if __name__ == "__main__":
    demo.launch()
