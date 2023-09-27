import discord
from discord.ext import commands
import random
import asyncio
import time

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Initialize variables to keep track of trivia statistics
total_questions_asked = 0
total_correct_answers = 0
user_scores = {}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print("You can now interact with the bot using the Discord server and in this terminal.")


@bot.command()
async def trivia(ctx):
    global total_questions_asked, total_correct_answers, user_scores

    print("\n" + "-" * 60)
    print(
        f'| {"Timestamp":<19} | {"User":<25} | {"Question":<40} | {"Answer":<20} | {"Result":<8} | {"Time (s)":<10} |')
    print("-" * 60)

    question = random.choice(trivia_questions)
    await ctx.send(f'**Trivia Question:**\n{question["question"]}')

    start_time = time.time()
    try:
        response = await bot.wait_for(
            'message',
            timeout=20,  # Set a time limit for answering (in seconds)
            check=lambda message: message.author == ctx.author
        )
        elapsed_time = time.time() - start_time

        total_questions_asked += 1

        if response.content.lower() == question['answer'].lower():
            total_correct_answers += 1
            if ctx.author.id in user_scores:
                user_scores[ctx.author.id] += 1
            else:
                user_scores[ctx.author.id] = 1
            result = "Correct"
        else:
            result = "Incorrect"

        print(
            f'| {get_timestamp():<19} | {ctx.author.name:<25} | {question["question"][:40]:<40} | {response.content[:20]:<20} | {result:<8} | {elapsed_time:<10.2f} |')
        print(f'| {"":<19} | {"":<25} | {"Correct Answer:":<40} | {question["answer"][:20]:<20} | {"":<8} | {"":<10} |')
    except asyncio.TimeoutError:
        result = "Timeout"
        elapsed_time = 20.0
        print(
            f'| {get_timestamp():<19} | {ctx.author.name:<25} | {question["question"][:40]:<40} | {"":<20} | {result:<8} | {elapsed_time:<10.2f} |')
        print(f'| {"":<19} | {"":<25} | {"Correct Answer:":<40} | {question["answer"][:20]:<20} | {"":<8} | {"":<10} |')
    finally:
        print("-" * 60)


def get_timestamp():
    return time.strftime('%Y-%m-%d %H:%M:%S')


# Your trivia questions here
trivia_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "How many continents are there in the world?", "answer": "7"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Which gas do plants absorb from the atmosphere during photosynthesis?", "answer": "Carbon dioxide"},
    {"question": "In which country can you find the Great Barrier Reef?", "answer": "Australia"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "In which year did the Titanic sink?", "answer": "1912"},
    {"question": "What ancient wonder was located in Alexandria, Egypt?", "answer": "The Lighthouse of Alexandria"},
    {"question": "Who wrote the 'I Have a Dream' speech?", "answer": "Martin Luther King Jr"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "How many continents are there in the world?", "answer": "7"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Which gas do plants absorb from the atmosphere during photosynthesis?", "answer": "Carbon dioxide"},
    {"question": "In which country can you find the Great Barrier Reef?", "answer": "Australia"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "In which year did the Titanic sink?", "answer": "1912"},
    {"question": "What ancient wonder was located in Alexandria, Egypt?", "answer": "The Lighthouse of Alexandria"},
    {"question": "Who wrote the 'I Have a Dream' speech?", "answer": "Martin Luther King Jr."},
    {"question": "Which war is also known as the First World War?", "answer": "World War I"},
    {"question": "What is the chemical symbol for the element gold?", "answer": "Au"},
    {"question": "How many bones are there in the adult human body?", "answer": "206"},
    {"question": "What is the freezing point of water in Fahrenheit?", "answer": "32°F"},
    {"question": "What is the process by which plants make their own food using sunlight?", "answer": "Photosynthesis"},
    {"question": "Who is known as the father of modern physics?", "answer": "Albert Einstein"},
    {"question": "Which African country is known as the 'Rainbow Nation'?", "answer": "South Africa"},
    {"question": "What is the longest river in the world?", "answer": "The Nile"},
    {"question": "In which country can you find the Andes Mountains?", "answer": "South America"},
    {"question": "What is the largest ocean in the world?", "answer": "The Pacific Ocean"},
    {"question": "Which city is located on the European and Asian continents?", "answer": "Istanbul"},
    {"question": "What is the most widely spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "Which gas is responsible for the Earth's greenhouse effect?", "answer": "Carbon dioxide"},
    {"question": "Who is the author of 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the national flower of Japan?", "answer": "Cherry blossom"},
    {"question": "What is the largest desert in the world?", "answer": "Antarctica"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart"},
    {"question": "In which year did the American Civil War begin?", "answer": "1861"},
    {"question": "What is the oldest known written language?", "answer": "Sumerian"},
    {"question": "Who painted the 'Mona Lisa'?", "answer": "Leonardo da Vinci"},
    {"question": "In which city was the Magna Carta sealed?", "answer": "Runnymede"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "What is the study of the Earth's atmosphere and weather?", "answer": "Meteorology"},
    {"question": "Who is known for formulating the laws of motion?", "answer": "Isaac Newton"},
    {"question": "Which mountain range runs along the border between Italy and Switzerland?", "answer": "The Alps"},
    {"question": "What is the largest lake in Africa?", "answer": "Lake Victoria"},
    {"question": "In which country is Mount Everest located?", "answer": "Nepal"},
    {"question": "What is the capital of New Zealand?", "answer": "Wellington"},
    {"question": "Which river flows through the Grand Canyon?", "answer": "Colorado River"},
    {"question": "What is the chemical symbol for silver?", "answer": "Ag"},
    {"question": "Which planet is known as the 'Red Planet'?", "answer": "Mars"},
    {"question": "In which year did the Berlin Wall fall?", "answer": "1989"},
    {"question": "What is the largest species of shark?", "answer": "Whale shark"},
    {"question": "What is the main component of the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "Who was the first woman to win a Nobel Prize?", "answer": "Marie Curie"},
    {"question": "In which war was the Battle of Gettysburg fought?", "answer": "American Civil War"},
    {"question": "What is the Great Depression known for?", "answer": "Economic crisis in the 1930s"},
    {"question": "Who is known for leading the Salt March in India?", "answer": "Mahatma Gandhi"},
    {"question": "In which country was the game of chess invented?", "answer": "India"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "What gas do plants release during photosynthesis?", "answer": "Oxygen"},
    {"question": "Who is known for formulating the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the longest river in Europe?", "answer": "Volga River"},
    {"question": "In which country is the Great Barrier Reef located?", "answer": "Australia"},
    {"question": "What is the world's largest archipelago?", "answer": "Indonesia"},
    {"question": "Which U.S. state is known as the 'Sunshine State'?", "answer": "Florida"},
    {"question": "What is the capital of South Korea?", "answer": "Seoul"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
    {"question": "How many time zones are there in the world?", "answer": "24"},
    {"question": "What is the most abundant gas in the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "Which gas do plants absorb from the atmosphere during photosynthesis?", "answer": "Carbon dioxide"},
    {"question": "What is the capital of Brazil?", "answer": "Brasília"},
    {"question": "What year did Christopher Columbus first arrive in the Americas?", "answer": "1492"},
    {"question": "Who was the first person to orbit the Earth?", "answer": "Yuri Gagarin"},
    {"question": "In which year did the Russian Revolution occur?", "answer": "1917"},
    {"question": "Who was the 16th President of the United States?", "answer": "Abraham Lincoln"},
    {"question": "What is the oldest known ancient civilization?", "answer": "Sumer"},
    {"question": "What is the atomic number of carbon?", "answer": "6"},
    {"question": "What is the process by which plants make their own food using sunlight?", "answer": "Photosynthesis"},
    {"question": "What is the pH scale used to measure?", "answer": "Acidity or alkalinity"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "Who is known for the discovery of penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the largest desert in the world?", "answer": "Antarctica"},
    {"question": "In which country is Mount Kilimanjaro located?", "answer": "Tanzania"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "Which river flows through Cairo, Egypt?", "answer": "Nile River"},
    {"question": "What is the highest mountain in North America?", "answer": "Denali"},
]

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE1NjU2MjkxNjMyMjA3MDUyOA.GVHJ0r.k7O8-EXgqQ2fxK8f973hK_IA4k6efAHUa7UKFY')