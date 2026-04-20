from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
from elevenlabs_text_to_audio_podcast_converter import ElevenlabsTextToAudioPodcastConverter


load_dotenv()

class AiDrivenAiTTSConverterFromTextDocument:
    def __init__(self):
        self.prompt = """
        Your role: You will convert a given text data into ai/tts friendly version so that i can feed the output to my audio podcast generator.
        Some important information that need to be maintained : 
        * the podcast script should be as human like as possible with intonation, proper use of pause, some humor, proper use sentiment while talkinng about something that needs more careful phrasing
        
        Here is the data : 

        {}
        """
        self.llm = Ollama(model=os.getenv("llm_model_name"))

    def convert_text_into_tts(self, text_doc:str)->str:
        self.prompt = self.prompt.format(text_doc)
        
        
        response = self.llm.invoke(self.prompt)
        
        return response
    
    
if __name__ == "__main__":
    print("Starting the testing")
    text_data = """
    🎙️ Podcast Title: “Let’s Talk Real”
Episode: Discipline – Building a Strong Life

[Intro Music Fades In]

Host (Masud):
Hey everyone, welcome back to Let’s Talk Real, the podcast where we talk about real life in a simple way. I’m Masud.

Host (Sara):
And I’m Sara.

Host (Masud):
Today we’re talking about something that shapes your entire life: discipline.

Host (Sara):
Not motivation. Not luck. Discipline.

Host (Masud):
Let’s get into it.

[Music fades out]

Segment 1: What is discipline?

Host (Sara):
So Masud, what does discipline actually mean in simple words?

Host (Masud):
Discipline is doing what you need to do, even when you don’t feel like doing it.

Host (Sara):
That sounds simple, but it’s actually really hard in real life.

Host (Masud):
Exactly. It’s waking up when you’re tired.
It’s studying when you’re distracted.
It’s continuing when you want to quit.

Host (Sara):
So it’s basically doing the uncomfortable thing anyway.

Host (Masud):
Yes. That’s discipline.

Segment 2: Why discipline matters

Host (Masud):
Most people think success comes from motivation or talent.

Host (Sara):
But it doesn’t, right?

Host (Masud):
Not really. Success comes from consistency.
Doing small things every day, even when you don’t feel like it.

Host (Sara):
So discipline is like the foundation of everything.

Host (Masud):
Exactly. Without it, nothing stays stable.

Segment 3: Motivation vs Discipline

Host (Sara):
People always say “I need motivation first.”

Host (Masud):
And that’s the problem. Motivation is temporary.

Host (Sara):
It comes and goes.

Host (Masud):
One day you feel powerful.
The next day you feel nothing.

Host (Sara):
So if you depend on motivation, you keep restarting your life.

Host (Masud):
Exactly. Discipline keeps you moving even when motivation disappears.

Segment 4: Why discipline is hard

Host (Masud):
Let’s be honest. Discipline is uncomfortable at the beginning.

Host (Sara):
Your mind resists it.

Host (Masud):
Yes. It tells you to delay things.
It says “start tomorrow.”
It gives you excuses.

Host (Sara):
And everyone goes through that.

Host (Masud):
Everyone. The difference is whether you listen or not.

Segment 5: How to build discipline

Host (Sara):
So how do you actually build it?

Host (Masud):
You start small.

Host (Sara):
How small?

Host (Masud):
Very small. Ten minutes of focus. One task a day. One habit repeated daily.

Host (Sara):
So not big changes.

Host (Masud):
No. Small consistent actions. That’s what builds discipline.

Segment 6: The truth about discipline

Host (Masud):
At first, discipline feels hard. It feels like pressure.

Host (Sara):
But does it get easier?

Host (Masud):
Yes. Over time, it becomes freedom.

Host (Sara):
Freedom from what?

Host (Masud):
Freedom from emotions controlling your life.

Host (Sara):
That’s powerful.

Host (Masud):
It is. Once you’re disciplined, you control your actions, not your mood.

[Outro Music Starts Softly]

Host (Sara):
So if there’s one thing to remember, it’s this: don’t wait for motivation.

Host (Masud):
Start with discipline. Even small steps matter.

Host (Sara):
Because that’s how real change begins.

Host (Masud):
Thank you for listening.

Host (Sara):
This was Let’s Talk Real.

Together:
Stay consistent. Stay disciplined.

[Outro Music Fades Out]
    """
    
    tts_formated_string = AiDrivenAiTTSConverterFromTextDocument().convert_text_into_tts(text_data)
    # print("printing the tts formated string \n {}".format(tts_formated_string))
    ElevenlabsTextToAudioPodcastConverter().convert_to_podcast(tts_formated_string)