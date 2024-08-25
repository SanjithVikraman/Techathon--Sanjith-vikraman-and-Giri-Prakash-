import spacy
import random

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define possible responses
responses = {
    "stress": [
        "I'm sorry to hear you're feeling stressed. How can I assist you? Do you want an exercise, music, or a motivational quote?",
        "Stress can be tough. Would you like some exercises, calming music, or a motivational quote?",
        "I will help you to come out of stress"
    ],
    "anxious": [
        "It sounds like you're feeling anxious. Try some deep breathing or listen to calming music. How can I help?",
        "Anxiety is challenging. Would you like a breathing exercise, relaxing music, or a motivational quote?"
    ],
    "burnout": [
        "Burnout can be overwhelming. Taking breaks and practicing mindfulness might help. What can I do for you?",
        "Feeling burned out is difficult. Consider some relaxation exercises, calming music, or a motivational quote."
    ],
    "exercise": [
        "Here's a simple exercise: Deep Breathing - Breathe in deeply through your nose for 4 counts, hold for 4 counts, and exhale through your mouth for 4 counts. Repeat 5 times.",
        "Try Progressive Muscle Relaxation: Tense each muscle group for 5 seconds, then relax for 30 seconds, starting from your toes and working your way up.",
        """Deep Breathing How-To: Sit or lie down comfortably. Breathe in deeply through your nose for 4 counts, hold for 4 counts, and exhale slowly through your mouth for 4 counts. Repeat for 5-10 minutes.
         Benefit: Helps calm the nervous system and reduce anxiety.""",
        """Progressive Muscle Relaxation
How-To: Tense each muscle group (e.g., feet, calves, thighs, abdomen, arms, shoulders, and face) for 5 seconds, then relax for 30 seconds. Move progressively from toes to head.
Benefit: Reduces physical tension and promotes relaxation""",
        """Stretching
How-To: Perform gentle stretches such as reaching for the sky, touching your toes, and side stretches. Hold each stretch for 15-30 seconds.
Benefit: Relieves muscle tension and improves flexibility.""",
        """Walking or Light Jogging

How-To: Take a brisk walk or a light jog for 20-30 minutes. You can do this outdoors or on a treadmill.
Benefit: Increases endorphins, which improve mood and reduce stress.""","""Yoga

How-To: Practice yoga poses such as Child's Pose, Cat-Cow Stretch, Downward Dog, and Corpse Pose. Follow a guided yoga session or video if needed.
Benefit: Combines physical movement, breath control, and mindfulness to alleviate stress.""",
        """Tai Chi

How-To: Practice slow, flowing movements and deep breathing. Tai Chi can be learned through classes or guided videos.
Benefit: Improves balance and reduces stress through mindful movement.
""",
"""Visualization

How-To: Imagine a peaceful scene, such as a beach or forest. Visualize yourself in that place, focusing on the sights, sounds, and feelings of relaxation.
Benefit: Helps reduce stress by creating a mental escape from daily pressures.""",
        """Mindfulness Meditation

How-To: Sit quietly and focus on your breath or a specific object. Notice your thoughts and feelings without judgment. Practice for 10-15 minutes.
Benefit: Enhances awareness and helps manage stress by focusing on the present moment.""",
        """Body Scan Meditation

How-To: Lie down or sit comfortably. Close your eyes and mentally scan your body from head to toe, noticing any areas of tension or discomfort without judgment.
Benefit: Increases body awareness and helps release physical tension.""",
        """Journaling

How-To: Write down your thoughts, feelings, and any stressors you’re experiencing. Reflect on positive experiences and things you’re grateful for.
Benefit: Provides an outlet for expressing emotions and gaining perspective on stressors."""
    ],
    "music": [
        "Listen to this calming music: [Link to Music](https://www.example.com/music/track1.mp3)",
        "Here's a relaxing track for you: [Link to Music](https://www.example.com/music/track2.mp3)"
    ],
    "quote": [
        "Here's a motivational quote: 'The best way to predict the future is to create it.'",
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "The best way to predict the future is to create it." ,
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "The only way to do great work is to love what you do.",
        "In the middle of every difficulty lies opportunity.",
        "It does not matter how slowly you go as long as you do not stop.",
        "You are never too old to set another goal or to dream a new dream." ,
        "Believe you can and you're halfway there." ,
        "Start where you are. Use what you have. Do what you can.",
        "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Act as if what you do makes a difference. It does." ,
        "You do not find the happy life. You make it.",
        "Happiness is not something ready made. It comes from your own actions.",
        "Challenges are what make life interesting and overcoming them is what makes life meaningful." ,
        "Your present circumstances don't determine where you can go; they merely determine where you start."
    ]
}

def get_response(user_input):
    doc = nlp(user_input.lower())
    response_key = None
    
    # Check for keywords in user input
    for token in doc:
        if token.lemma_ in responses:
            response_key = token.lemma_
            break

    # Return a random response if a keyword was found, otherwise a default message
    if response_key:
        return random.choice(responses[response_key])
    else:
        return "I can help with stress management. Try asking for exercises, music, or quotes."

def main():
    print("Stress Relief Chatbot: How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Take care.")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()