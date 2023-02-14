import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello there! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. How can I assist you today?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you for asking. How can I assist you today?"]
    ],
    [
        r"tell me about your health features|what can you do for health?",
        ["I can help you with basic health information, such as calculating your BMI, suggesting some exercises or providing some nutritional advice. Just let me know what you need help with!"]
    ],
    [
        r"what is bmi|calculate bmi|how to calculate bmi",
        ["BMI stands for Body Mass Index, which is a measure of body fat based on height and weight. To calculate your BMI, you can use the formula: BMI = (weight in kg) / (height in meters squared). Would you like me to calculate your BMI?"]
    ],
    [
        r"yes",
        ["Sure! Can you please tell me your weight in kilograms?"]
    ],
    [
        r"(\d+(\.\d+)?)",
        ["Great! And what is your height in meters?"]
    ],
    [
        r"(\d+(\.\d+)?)",
        ["Your BMI is %.2f. A healthy BMI range is between 18.5 and 24.9. Let me know if you have any questions about this." % (float(nltk.chat.util.reflections.get("matches")[0]))]
    ],
    [
        r"what are some exercises for beginners?",
        ["Some good exercises for beginners include walking, jogging, cycling, and swimming. Would you like me to suggest a beginner's workout routine?"]
    ],
    [
        r"yes",
        ["Sure, here is a beginner's workout routine you can try:\n\n1. 10-minute warm-up (stretching or light cardio)\n2. 20-minute strength training (push-ups, squats, lunges, etc.)\n3. 20-minute cardio (jogging, cycling, etc.)\n4. 10-minute cool-down (stretching or light yoga)\n\nRemember to start slowly and gradually increase the intensity and duration of your workouts. Let me know if you have any questions!"]
    ],
    [
        r"what are some healthy foods|what should i eat to stay healthy?",
        ["Some healthy foods include fruits, vegetables, whole grains, lean protein sources (such as fish, chicken, or beans), and healthy fats (such as nuts, seeds, or avocado). Do you have any specific dietary concerns?"]
    ],
    [
        r"tell me about your finance features|what can you do for finance?",
        ["I can help you with basic financial information, such as currency conversion rates, stock prices, and budgeting advice. Just let me know what you need help with!"]
    ],
    [
        r"what is the conversion rate between (.*) and (.*)?",
        ["Sorry, I am not currently able to check currency conversion rates. However, you can easily find this information online through various currency exchange websites. Is there anything else I can assist you with?"]
    ],
    [
        r"what is the stock price of (.*)?",
        ["Sorry, I am not currently able to check stock prices. However, you can easily find this information online through various financial news websites or by using a stock market tracking app. Is there anything else I can assist you with?"]
    ],
    [
        r"how can i save money|what are some budgeting tips?",
        ["Some good budgeting tips include:\n\n1. Set financial goals (such as saving for a down payment on a house or paying off debt)\n2. Create a budget that tracks your income and expenses\n3. Cut unnecessary expenses (such as eating out or buying expensive coffee)\n4. Look for ways to increase your income (such as taking on a side job or freelancing)\n\nRemember to be patient and persistent, and don't hesitate to ask for help if you need it. Let me know if you have any questions!"]
    ],
    [
        r"thank you|thanks|bye|goodbye",
        ["You're welcome! Have a great day."]
    ]
]

def finance_chat():
    print("Welcome to the finance chatbot. Please enter your message to get started!")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    finance_chat()
