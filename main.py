from dotenv import load_dotenv
from src.elevenlabs_text_to_audio_podcast_converter import ElevenlabsTextToAudioPodcastConverter
load_dotenv()

if __name__ == "__main__":
      podcast_text ="""
    Podcast Title: Let’s Talk Real
Episode: Marijuana – Effects and Reality

Intro.

Hello.
Welcome to Let’s Talk Real.
I am your host, Masud.

Today we will talk about marijuana.
We will discuss what it is, why people use it, and its effects.

Let us begin.

Section 1. What is marijuana?

Marijuana is a plant.
People use it for recreational and medical purposes.

The main chemical in marijuana is THC.
THC affects the brain.
It creates a feeling known as a “high.”

Section 2. Why do people use it?

Some people use marijuana to relax.
It may help reduce stress.
It may also help with sleep.

Other people use it in social situations.

In some countries, marijuana is used for medical reasons.
Doctors may prescribe it for pain or anxiety.

Section 3. Possible negative effects.

Marijuana can affect memory.
It can reduce focus.
It may lower motivation.

Some users may feel anxiety or paranoia.

Regular use can lead to dependency.

Smoking marijuana may also affect lung health.

Section 4. Final thoughts.

Marijuana is not the same for everyone.
Its effects depend on the person.
It also depends on how often it is used.

It is important to stay aware.
Understand the risks.
Make informed decisions.

Conclusion.

Thank you for listening.
This was Let’s Talk Real.

Goodbye.

    
    """
    
    
ElevenlabsTextToAudioPodcastConverter().convert_to_podcast(podcast_text)
